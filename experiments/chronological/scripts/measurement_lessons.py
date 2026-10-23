"""Build small, visible worked examples from recorded registration evidence.

Run with the established Python environment. This does not rerun ORB, optimization,
or the research searches. It checks their saved coordinates and computes three
small, precisely labelled MRI score samples on the original common mask.
"""
from pathlib import Path
import hashlib
import importlib.util
import json
import math

ROOT = Path(__file__).resolve().parents[1]
WORKSPACE = ROOT.parent


def load(relative):
    return json.loads((WORKSPACE / relative).read_text(encoding="utf-8"))


def distance(first, second):
    """The straight-line gap between two addresses, in the same coordinate order."""
    return math.sqrt(sum((a-b)**2 for a, b in zip(first, second)))


def apply(matrix, point):
    """Apply the first two rows of an affine matrix to an (x,y) address."""
    x, y = point
    return [matrix[0][0]*x + matrix[0][1]*y + matrix[0][2],
            matrix[1][0]*x + matrix[1][1]*y + matrix[1][2]]


def inverse(matrix):
    """Undo a nonsingular 2-D affine transform; return a readable 2-by-3 matrix."""
    a, b, tx = matrix[0]
    c, d, ty = matrix[1]
    determinant = a*d-b*c
    assert abs(determinant) > 1e-12, "Cannot undo a collapsed coordinate system."
    return [[d/determinant, -b/determinant, (b*ty-d*tx)/determinant],
            [-c/determinant, a/determinant, (c*tx-a*ty)/determinant]]


def entropy(probabilities):
    # Empty cells contribute zero; never evaluate log(0).
    return -sum(p*math.log(p) for p in probabilities if p > 0)


def information_case(identifier, first, second, explanation):
    """Count four observed label pairs before introducing any equation."""
    count = len(first)
    counts = [[sum(a==i and b==j for a,b in zip(first,second)) for j in [0,1]] for i in [0,1]]
    joint = [[c/count for c in row] for row in counts]
    marginal_first = [sum(row) for row in joint]
    marginal_second = [sum(joint[i][j] for i in [0,1]) for j in [0,1]]
    cells = []
    for i in [0,1]:
        for j in [0,1]:
            p = joint[i][j]
            independent_probability = marginal_first[i]*marginal_second[j]
            ratio = p/independent_probability if p > 0 else None
            log_ratio = math.log(ratio) if p > 0 else None
            contribution = p*log_ratio if p > 0 else 0.0
            cells.append({"first_label":i,"second_label":j,"count":counts[i][j],
                          "joint_probability":p,"first_probability":marginal_first[i],
                          "second_probability":marginal_second[j],
                          "independent_probability":independent_probability,
                          "ratio":ratio,"natural_log_ratio":log_ratio,
                          "mi_contribution_nats":contribution})
    h_first = entropy(marginal_first)
    h_second = entropy(marginal_second)
    h_joint = entropy([p for row in joint for p in row])
    mi = sum(cell["mi_contribution_nats"] for cell in cells)
    nmi = (h_first+h_second)/h_joint if h_joint > 0 else None
    assert math.isclose(mi, h_first+h_second-h_joint, abs_tol=1e-12)
    return {"id":identifier,"first_labels":first,"second_labels":second,
            "pairs":[{"pair":i+1,"first":a,"second":b} for i,(a,b) in enumerate(zip(first,second))],
            "sample_count":count,"counts":counts,"joint_probabilities":joint,
            "marginal_first":marginal_first,"marginal_second":marginal_second,
            "cells":cells,"h_first_nats":h_first,"h_second_nats":h_second,
            "h_joint_nats":h_joint,"mi_nats":mi,"nmi":nmi,
            "nmi_numerator_nats":h_first+h_second,"explanation":explanation,
            "nmi_interpretation":"Undefined: both images are flat, so the formula asks for 0/0." if nmi is None else "An entropy ratio, not a percentage or geometric accuracy."}


def recorded_points(study_id, case, known_forward):
    """Verify every saved check point using its true generator and estimated undo."""
    check = case["independent_check"]
    estimated_forward = case["estimated_forward"]
    undo = inverse(estimated_forward)
    rows = []
    for i,(fixed,moving,recovered,stored_gap) in enumerate(zip(
            check["fixed_points"],check["true_moving_points"],
            check["recovered_points"],check["distances_fixed_px"])):
        assert distance(apply(known_forward,fixed),moving) < 1e-9
        assert distance(apply(undo,moving),recovered) < 1e-9
        gap = [recovered[j]-fixed[j] for j in [0,1]]
        measured = distance(recovered,fixed)
        assert math.isclose(measured,stored_gap,abs_tol=1e-9)
        rows.append({"point":i+1,"fixed_xy_px":fixed,"known_moving_xy_px":moving,
                     "estimated_recovered_xy_px":recovered,"gap_xy_fixed_px":gap,
                     "distance_fixed_px":measured})
    mean = sum(r["distance_fixed_px"] for r in rows)/len(rows)
    assert math.isclose(mean,check["mean_error_fixed_px"],abs_tol=1e-9)
    assert check["used_for_fitting"] is False
    return {"study_id":study_id,"case_id":case["case_id"],"known_forward_fixed_to_moving":known_forward,
            "estimated_forward_fixed_to_moving":estimated_forward,
            "estimated_undo_moving_to_fixed":undo,"rows":rows,
            "point_count":len(rows),"mean_distance_fixed_px":mean,
            "point_rmse_fixed_px":math.sqrt(sum(r["distance_fixed_px"]**2 for r in rows)/len(rows)),
            "used_for_fitting":False,"meaning":"Average leftover position error on 25 exact check points that did not fit or vote; fixed-image pixels."}


def mri_score_samples(genuine):
    """Recompute only three 27,756-pixel comparisons, using original functions.

    These extra scalar samples explain before/after; recorded exhaustive-search
    optima are loaded unchanged. The PD-only mask and margin are identical to the
    source search, and every state compares exactly the same fixed coordinates.
    """
    spec = importlib.util.spec_from_file_location("measurement_source_lab", WORKSPACE/"scripts/registration_lab.py")
    source = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(source)
    import numpy as np
    fixed = source.image("brain_pd.png", None)
    original_t1 = source.image("brain_t1.png", None)
    moving = source.warp(original_t1, source.transform(9,-6,shape=fixed.shape))
    height, width = fixed.shape
    margin = 27
    a = fixed[margin:height-margin,margin:width-margin]
    selection = (fixed > .07)[margin:height-margin,margin:width-margin]
    aa = a[selection]
    az = aa-aa.mean()
    rows = []
    for label, candidate, correction in [("native_pair",original_t1,[0,0]),
                                         ("added_shift_before_correction",moving,[0,0]),
                                         ("added_shift_after_correction",moving,[-9,6])]:
        dx, dy = correction
        bb = candidate[margin-dy:height-margin-dy,margin-dx:width-margin-dx][selection]
        bz = bb-bb.mean()
        rows.append({"state":label,"applied_correction_xy_px":correction,
                     "mse_squared_normalized_brightness":float(np.mean((aa-bb)**2)),
                     "signed_ncc":float((az@bz)/(np.linalg.norm(az)*np.linalg.norm(bz))),
                     "mi_nats":source.mi(aa,bb,bins=32),"sample_count":len(aa)})
    assert all(row["sample_count"] == 27756 for row in rows)
    # An integer displacement and its integer inverse return the sampled T1 values.
    for metric in ["mse_squared_normalized_brightness","signed_ncc","mi_nats"]:
        assert rows[0][metric] == rows[2][metric]
    return rows


def build():
    studies = load("research/results/study_results.json")["studies"]
    genuine = load("results/multimodal.json")["genuine"]
    r3 = next(row for row in studies["R3"]["rows"] if row["condition"]=="clean" and row["upsample_factor"]==1)
    known = studies["R3"]["settings"]["known_correction_yx_px"]
    estimated = [r3["estimated_correction_y_px"],r3["estimated_correction_x_px"]]
    translation = {"source_case":"R3 clean, upsample factor 1","order":"y,x",
                   "known_correction_yx_px":known,"estimated_correction_yx_px":estimated,
                   "gap_yx_px":[estimated[i]-known[i] for i in [0,1]],
                   "absolute_gap_yx_px":[abs(estimated[i]-known[i]) for i in [0,1]],
                   "squared_gaps_px2":[(estimated[i]-known[i])**2 for i in [0,1]],
                   "error_px":distance(known,estimated),
                   "arithmetic":"y gap = -5 - (-5.4) = +0.4; x gap = +4 - (+3.7) = +0.3; sqrt(0.4^2 + 0.3^2) = 0.5 px.",
                   "purpose":"Measure how far the estimated translation is from the translation deliberately introduced.",
                   "limit":"The row with extra rotation compares only translation components; a translation cannot undo that rotation. It is not full point-alignment error there.",
                   "grid_warning":"A 0.01-pixel search grid offers finer choices; it does not guarantee 0.01-pixel accuracy."}
    assert math.isclose(translation["error_px"],r3["translation_component_error_px"],abs_tol=1e-12)
    wrong = next(row for row in studies["R4"]["rows"] if row["contrast"]=="inverted" and row["metric"]=="mse")
    truth = studies["R4"]["settings"]["known_sampling_offset_xy_px"]
    chosen = [wrong["best_sampling_x_px"],wrong["best_sampling_y_px"]]
    offset = {"source_case":"R4 inverted contrast, MSE","order":"x,y","known_sampling_xy_px":truth,
              "chosen_sampling_xy_px":chosen,"gap_xy_px":[chosen[i]-truth[i] for i in [0,1]],
              "squared_gaps_px2":[(chosen[i]-truth[i])**2 for i in [0,1]],
              "error_px":distance(truth,chosen),"known_content_correction_xy_px":[-x for x in truth],
              "chosen_content_correction_xy_px":[-x for x in chosen],
              "arithmetic":"x gap = 10 - 6 = 4; y gap = 10 - (-4) = 14; sqrt(4^2 + 14^2) = sqrt(212) = 14.5602 px.",
              "meaning":"The selected address is about 14.56 pixels away from the known correct address; smaller is better, zero is exact for this model.",
              "sampling_explanation":"Sampling (+6,-4) reads M(x+6,y-4) for F(x,y). Moving the visible content to its target uses the opposite correction (-6,+4).",
              "limit":"This distance checks pure translation on controlled data. Image similarity scores and full-transform point error are different measurements."}
    assert math.isclose(offset["error_px"],wrong["geometric_error_px"],abs_tol=1e-12)
    cases = [information_case("same",[0,0,1,1],[0,0,1,1],"Knowing the first label predicts the second label exactly."),
             information_case("reversed",[0,0,1,1],[1,1,0,0],"Knowing the first label still predicts the second exactly, even though bright and dark swap."),
             information_case("independent",[0,0,1,1],[0,1,0,1],"Each first label occurs with both second labels equally; the first gives no clue."),
             information_case("both_flat",[0,0,0,0],[0,0,0,0],"There is no changing label to predict: MI is zero and this NMI formula is undefined.")]
    assert math.isclose(cases[0]["mi_nats"],math.log(2),abs_tol=1e-12)
    assert cases[0]["mi_nats"] == cases[1]["mi_nats"]
    assert cases[2]["mi_nats"] == 0 and cases[2]["nmi"] == 1
    assert cases[0]["nmi"] == 2 and cases[3]["nmi"] is None
    toy_rows = []
    for i,x in enumerate([10,20,30]):
        fixed = [x,0]
        moving = [2*x,0]
        recovered = [.55*moving[0],0]
        toy_rows.append({"point":i+1,"fixed_xy_px":fixed,"known_moving_xy_px":moving,
                         "estimated_recovered_xy_px":recovered,
                         "gap_xy_fixed_px":[recovered[0]-x,0],"distance_fixed_px":distance(fixed,recovered)})
    toy_mean = sum(row["distance_fixed_px"] for row in toy_rows)/3
    toy_rmse = math.sqrt(sum(row["distance_fixed_px"]**2 for row in toy_rows)/3)
    assert all(math.isclose(row["distance_fixed_px"],i+1,abs_tol=1e-12) for i,row in enumerate(toy_rows))
    assert math.isclose(toy_mean,2,abs_tol=1e-12) and toy_rmse > toy_mean
    r1 = next(case for case in studies["R1"]["traces"] if case["case_id"]=="spread_sigma_0p5")
    r2 = next(case for case in studies["R2"]["cases"] if case["case_id"]=="angle_0_blur_0p0")
    recorded_r1 = recorded_points("R1",r1,studies["R1"]["known_forward"])
    recorded_r2 = recorded_points("R2",r2,r2["known_forward"])
    methods = []
    for row in genuine["methods"]:
        native = [row["native_optimum_x_px"],row["native_optimum_y_px"]]
        perturbed = [row["shifted_optimum_x_px"],row["shifted_optimum_y_px"]]
        incremental = [perturbed[i]-native[i] for i in [0,1]]
        error = distance(incremental,[-9,6])
        assert error == row["perturbation_recovery_error_px"] == 0
        methods.append({"method":row["method"],"native_optimum_correction_xy_px":native,
                        "perturbed_optimum_correction_xy_px":perturbed,
                        "change_in_optimum_xy_px":incremental,"known_added_shift_correction_xy_px":[-9,6],
                        "perturbation_recovery_error_px":error,"sample_count":row["valid_pixels"]})
    sources = ["research/results/study_results.json","results/multimodal.json",
               "results/genuine_multimodal_search.csv","scripts/registration_lab.py",
               "data/brain_pd.png","data/brain_t1.png"]
    return {"schema_version":1,"presenter":"Mark Lester O. Dampios",
            "coordinate_key":{"xy":"x first: right is positive; y second: down is positive.",
                              "yx":"Array order: vertical y first, horizontal x second. Always read the heading.",
                              "px":"Pixel: a picture-grid unit. These data do not supply a millimetre conversion.",
                              "known":"Known because the researcher deliberately generated the movement.",
                              "estimate":"The movement selected by an algorithm, or explicitly supplied in the arithmetic toy.",
                              "error":"The gap from an estimate to a known correct answer; zero is ideal for that defined quantity."},
            "translation_error":translation,"offset_error":offset,
            "information":{"label_key":"0 = dark label, 1 = bright label; four paired addresses, not four subjects.",
                           "probability_rule":"Count a label pair, then divide by the four observed pairs.",
                           "marginal_rule":"A row total gives a first-image probability; a column total gives a second-image probability.",
                           "mi_rule":"For each nonzero cell add p(first,second) * ln[p(first,second)/(p(first)*p(second))]. Empty cells contribute zero.",
                           "entropy_rule":"For each nonzero probability add -p*ln(p). Entropy measures uncertainty in the labels, not their positions.",
                           "nmi_rule":"(H(first) + H(second)) / H(first,second)",
                           "log_key":"ln is the natural logarithm; ln(2)=0.693147. Using ln gives the information unit nats.",
                           "cases":cases,"use_case":"Try candidate image positions; a larger MI can prefer a more predictable intensity relationship even when bright and dark swap. This can help with different MRI contrasts.",
                           "nmi_use_case":"NMI rescales shared information using the images' entropies; it was proposed to reduce some overlap sensitivity. Cropping changes the observed content and probabilities; it does not guarantee a correct position.",
                           "limits":["MI does not output a shift: a search or optimizer compares its scores at candidate positions.",
                                     "Same and reversed labels both score 0.693 nats here; MI rewards predictability, not equal brightness.",
                                     "MI 0.693 is not 69.3% accuracy. NMI 2 is not 200% accuracy.",
                                     "Natural-image 32-bin scores differ from this two-label example; bins, samples and content matter.",
                                     "Repeated stripes can give the same perfect score at a wrong physical position."]},
            "independent_points":{"toy":{"status":"Calculation toy with a supplied estimate, not an algorithm result.",
                                            "known_forward_scale":2,"true_undo_scale":.5,"supplied_undo_scale":.55,
                                            "slider_undo_range":[.45,.55],"rows":toy_rows,"point_count":3,
                                            "mean_distance_fixed_px":toy_mean,"point_rmse_fixed_px":toy_rmse,
                                            "mean_arithmetic":"(1 + 2 + 3) / 3 = 2 fixed-image pixels.",
                                            "rmse_arithmetic":"sqrt((1^2 + 2^2 + 3^2) / 3) = sqrt(14/3) = 2.16025 fixed-image pixels.",
                                            "meaning":"All three points use one and the same supplied undo scale. Their exact coordinates were not used to fit that estimate."},
                                  "recorded_R1":recorded_r1,"recorded_R2":recorded_r2,
                                  "distinction":"A mean point distance averages straight-line position gaps. Point RMSE squares those gaps first. Brightness RMSE instead uses brightness differences; its unit is brightness, not pixels.",
                                  "why_independent":"Checking only points that fitted or voted can flatter the fit. Separate known check points test where the estimated transform sends other locations.",
                                  "interpretation":"Compare against no correction, the known answer and a declared application tolerance. The two-pixel classroom target is not an industry or clinical standard."},
            "mri":{"source":"Public ITK T1-weighted / proton-density MRI teaching pair; genuine MRI contrasts.",
                   "fixed":"PD","moving":"T1","image_size_xy_px":genuine["resolution_px"],
                   "introduced_content_shift_xy_px":genuine["introduced_shift_xy_px"],
                   "known_inverse_added_shift_xy_px":[-9,6],"introduced_displacement_magnitude_px":genuine["introduced_displacement_px"],
                   "before_added_shift_recovery_error_px":genuine["introduced_displacement_px"],
                   "after_added_shift_recovery_error_px":0,"methods":methods,
                   "score_samples":mri_score_samples(genuine),"score_samples_status":"Three new light comparisons, using the original image loading, warp, MI formula and exact original fixed ROI; no new search or algorithm fit.",
                   "roi":genuine["roi"],"mi_histogram_bins":32,"search_corrections_each_axis_px":[-16,16],"search_step_px":1,
                   "arithmetic":"Change in optimum = (-9,+6) - (0,0) = (-9,+6); compare with known inverse (-9,+6); gap (0,0), length 0 px.",
                   "achievement":"Every tested metric recovered the deliberately added integer displacement on this pair and search grid. Corrected scores return to this pair's native score values.",
                   "not_established":"The original supplied pair's perfect anatomical alignment, physical millimetre accuracy, other patients, other modality pairs or clinical fitness. There is no independent native anatomical ground truth here.",
                   "images":{"pd":"data/brain_pd.png","t1":"data/brain_t1.png","recorded_comparison":"figures/genuine_multimodal.png"},
                   "source_url":"https://github.com/InsightSoftwareConsortium/ITK/tree/50c5b33430e98b91b53fbaae2dd94f0edb2a639a/Examples/Data"},
            "validations":{"status":"passed","checks":["R3 component arithmetic matches actual saved row","R4 wrong-offset arithmetic matches actual saved row","MI cell sum equals entropy identity in all four cases","same and reversed MI match; independent MI zero","NMI 2, 1 and undefined cases","one transform produces all toy point distances","all 50 real R1/R2 check coordinates regenerate from known and estimated transforms","independent points were not used for fitting","MRI native-to-perturbed optimum difference matches known inverse","all three light MRI scores return exactly to native values on the same 27756 pixels"]},
            "sources":[{"path":relative,"sha256":hashlib.sha256((WORKSPACE/relative).read_bytes()).hexdigest()} for relative in sources]}


def render_figures(result):
    """Plot positions and a coordinate-gap triangle, with no slide-number artwork."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    plt.rcParams.update({"font.family":"DejaVu Sans","font.size":17,
                         "axes.titlesize":22,"axes.labelsize":17,
                         "xtick.labelsize":15,"ytick.labelsize":15})
    folder = ROOT/"figures"
    folder.mkdir(exist_ok=True)
    blue, green, orange = "#15557A", "#167358", "#AE511E"
    fig, ax = plt.subplots(figsize=(11,6.3))
    ax.set_xlim(0,25)
    ax.set_ylim(.2,3.8)
    ax.set_yticks([3,2,1],["Fixed address","Known moved address","Estimated return"])
    ax.set_xlabel("Horizontal address x (fixed and moving grids share this scale)")
    ax.set_title("Follow one check point: 10 → 20 → 11",pad=18)
    ax.scatter([10,20,11],[3,2,1],s=150,c=[blue,blue,orange],zorder=4)
    for x,y,label,offset,alignment in [(10,3,"(10, 0)",(0,14),"center"),
                                        (20,2,"(20, 0)",(18,-4),"left"),
                                        (11,1,"(11, 0)",(18,-3),"left")]:
        ax.annotate(label,(x,y),xytext=offset,textcoords="offset points",ha=alignment,weight="bold")
    ax.annotate("",xy=(20,2.12),xytext=(10,2.88),arrowprops={"arrowstyle":"->","color":blue,"lw":2})
    ax.text(16.5,2.68,"Known ×2",color=blue,ha="center")
    ax.annotate("",xy=(11,1.12),xytext=(20,1.88),arrowprops={"arrowstyle":"->","color":orange,"lw":2})
    ax.text(18,1.15,"Supplied undo ×0.55",color=orange,ha="center")
    ax.plot([10,10],[.65,3],"--",color=green,lw=2)
    ax.scatter([10],[1],s=90,facecolors="white",edgecolors=green,linewidths=2,zorder=5)
    ax.annotate("True undo ×0.50\nwould return to 10",(10,1),xytext=(3.3,.33),
                arrowprops={"arrowstyle":"->","color":green},color=green,ha="center",fontsize=16)
    ax.annotate("",xy=(11,.55),xytext=(10,.55),arrowprops={"arrowstyle":"|-|","color":orange,"lw":2})
    ax.text(18.2,.47,"Gap = |11 − 10| = 1 fixed px",fontsize=15,color=orange,ha="center")
    ax.spines[["top","right"]].set_visible(False)
    ax.grid(axis="x",alpha=.17)
    fig.text(.5,.015,"Calculation toy: one supplied estimate, not a fitted algorithm result. All y addresses are 0.",ha="center",fontsize=13)
    fig.tight_layout(rect=(0,.05,1,1))
    first = folder/"measurement_independent_trace.png"
    fig.savefig(first,dpi=180,facecolor="white")
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(11,6.3))
    known = (3.7,-5.4)
    estimated = (4,-5)
    corner = (4,-5.4)
    ax.plot([known[0],corner[0]],[known[1],corner[1]],color=blue,lw=3)
    ax.plot([corner[0],estimated[0]],[corner[1],estimated[1]],color=blue,lw=3)
    ax.plot([known[0],estimated[0]],[known[1],estimated[1]],color=orange,lw=3)
    ax.scatter([known[0],estimated[0]],[known[1],estimated[1]],s=130,c=[green,orange],zorder=4)
    ax.annotate("Known correction\n(x,y) = (+3.7, −5.4)",known,xytext=(-15,-49),textcoords="offset points",ha="right",color=green,fontsize=16)
    ax.annotate("Estimated correction\n(x,y) = (+4.0, −5.0)",estimated,xytext=(18,5),textcoords="offset points",color=orange,fontsize=16)
    ax.text(3.85,-5.43,"x gap 0.3 px",ha="center",va="bottom",fontsize=16,color=blue)
    ax.text(4.025,-5.21,"y gap\n0.4 px",ha="left",va="center",fontsize=16,color=blue)
    ax.text(3.74,-5.15,"Straight-line gap\n0.5 px",ha="right",color=orange,fontsize=17,weight="bold")
    ax.set_xlim(3.22,4.62)
    ax.set_ylim(-4.84,-5.65)
    ax.set_aspect("equal",adjustable="box")
    ax.set_xticks([3.5,3.7,4,4.3])
    ax.set_yticks([-5.6,-5.4,-5.2,-5])
    ax.set_xlabel("Horizontal correction x (pixels; right is positive)")
    ax.set_ylabel("Vertical correction y\n(pixels; down is positive)")
    ax.set_title("Translation error is a distance between two answers",pad=17)
    ax.grid(alpha=.17)
    ax.spines[["top","right"]].set_visible(False)
    fig.text(.5,.02,"sqrt(0.3² + 0.4²) = 0.5 px  |  R3 clean result, upsample factor 1; values are (x,y) on this plot.",ha="center",fontsize=14)
    fig.tight_layout(rect=(0,.065,1,1))
    second = folder/"measurement_translation_triangle.png"
    fig.savefig(second,dpi=180,facecolor="white")
    plt.close(fig)
    result["figures"] = {"independent_trace":str(first.relative_to(ROOT)).replace("\\","/"),
                          "translation_triangle":str(second.relative_to(ROOT)).replace("\\","/")}


if __name__ == "__main__":
    result = build()
    render_figures(result)
    for relative in ["content/measurement_lessons.json","results/measurement_lessons.json"]:
        path = ROOT/relative
        path.parent.mkdir(parents=True,exist_ok=True)
        path.write_text(json.dumps(result,indent=2,allow_nan=False),encoding="utf-8")
    print("Measurement lessons saved; all ten meaningful checks passed.")
    print("MRI score samples:",json.dumps(result["mri"]["score_samples"]))
