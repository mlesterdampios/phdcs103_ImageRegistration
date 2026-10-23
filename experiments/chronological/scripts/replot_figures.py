"""Replot existing measured data without obsolete PowerPoint slide labels.

No experiment is rerun and no original source file or old figure is overwritten.
This loads the original plotting definitions in memory, strips only literal legacy
slide-reference prefixes, and redirects new images to chronological/figures/.
Both baseline and new figures must contain identical numerical plotting artists.
"""
from pathlib import Path
import ast
import hashlib
import json
import re

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import cv2

ROOT=Path(__file__).resolve().parents[1]
WORKSPACE=ROOT.parent
FIGURES=ROOT/"figures"
FIGURES.mkdir(parents=True,exist_ok=True)
CONTENT=ROOT/"content"
CONTENT.mkdir(parents=True,exist_ok=True)

# Strip references such as 'Slides 17-19 |'. Scientific quantities elsewhere in
# the sentence (pixel counts, brightness values and coordinates) are preserved.
LEGACY_REFERENCE=re.compile(r"\b[Ss]lides?\s+\d+(?:\s*(?:[–−-]{1,2}|,|/|and|&)\s*\d+)*\s*[|·:]?\s*")


class RemoveLegacyReferences(ast.NodeTransformer):
    def visit_Constant(self,node):
        if isinstance(node.value,str):
            return ast.copy_location(ast.Constant(LEGACY_REFERENCE.sub("",node.value)),node)
        return node


def source_namespace(path,strip_references):
    """Evaluate a plotting source in memory; its __main__ experiments never run."""
    text=path.read_text(encoding="utf-8")
    tree=ast.parse(text,filename=str(path))
    if strip_references:
        tree=ast.fix_missing_locations(RemoveLegacyReferences().visit(tree))
    namespace={"__file__":str(path),"__name__":"chronological_plot_definitions"}
    exec(compile(tree,str(path),"exec"),namespace)
    namespace["FIGURES"]=FIGURES
    return namespace


def numeric_value(value):
    array=np.ma.filled(np.ma.asarray(value),np.nan)
    # All plotted values in these experiments are finite; str supports any table
    # labels without changing numerical precision in their displayed entries.
    return np.asarray(array).tolist()


def numerical_artist_fingerprint(figure):
    """Fingerprint the measured values, coordinates, bars, images and table cells.

    This intentionally excludes titles, captions and layout bounding boxes: the
    new captions have no obsolete slide tags, so their occupied space may change.
    """
    axes_data=[]
    for axis in figure.axes:
        data={"lines":[],"images":[],"collections":[],"patches":[],"tables":[]}
        for line in axis.lines:
            data["lines"].append([numeric_value(line.get_xdata()),numeric_value(line.get_ydata())])
        for picture in axis.images:
            data["images"].append(numeric_value(picture.get_array()))
        for collection in axis.collections:
            data["collections"].append(numeric_value(collection.get_offsets()))
        for patch in axis.patches:
            if hasattr(patch,"get_x") and hasattr(patch,"get_y") and hasattr(patch,"get_width") and hasattr(patch,"get_height"):
                data["patches"].append([patch.get_x(),patch.get_y(),patch.get_width(),patch.get_height()])
            elif hasattr(patch,"radius"):
                data["patches"].append([list(patch.center),patch.radius])
        for table in axis.tables:
            data["tables"].append({str(key):cell.get_text().get_text() for key,cell in table.get_celld().items()})
        axes_data.append(data)
    encoded=json.dumps(axes_data,sort_keys=True,allow_nan=False,separators=(",",":"),default=str).encode()
    return hashlib.sha256(encoded).hexdigest()


def invoke(namespace,source_kind,results):
    if source_kind=="basic":
        return namespace["make_figures"](results["toy_metrics"],results["image_scan"],results["noise"],results["ransac"])
    trace=json.loads((WORKSPACE/"beginner/results/complete_orb_trace.json").read_text(encoding="utf-8"))
    fixed=cv2.imread(str(WORKSPACE/"beginner/data/complete_fixed.png"),0)
    moving=cv2.imread(str(WORKSPACE/"beginner/data/complete_moving.png"),0)
    registered=cv2.imread(str(WORKSPACE/"beginner/data/complete_registered.png"),0)
    return namespace["make_figures"](results,trace,fixed,moving,registered)


def regenerate(source_kind,source_path,results_path):
    results=json.loads(results_path.read_text(encoding="utf-8"))
    baseline={}
    original=source_namespace(source_path,False)
    def baseline_capture(figure,name,caption):
        baseline[name]=numerical_artist_fingerprint(figure)
        plt.close(figure)
        return "figures/"+name
    original["save_figure"]=baseline_capture
    invoke(original,source_kind,results)

    updated=source_namespace(source_path,True)
    native_save=updated["save_figure"]
    output=[]
    def checked_save(figure,name,caption):
        new_fingerprint=numerical_artist_fingerprint(figure)
        assert new_fingerprint==baseline[name],f"Numerical artist data changed in {name}"
        visible_text=[artist.get_text() for artist in figure.findobj() if hasattr(artist,"get_text")]
        assert not any(LEGACY_REFERENCE.search(value) for value in visible_text if isinstance(value,str)),name
        assert not LEGACY_REFERENCE.search(caption),name
        path=native_save(figure,name,caption)
        old_path=WORKSPACE/"beginner/figures"/name
        output.append({"original_basename":name,"new_path":path,
                       "original_path":str(old_path.relative_to(WORKSPACE)).replace("\\","/"),
                       "original_image_sha256":hashlib.sha256(old_path.read_bytes()).hexdigest(),
                       "new_image_sha256":hashlib.sha256((ROOT/path).read_bytes()).hexdigest(),
                       "source_plot_definition":str(source_path.relative_to(WORKSPACE)).replace("\\","/"),
                       "source_results":str(results_path.relative_to(WORKSPACE)).replace("\\","/"),
                       "source_results_sha256":hashlib.sha256(results_path.read_bytes()).hexdigest(),
                       "numerical_artist_sha256":new_fingerprint,
                       "same_plotted_data_as_baseline":True,"legacy_slide_labels_removed":True})
        return path
    updated["save_figure"]=checked_save
    invoke(updated,source_kind,results)
    return output


if __name__=="__main__":
    records=[]
    records+=regenerate("basic",WORKSPACE/"beginner/scripts/teaching_lab.py",WORKSPACE/"beginner/results/lesson_results.json")
    records+=regenerate("complete",WORKSPACE/"beginner/scripts/complete_lab.py",WORKSPACE/"beginner/results/complete_lab.json")
    manifest={"schema_version":1,"status":"passed","experiment_rerun":False,
              "method":"Same saved measurements and Matplotlib definitions; remove only literal legacy slide-reference prefixes in memory.",
              "figure_count":len(records),"figures":records,
              "basename_to_new_path":{row["original_basename"]:row["new_path"] for row in records}}
    (CONTENT/"figure_replot_map.json").write_text(json.dumps(manifest,indent=2),encoding="utf-8")
    print(f"Regenerated {len(records)} figures. All numerical artist fingerprints match their baselines.")
