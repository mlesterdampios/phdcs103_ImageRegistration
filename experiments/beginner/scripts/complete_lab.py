"""Worked explanations of every original-laboratory measurement, slides 35--52.

Run: python beginner/scripts/complete_lab.py
The photograph is public CC0. Its movement and appearance changes are synthetic.
ORB really runs in Python; browser lessons replay saved results rather than run ORB.
"""

from pathlib import Path
import csv
import hashlib
import json
import math
import shutil

import cv2
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
RESULTS = ROOT / "results"
FIGURES = ROOT / "figures"
for folder in [DATA, RESULTS, FIGURES]:
    folder.mkdir(exist_ok=True)
plt.rcParams.update({"font.size":11, "axes.titlesize":13, "figure.dpi":130,
                     "axes.spines.top":False, "axes.spines.right":False})
BLUE, ORANGE, GREEN, RED = "#1764a0", "#c15b19", "#21764c", "#aa3344"
SEED = 20261022


def save_json(path, value):
    """Strict JSON uses null instead of an invented number for missing answers."""
    path.write_text(json.dumps(value, indent=2, allow_nan=False), encoding="utf-8")


def save_csv(path, rows):
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def rmse(reference, other, valid=None):
    """Square brightness gaps, average, then take a square root.

    With values on a 0--1 brightness scale the result has brightness units,
    not pixels and not percent. The optional mask chooses actual valid samples.
    """
    difference = np.asarray(reference, float) - np.asarray(other, float)
    if valid is not None:
        difference = difference[np.asarray(valid, bool)]
    if difference.size == 0:
        return None
    return float(np.sqrt(np.mean(difference**2)))


def contrast_mode(values, mode):
    """Exactly match the original browser's brightness rules, with no clipping.

    The nonlinear rule is 1 - v**0.7. It is NOT (1-v)**0.65, which appeared
    in a different old notebook experiment. Here every input v lies in 0..1.
    """
    v = np.asarray(values, dtype=float)
    if mode == "same":
        return v.copy()
    if mode == "inverted":
        return 1 - v
    if mode == "nonlinear_inverted":
        return 1 - v**0.7
    raise ValueError("Choose same, inverted, or nonlinear_inverted.")


def transform_points(points, affine):
    """Apply x'=a*x+b*y+tx and y'=c*x+d*y+ty to each point."""
    coordinates = np.asarray(points, dtype=float)
    matrix = np.asarray(affine, dtype=float)
    return coordinates @ matrix[:, :2].T + matrix[:, 2]


def inverse_affine(affine):
    """An inverse undoes a transform; a full inverse is more than changing signs.

    A 3-by-3 homogeneous matrix stores a 2-D transform including translation.
    The final [0,0,1] row makes ordinary matrix inversion possible.
    """
    full = np.vstack([np.asarray(affine, float), [0, 0, 1]])
    return np.linalg.inv(full)[:2]


def public_camera():
    """Copy the existing CC0 source into this self-contained beginner package."""
    source = ROOT.parent / "data" / "camera.png"
    target = DATA / "camera.png"
    if source.exists():
        shutil.copyfile(source, target)
    if not target.exists():
        raise FileNotFoundError("The bundled CC0 camera.png source is required.")
    provenance = """# Public photograph and derived experiment images

`camera.png` is the 512 x 512 grayscale camera photograph provided by
`skimage.data.camera()`, photographer Lav Varshney. Official scikit-image
documentation identifies this image as CC0, with no copyright restrictions:
https://scikit-image.org/docs/stable/api/skimage.data.html#skimage.data.camera

It was copied from the original package's bundled `data/camera.png`; no internet
download is performed. `complete_fixed.png` is an area-resized 384 x 384 copy.
`complete_moving.png` is a researcher-made known geometric transformation.
`complete_registered.png` and `complete_oracle.png` are bilinear resamplings.
These are synthetic registration conditions on a public photograph, not real
multimodal acquisitions, satellite images, medical data, or a clinical validation.

SHA-256 checksums and library versions are saved in `../results/complete_lab.json`.
"""
    (DATA / "PROVENANCE.md").write_text(provenance, encoding="utf-8")
    original = cv2.imread(str(target), cv2.IMREAD_GRAYSCALE)
    if original is None:
        raise ValueError("The photograph could not be read.")
    # Area interpolation averages source pixels when reducing image dimensions.
    return cv2.resize(original, (384,384), interpolation=cv2.INTER_AREA)


def independent_grid(known_forward, estimated_forward):
    """Evaluate 25 unused geometric points in FIXED-image pixel coordinates.

    1. Start with exact reference grid points.
    2. Generate their exact moving locations using the known forward transform.
    3. Bring them back using the INVERSE of the estimated forward transform.
    4. Measure each leftover ruler distance in the fixed coordinate system.
    Neither the ORB fit nor RANSAC has access to these grid points.
    """
    positions = np.linspace(64,320,5)
    fixed_grid = np.array([[x,y] for y in positions for x in positions])
    true_moving_grid = transform_points(fixed_grid, known_forward)
    recovered_grid = transform_points(true_moving_grid, inverse_affine(estimated_forward))
    errors = np.linalg.norm(recovered_grid - fixed_grid, axis=1)
    return {"number_of_points":25, "coordinate_system":"fixed-image pixels",
            "fixed_points":fixed_grid.tolist(), "true_moving_points":true_moving_grid.tolist(),
            "recovered_points":recovered_grid.tolist(), "per_point_error_px":errors.tolist(),
            "mean_error_px":float(errors.mean()), "maximum_error_px":float(errors.max()),
            "used_for_fitting":False}


def fit_forward(source_points, target_points, threshold_px):
    """Fit a similarity transform: one scale, one rotation and two translations.

    Source is FIXED, target is MOVING. Therefore the RANSAC residual and threshold
    are measured in MOVING pixels. This differs from lesson 01's correction-only
    translation toy, where residuals were measured in fixed pixels.
    """
    cv2.setRNGSeed(SEED)
    affine, mask = cv2.estimateAffinePartial2D(
        np.asarray(source_points, np.float32), np.asarray(target_points, np.float32),
        method=cv2.RANSAC, ransacReprojThreshold=float(threshold_px),
        maxIters=3000, confidence=0.99, refineIters=10)
    if affine is None or mask is None:
        return None, None
    return affine, mask.ravel().astype(bool)


def run_orb():
    """Run the actual public-library pipeline and retain inspectable evidence."""
    cv2.setNumThreads(1)  # A small CPU experiment; no GPU is required.
    cv2.setRNGSeed(SEED)
    fixed = public_camera()
    height, width = fixed.shape
    # Positive OpenCV rotation angles turn the displayed picture anticlockwise.
    # Rotate and scale around the center, THEN add the stated x/y displacement.
    known_forward = cv2.getRotationMatrix2D((width/2,height/2), 6.0, 1.03)
    known_forward[:,2] += [14,-10]
    moving = cv2.warpAffine(fixed, known_forward, (width,height), flags=cv2.INTER_LINEAR,
                            borderMode=cv2.BORDER_CONSTANT, borderValue=0)
    # A valid mask tells real image support apart from artificial black padding.
    moving_support = cv2.warpAffine(np.ones(fixed.shape,np.float32), known_forward,
                                    (width,height), flags=cv2.INTER_LINEAR) >= 0.999
    cv2.imwrite(str(DATA/"complete_fixed.png"),fixed)
    cv2.imwrite(str(DATA/"complete_moving.png"),moving)

    # ORB finds recognizable keypoints, then gives each a 32-byte yes/no fingerprint.
    # WTA_K=2 selects ordinary binary comparisons, so NORM_HAMMING is appropriate.
    detector = cv2.ORB_create(nfeatures=1200, WTA_K=2)
    fixed_keypoints, fixed_descriptors = detector.detectAndCompute(fixed,None)
    moving_keypoints, moving_descriptors = detector.detectAndCompute(moving,None)
    if fixed_descriptors is None or moving_descriptors is None:
        raise RuntimeError("No ORB descriptors were found in the photograph.")
    matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=False)
    # For each fixed fingerprint, get its two nearest moving fingerprints.
    nearest_pairs = matcher.knnMatch(fixed_descriptors,moving_descriptors,k=2)
    records = []
    accepted_matches = []
    for choices in nearest_pairs:
        if len(choices) < 2:
            continue
        best, second = choices
        # A 0.75 cutoff is a chosen ambiguity filter, NOT 75% accuracy.
        # If the second distance is zero, two identical candidates are ambiguous.
        accepted = second.distance > 0 and best.distance < 0.75 * second.distance
        record = {"query_idx":int(best.queryIdx), "train_idx":int(best.trainIdx),
                  "best_hamming":int(best.distance), "second_hamming":int(second.distance),
                  "ratio":float(best.distance/second.distance) if second.distance>0 else None,
                  "passes_ratio":bool(accepted)}
        records.append(record)
        if accepted:
            accepted_matches.append(best)
    if len(accepted_matches)<3:
        raise RuntimeError("Too few unambiguous matches for the teaching fit.")
    source = np.array([fixed_keypoints[m.queryIdx].pt for m in accepted_matches])
    target = np.array([moving_keypoints[m.trainIdx].pt for m in accepted_matches])
    estimated_forward, inliers = fit_forward(source,target,3.0)
    if estimated_forward is None:
        raise RuntimeError("RANSAC could not fit this controlled experiment.")
    estimated_inverse = inverse_affine(estimated_forward)
    check = independent_grid(known_forward, estimated_forward)
    # Per-match residuals use the FORWARD model and MOVING coordinates.
    residuals = np.linalg.norm(transform_points(source,estimated_forward)-target,axis=1)
    accepted_records = []
    accepted_by_query = {r["query_idx"]:r for r in records if r["passes_ratio"]}
    for index,match in enumerate(accepted_matches):
        item = dict(accepted_by_query[match.queryIdx])
        item.update({"match_id":index+1,"fixed_xy":source[index].tolist(),
                     "moving_xy":target[index].tolist(),"ransac_inlier":bool(inliers[index]),
                     "forward_residual_moving_px":float(residuals[index]),
                     "final_within_3px":bool(residuals[index]<=3.0)})
        accepted_records.append(item)

    # Expose one REAL full descriptor pair, including its exact XOR bit count.
    sample_match = accepted_matches[0]
    first_bytes = fixed_descriptors[sample_match.queryIdx]
    second_bytes = moving_descriptors[sample_match.trainIdx]
    first_bits = np.unpackbits(first_bytes)
    second_bits = np.unpackbits(second_bytes)
    xor_bits = np.bitwise_xor(first_bits,second_bits)
    fingerprint = {"match_id":1,"query_idx":int(sample_match.queryIdx),"train_idx":int(sample_match.trainIdx),
                   "fixed_bytes":first_bytes.tolist(),"moving_bytes":second_bytes.tolist(),
                   "fixed_bits":"".join(str(int(v)) for v in first_bits),
                   "moving_bits":"".join(str(int(v)) for v in second_bits),
                   "different_bit_positions_zero_based":np.flatnonzero(xor_bits).tolist(),
                   "full_256_bit_hamming":int(xor_bits.sum()),
                   "first_16_bit_hamming":int(xor_bits[:16].sum()),
                   "note":"Actual OpenCV bytes, unpacked most-significant bit first for display; toy comparisons do not claim this internal layout."}
    assert fingerprint["full_256_bit_hamming"] == int(sample_match.distance)

    # Rewarp the same image with the estimated inverse and the known (oracle) inverse.
    oracle_inverse = inverse_affine(known_forward)
    registered = cv2.warpAffine(moving, estimated_inverse, (width,height), flags=cv2.INTER_LINEAR)
    oracle = cv2.warpAffine(moving, oracle_inverse, (width,height), flags=cv2.INTER_LINEAR)
    estimated_valid = cv2.warpAffine(moving_support.astype(np.float32),estimated_inverse,
                                    (width,height),flags=cv2.INTER_LINEAR) >= .999
    oracle_valid = cv2.warpAffine(moving_support.astype(np.float32),oracle_inverse,
                                 (width,height),flags=cv2.INTER_LINEAR) >= .999
    common_valid = moving_support & estimated_valid & oracle_valid
    image_errors = {"brightness_scale":"0..1", "common_valid_pixels":int(common_valid.sum()),
                    "before":rmse(fixed/255,moving/255,common_valid),
                    "estimated_inverse":rmse(fixed/255,registered/255,common_valid),
                    "known_inverse_oracle":rmse(fixed/255,oracle/255,common_valid),
                    "note":"Same valid pixel mask for all three. Bilinear resampling can leave brightness error even with the exact known inverse."}
    cv2.imwrite(str(DATA/"complete_registered.png"),registered)
    cv2.imwrite(str(DATA/"complete_oracle.png"),oracle)
    cv2.imwrite(str(DATA/"complete_common_valid_mask.png"),common_valid.astype(np.uint8)*255)

    threshold_rows = []
    for threshold in [.5,1,2,3,5,10]:
        affine, mask = fit_forward(source,target,threshold)
        if affine is None:
            threshold_rows.append({"threshold_moving_px":threshold,"inlier_count":0,"independent_mean_fixed_px":None})
        else:
            threshold_rows.append({"threshold_moving_px":threshold,"inlier_count":int(mask.sum()),
                                   "independent_mean_fixed_px":independent_grid(known_forward,affine)["mean_error_px"]})
    blank = np.zeros((64,64),np.uint8)
    blank_keypoints, blank_descriptors = detector.detectAndCompute(blank,None)
    failure = {"example":"64x64 blank black picture", "keypoint_count":len(blank_keypoints),
               "descriptor_count":0 if blank_descriptors is None else len(blank_descriptors),
               "outcome":"cannot register from ORB: no distinctive places; no transform or success score invented"}
    summary = {"status":"measured","library":"OpenCV","opencv_version":cv2.__version__,"seed":SEED,
               "image_shape_hw":[height,width],"image_provenance":"CC0 public camera photograph; generated geometric transform",
               "settings":{"nfeatures_max":1200,"WTA_K":2,"descriptor_bytes":32,"descriptor_bits":256,
                           "distance":"Hamming","ratio_cutoff":.75,"forward_ransac_threshold_moving_px":3.0,
                           "fit_model":"similarity: isotropic scale + rotation + x/y translation",
                           "max_iterations":3000,"confidence":.99,"refine_iterations":10},
               "generated_transform":{"rotation_degrees_opencv":6.0,"scale":1.03,"added_translation_xy_px":[14,-10],
                                      "rotation_scale_center_xy":[width/2,height/2]},
               "counts":{"fixed_keypoints":len(fixed_keypoints),"moving_keypoints":len(moving_keypoints),
                         "two_neighbor_queries":len(records),"ratio_pass_matches":len(accepted_matches),
                         "ransac_inliers":int(inliers.sum()),"ransac_rejections":int((~inliers).sum()),
                         "final_refit_residual_within_3px":int((residuals<=3).sum()),
                         "returned_inliers_final_residual_above_3px":int((inliers&(residuals>3)).sum()),
                         "returned_outliers_final_residual_within_3px":int(((~inliers)&(residuals<=3)).sum())},
               "mask_note":"Returned RANSAC mask records the voting stage. The final least-squares adjustment changes the model: some borderline final residuals cross the 3 px ruler. Keep returned-mask membership separate from final residual<=3.",
               "known_forward_fixed_to_moving":known_forward.tolist(),
               "estimated_forward_fixed_to_moving":estimated_forward.tolist(),
               "estimated_inverse_moving_to_fixed":estimated_inverse.tolist(),
               "independent_check":check,"image_rmse":image_errors,"fingerprint_example":fingerprint,
               "threshold_sweep":threshold_rows,"blank_failure":failure,
               "images":{"source":"data/camera.png","fixed":"data/complete_fixed.png",
                         "moving":"data/complete_moving.png","registered":"data/complete_registered.png",
                         "oracle":"data/complete_oracle.png","common_valid_mask":"data/complete_common_valid_mask.png"},
               "trace_path":"results/complete_orb_trace.json","browser_trace_path":"results/complete_orb_browser.json"}
    def keypoint_dict(k):
        return {"xy":[float(k.pt[0]),float(k.pt[1])],"size_px":float(k.size),
                "angle_degrees":float(k.angle),"response":float(k.response),"octave":int(k.octave)}
    trace = {"summary":summary,"fixed_keypoints":[keypoint_dict(k) for k in fixed_keypoints],
             "moving_keypoints":[keypoint_dict(k) for k in moving_keypoints],
             "fixed_descriptors_bytes":fixed_descriptors.tolist(),
             "moving_descriptors_bytes":moving_descriptors.tolist(),
             "nearest_neighbor_queries":records,"ratio_pass_matches":accepted_records}
    save_json(RESULTS/"complete_orb_trace.json",trace)
    # The browser does not need the entire descriptor bank to replay this experiment.
    browser = {"summary":summary,"keypoints_fixed_xy":[list(k.pt) for k in fixed_keypoints],
               "keypoints_moving_xy":[list(k.pt) for k in moving_keypoints],
               "ratio_pass_matches":accepted_records,
               "replay_notice":"Recorded actual Python/OpenCV ORB output; not a live browser feature detector."}
    save_json(RESULTS/"complete_orb_browser.json",browser)
    save_csv(RESULTS/"complete_orb_matches.csv",accepted_records)
    save_csv(RESULTS/"complete_orb_thresholds.csv",threshold_rows)
    grid_rows = [{"point_id":i+1,"fixed_x":a[0],"fixed_y":a[1],"recovered_x":b[0],"recovered_y":b[1],"error_fixed_px":e}
                 for i,(a,b,e) in enumerate(zip(check["fixed_points"],check["recovered_points"],check["per_point_error_px"]))]
    save_csv(RESULTS/"complete_independent_grid.csv",grid_rows)
    return summary, trace, fixed, moving, registered


def make_tiny_fingerprint():
    """Eight illustrated comparisons explain a fingerprint; NOT ORB's exact layout."""
    first = np.array([[1,4,2],[6,3,8],[5,0,7]])
    second = np.array([[1,4,2],[6,3,8],[5,7,0]])
    # Each row stores [A_y,A_x,B_y,B_x]; a test returns 1 when A is darker than B.
    comparisons = [[0,0,0,1],[0,1,0,2],[1,0,1,1],[1,1,1,2],
                   [2,0,2,1],[2,1,2,2],[0,2,2,2],[0,0,2,0]]
    rows=[]
    for i,(ay,ax,by,bx) in enumerate(comparisons):
        a_bit=int(first[ay,ax]<first[by,bx])
        b_bit=int(second[ay,ax]<second[by,bx])
        rows.append({"test":i+1,"A_xy":[ax,ay],"B_xy":[bx,by],
                     "first_A":int(first[ay,ax]),"first_B":int(first[by,bx]),
                     "second_A":int(second[ay,ax]),"second_B":int(second[by,bx]),
                     "first_bit":a_bit,"second_bit":b_bit,"different":a_bit!=b_bit})
    return {"first_patch":first.tolist(),"second_patch":second.tolist(),"tests":rows,
            "first_bits":"".join(str(r["first_bit"]) for r in rows),
            "second_bits":"".join(str(r["second_bit"]) for r in rows),
            "hamming_distance":sum(r["different"] for r in rows),
            "notice":"Illustrated 8-test BRIEF-like toy only; not OpenCV's true 256-test pattern, smoothing, orientation or scale handling."}


def save_figure(fig,name,caption):
    fig.text(.02,.015,caption,fontsize=10,va="bottom",wrap=True)
    fig.tight_layout(rect=(0,.11,1,.98))
    fig.savefig(FIGURES/name,facecolor="white",bbox_inches="tight")
    plt.close(fig)
    return "figures/"+name


def make_figures(data,trace,fixed,moving,registered):
    """Measured figures with labels, units, direction, and explicit limitations."""
    paths={}
    fig,ax=plt.subplots(figsize=(11,4.7));ax.axis("off")
    rows=[["1",0,1,-1,1],["2",1,1,0,0],["3",2,2,0,0],["4",3,2,1,1]]
    table=ax.table(cellText=rows,colLabels=["Compared pair","Reference","Other","Subtract","Square"],loc="center",cellLoc="center")
    table.auto_set_font_size(False);table.set_fontsize(13);table.scale(1,1.8)
    ax.set_title("Slide 37 | Square the gaps, average, then take a square root",pad=18)
    paths["rmse_steps"]=save_figure(fig,"complete_rmse_steps.png",
        "Squared gaps: 1+0+0+1=2; average: MSE=2/4=0.5 squared brightness units. Take square root: RMSE=sqrt(0.5)=0.707 brightness units. This is not a point distance or a percentage.")

    fig,axes=plt.subplots(1,2,figsize=(12,5.3),gridspec_kw={"width_ratios":[1.1,1]})
    x=np.linspace(0,1,201)
    for mode,label,color in [("same","Same: v",BLUE),("inverted","Inverted: 1-v",ORANGE),
                             ("nonlinear_inverted","Uneven inversion: 1-v^0.7",GREEN)]:
        axes[0].plot(x,contrast_mode(x,mode),label=label,color=color,linewidth=2)
    axes[0].set(xlabel="Input brightness v (0=dark, 1=bright)",ylabel="Output brightness after chosen rule",
                xticks=[0,.25,.5,.75,1],yticks=[0,.25,.5,.75,1],title="Slides 39-41 | Change brightness, not position")
    axes[0].legend(fontsize=9);axes[0].grid(alpha=.2)
    axes[1].axis("off")
    table=axes[1].table(cellText=[[f"{r['input']:.2f}",f"{r['same']:.3f}",f"{r['inverted']:.3f}",f"{r['nonlinear_inverted']:.3f}"] for r in data["contrast"]["table"]],
                         colLabels=["Input","Same","Inverted","Uneven\ninversion"],loc="center",cellLoc="center")
    table.auto_set_font_size(False);table.set_fontsize(12);table.scale(1,2)
    paths["contrast_modes"]=save_figure(fig,"complete_contrast_modes.png",
        "Read across from an input value to its new output. Same keeps it; inversion swaps dark and bright evenly; the curved rule changes middle values unequally. These are simulated appearance changes, not acquired imaging modalities.")

    fig,axes=plt.subplots(1,2,figsize=(11,5.7))
    for ax,image,keypoints,title in [(axes[0],fixed,trace["fixed_keypoints"],"Reference picture"),
                                     (axes[1],moving,trace["moving_keypoints"],"Generated movable picture")]:
        ax.imshow(image,cmap="gray",vmin=0,vmax=255)
        # Show 80 of the actual detections to keep circles readable, not all hundreds.
        visible=keypoints[:80]
        ax.scatter([k["xy"][0] for k in visible],[k["xy"][1] for k in visible],s=45,facecolors="none",edgecolors="#ffcf39",linewidths=.9)
        ax.set(title=title+f"\n{len(keypoints)} keypoints detected; first 80 circled",xlabel="x pixel address",ylabel="y pixel address (down)")
    paths["orb_keypoints"]=save_figure(fig,"complete_orb_keypoints.png",
        "Slide 42 | ORB really ran in Python/OpenCV. A keypoint is a distinctive place to describe, not a recognized person/object. Circles identify detected locations; they are not bounding boxes or evidence of correct matches.")

    # One canvas shows actual correspondences across the two images.
    fig,ax=plt.subplots(figsize=(12,6.5))
    ax.imshow(np.hstack([fixed,moving]),cmap="gray",vmin=0,vmax=255)
    matches=trace["ratio_pass_matches"]
    visible=[r for r in matches if not r["ransac_inlier"]][:8]+[r for r in matches if r["ransac_inlier"]][:24]
    for r in visible:
        a,b=r["fixed_xy"],r["moving_xy"]
        ax.plot([a[0],b[0]+384],[a[1],b[1]],color=GREEN if r["ransac_inlier"] else RED,alpha=.65,linewidth=1)
    counts=data["orb"]["counts"]
    ax.set(title=f"Slides 44-45 | Detected {counts['fixed_keypoints']} reference / {counts['moving_keypoints']} movable keypoints\n"
                 f"{counts['ratio_pass_matches']} ratio-filtered matches -> {counts['ransac_inliers']} returned RANSAC inliers / {counts['ransac_rejections']} rejected",
           xlabel="Reference x=0..383  |  Movable picture starts at display x=384",ylabel="y pixel address (down)")
    paths["orb_matches"]=save_figure(fig,"complete_orb_matches.png",
        "Lines link claimed pairs: up to 24 green voting-mask inliers and 8 red rejections shown. Counts report ALL data. The recipe is adjusted after voting; borderline final gaps can cross 3 px. Inlier is not a proven correct match.")

    fig,axes=plt.subplots(2,1,figsize=(11,5.5));axes[0].axis("off");axes[1].axis("off")
    toy=data["fingerprint_toy"]
    table=axes[0].table(cellText=[[r["test"],f"{r['first_A']} < {r['first_B']}?",r["first_bit"],f"{r['second_A']} < {r['second_B']}?",r["second_bit"]] for r in toy["tests"]],
                        colLabels=["Test","Patch 1 question","Bit","Patch 2 question","Bit"],loc="center",cellLoc="center")
    table.auto_set_font_size(False);table.set_fontsize(11);table.scale(1,1.25)
    axes[0].set_title("Slide 43 | Eight illustrated yes/no tests (toy, not ORB's internal layout)",pad=16)
    actual=data["orb"]["fingerprint_example"]
    axes[1].text(.02,.65,f"Toy fingerprints: {toy['first_bits']} and {toy['second_bits']}  ->  {toy['hamming_distance']} different bits",fontsize=14)
    axes[1].text(.02,.32,f"Actual ORB first 16 bits: {actual['fixed_bits'][:16]} / {actual['moving_bits'][:16]}",fontsize=13)
    axes[1].text(.02,.05,f"Actual full 256-bit Hamming distance = {actual['full_256_bit_hamming']}; first 16 bits differ at {actual['first_16_bit_hamming']} positions.",fontsize=12)
    paths["fingerprints"]=save_figure(fig,"complete_fingerprints.png",
        "One bit is one yes/no answer. A byte contains 8 bits; ORB WTA_K=2 produces 32 bytes=256 bits. Hamming distance counts different bits, not spatial pixels. Real ORB uses its own oriented/scale-aware pattern; the 8-test toy only illustrates the idea.")

    fig,axes=plt.subplots(1,2,figsize=(11,5.5))
    ax=axes[0]
    ax.scatter([10],[10],s=110,facecolors="none",edgecolors=BLUE,label="Claimed moving click (10,10)")
    ax.scatter([13],[14],s=55,color=ORANGE,label="Forward prediction (13,14)")
    ax.plot([10,13],[10,14],color=RED,linewidth=3)
    ax.plot([10,13,13],[10,10,14],"--",color="gray")
    ax.text(11.5,9.6,"3 px",ha="center");ax.text(13.3,12,"4 px");ax.text(10.4,12.7,"5 px residual",color=RED)
    ax.set(xlim=(8,16),ylim=(16,8),aspect="equal",xlabel="Moving-image x (px)",ylabel="Moving-image y (px), down",
           title="Slide 46 | ONE claimed pair's leftover")
    ax.legend(fontsize=8,loc="lower left")
    check=data["orb"]["independent_check"]
    a=np.array(check["fixed_points"]);b=np.array(check["recovered_points"])
    axes[1].scatter(a[:,0],a[:,1],facecolors="none",edgecolors=BLUE,s=60,label="25 exact independent targets")
    axes[1].scatter(b[:,0],b[:,1],color=ORANGE,s=12,label="Recovered by estimated inverse")
    axes[1].set(xlim=(40,345),ylim=(345,40),aspect="equal",xlabel="Fixed-image x (px)",ylabel="Fixed-image y (px), down",
                title=f"Slide 48 | 25 UNUSED check points\nMean distance = {check['mean_error_px']:.3f} fixed px")
    paths["residual_vs_check"]=save_figure(fig,"complete_residual_vs_check.png",
        "Left: separate 3-4-5 example; forward residual in MOVING pixels. Right: blue rings=25 unused exact targets; orange=actual ORB inverse-corrected points, checked in FIXED pixels. Check points never fitted or voted. Neither measurement is brightness RMSE.")

    fig,axes=plt.subplots(1,2,figsize=(11,4.7))
    rows=data["orb"]["threshold_sweep"];ts=[r["threshold_moving_px"] for r in rows]
    axes[0].plot(ts,[r["inlier_count"] for r in rows],"o-",color=BLUE)
    axes[0].set(xlabel="Voting ruler: forward threshold (moving px)",ylabel="Number of fitting matches accepted",title="Slide 47 | Wider ruler can accept more pairs")
    axes[1].plot(ts,[r["independent_mean_fixed_px"] for r in rows],"o-",color=ORANGE)
    axes[1].set(xlabel="Voting ruler: forward threshold (moving px)",ylabel="Mean independent error (fixed px)",title="Slide 48 | Check accuracy separately")
    for ax in axes:ax.grid(alpha=.2)
    paths["orb_thresholds"]=save_figure(fig,"complete_orb_thresholds.png",
        "Dots are measured fits using the same saved ORB matches with different thresholds. Joining lines guide the eye. A 3 px default is a chosen voting tolerance, not a universal accuracy standard; more accepted pairs need not improve the separate check.")

    fig,axes=plt.subplots(1,3,figsize=(12,4.9))
    for ax,image,title in zip(axes,[fixed,moving,registered],["Reference stays put","Generated: scale 1.03, rotate 6 deg\nthen add (+14,-10) px","Apply estimated inverse\n(correction back toward reference)"]):
        ax.imshow(image,cmap="gray",vmin=0,vmax=255);ax.set(title=title,xlabel="x pixel address",ylabel="y pixel address (down)")
    paths["transform_steps"]=save_figure(fig,"complete_transform_steps.png",
        "Slides 45,49-50 | Scale 1.03 means 3% larger linear dimensions, not 3% area. Black uncovered borders are padding, excluded from brightness scores. Inverse undoes the whole transform; interpolation mixes nearby pixels, so exact geometry need not give zero RMSE.")
    return paths


def run_all():
    values=[0,.25,.5,.75,1]
    table=[{"input":v,"same":float(contrast_mode(v,"same")),"inverted":float(contrast_mode(v,"inverted")),
            "nonlinear_inverted":float(contrast_mode(v,"nonlinear_inverted"))} for v in values]
    orb,trace,fixed,moving,registered=run_orb()
    # Save measured numeric evidence BEFORE building figures so other artifacts can read it.
    data={"schema_version":1,"scope":"original laboratory explanations, slides 35-52",
          "synthetic_conditions_on_public_photo":True,
          "rmse":{"reference":[0,1,2,3],"other":[1,1,2,2],"mse":.5,"rmse":math.sqrt(.5),
                  "unit":"brightness units; worked example is not restricted to the 0..1 range"},
          "contrast":{"table":table,"same":"v","inverted":"1-v","nonlinear_inverted":"1-v**0.7",
                      "input_output_units":"normalized brightness values 0..1","changes_geometry":False},
          "residual_example":{"predicted_moving_xy":[13,14],"claimed_moving_xy":[10,10],
                              "dx_px":3,"dy_px":4,"residual_moving_px":5,
                              "accepted_at_3px_threshold":False,"separate_arithmetic_example":True},
          "sampling_example":{"generated_image_shift_x_px":3,"sampling_offset_u_px":3,
                              "applied_content_correction_x_px":-3,"equation":"Compare M(p+u) with F(p)."},
          "fingerprint_toy":make_tiny_fingerprint(),"orb":orb,"figures":{}}
    data["provenance"]={"numpy_version":np.__version__,"opencv_version":cv2.__version__,
                        "camera_sha256":hashlib.sha256((DATA/"camera.png").read_bytes()).hexdigest(),
                        "camera_license":"CC0","camera_credit":"Lav Varshney via scikit-image",
                        "source_url":"https://scikit-image.org/docs/stable/api/skimage.data.html#skimage.data.camera"}
    save_json(RESULTS/"complete_lab.json",data)
    save_csv(RESULTS/"complete_contrast_table.csv",table)
    data["figures"]=make_figures(data,trace,fixed,moving,registered)
    # Verify actual known answers and independent geometry, not only file creation.
    assert abs(data["rmse"]["rmse"]**2-.5)<1e-12
    assert abs(table[1]["nonlinear_inverted"]-(1-.25**.7))<1e-12
    assert abs(table[2]["nonlinear_inverted"]-.38442779332754184)<1e-12
    assert orb["settings"]["descriptor_bytes"]*8==256
    assert orb["blank_failure"]["keypoint_count"]==0
    assert orb["counts"]["ratio_pass_matches"]>=20
    assert orb["independent_check"]["number_of_points"]==25
    assert orb["independent_check"]["mean_error_px"]<1.0
    true=np.array(orb["known_forward_fixed_to_moving"])
    points=np.array(orb["independent_check"]["fixed_points"])
    assert np.allclose(transform_points(transform_points(points,true),inverse_affine(true)),points)
    data["validation"]={"status":"passed","topics":["RMSE arithmetic","exact original nonlinear rule",
                          "actual descriptor bit count","blank no-feature failure","ratio matching and fit",
                          "25 independent unused checks","known inverse round trip"]}
    save_json(RESULTS/"complete_lab.json",data)
    return data


if __name__=="__main__":
    results=run_all()
    print("Actual ORB counts:",results["orb"]["counts"])
    print("Independent mean error (fixed px):",results["orb"]["independent_check"]["mean_error_px"])
    print("Brightness RMSE:",results["orb"]["image_rmse"])
    print("Complete explanation experiments:",results["validation"]["status"])
