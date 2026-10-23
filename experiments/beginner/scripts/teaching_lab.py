"""Reproducible, small teaching experiments for slides 3--31.

Run from any folder: python beginner/scripts/teaching_lab.py
All pictures and point pairs are synthetic. No patient or satellite data are used.
The saved answers are measurements from these examples, not industry targets.
"""

from pathlib import Path
import csv
import json
import math

import matplotlib
matplotlib.use("Agg")  # Save pictures without needing an open desktop window.
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
SPEC = json.loads((ROOT / "content" / "lesson_spec.json").read_text(encoding="utf-8"))
FIGURES = ROOT / "figures"
RESULTS = ROOT / "results"
FIGURES.mkdir(exist_ok=True)
RESULTS.mkdir(exist_ok=True)
plt.rcParams.update({"font.size": 11, "axes.titlesize": 13, "figure.dpi": 130,
                     "axes.spines.top": False, "axes.spines.right": False})
BLUE = "#1764a0"
ORANGE = "#c15b19"
GREEN = "#21764c"
RED = "#aa3344"


def mse(reference, other):
    """Subtract, square, add, divide by the number of compared pixels."""
    a = np.asarray(reference, dtype=float)
    b = np.asarray(other, dtype=float)
    if a.shape != b.shape or a.size == 0:
        raise ValueError("Compare equal, nonempty arrays of pixel values.")
    squared_differences = (a - b) ** 2
    return float(squared_differences.mean())


def signed_ncc(reference, other):
    """Compare centered up/down patterns; return None if either is flat.

    Centered means: subtract each array's own average. Dividing by the
    lengths of these centered arrays makes the result stay between -1 and +1.
    None is deliberately different from a measured score of zero.
    """
    a = np.asarray(reference, dtype=float).ravel()
    b = np.asarray(other, dtype=float).ravel()
    if a.shape != b.shape or a.size == 0:
        raise ValueError("Compare equal, nonempty arrays of pixel values.")
    a_centered = a - a.mean()
    b_centered = b - b.mean()
    denominator = np.linalg.norm(a_centered) * np.linalg.norm(b_centered)
    if denominator == 0:
        return None  # No variation means there is no up/down pattern to compare.
    return float(np.clip(np.dot(a_centered, b_centered) / denominator, -1, 1))


def binary_mi(reference, other):
    """Count 0/1 pairs, then measure how much the pair counts reveal.

    This intentionally tiny implementation accepts only the labels 0 and 1.
    It uses the natural logarithm, so its unit is 'nats'. Real grayscale
    pictures need chosen intensity bins; those choices affect the answer.
    """
    a = np.asarray(reference).ravel()
    b = np.asarray(other).ravel()
    if a.shape != b.shape or a.size == 0:
        raise ValueError("Compare equal, nonempty arrays of pixel labels.")
    if not np.isin(a, [0, 1]).all() or not np.isin(b, [0, 1]).all():
        raise ValueError("This teaching function needs binary labels 0 or 1.")
    counts = np.zeros((2, 2), dtype=int)
    for fixed_value, other_value in zip(a, b):
        counts[int(fixed_value), int(other_value)] += 1
    joint = counts / a.size  # A count divided by all pairs is a fraction.
    fixed_fraction = joint.sum(axis=1)
    other_fraction = joint.sum(axis=0)
    information = 0.0
    for i in range(2):
        for j in range(2):
            if joint[i, j] == 0:
                continue  # An empty cell contributes zero, not log(0).
            independent_fraction = fixed_fraction[i] * other_fraction[j]
            information += joint[i, j] * math.log(joint[i, j] / independent_fraction)
    return {"counts": counts.tolist(), "nats": float(information)}


def toy_metrics():
    """Answers for the four-number worked examples, slides 9--16."""
    a = np.array(SPEC["mse_reference"])
    b = np.array(SPEC["mse_other"])
    rows = [{"pixel": i + 1, "reference": int(x), "other": int(y),
             "difference": int(x - y), "squared_difference": int((x-y)**2)}
            for i, (x, y) in enumerate(zip(a, b))]
    ncc_cases = {}
    for name in ["brighter", "reversed", "zero", "flat"]:
        values = SPEC["ncc_" + name]
        score = signed_ncc(SPEC["ncc_reference"], values)
        ncc_cases[name] = {"values": values, "value": score,
                           "display": "cannot calculate: no variation" if score is None else f"{score:+.3f}"}
    mi_cases = {name: binary_mi(SPEC["mi_fixed"], SPEC["mi_" + name])
                for name in ["same", "reversed", "independent"]}
    return {"mse": {"rows": rows, "value": mse(a, b), "unit": "squared brightness units"},
            "ncc": ncc_cases, "mi": mi_cases}


def image_scan():
    """Try 13 horizontal corrections on a known-shift binary pixel strip.

    The original strip has 96 pixels, each either dark=0 or bright=1. Moving
    it right by 3 creates the movable picture. A correction of -3 means left
    by 3. Every score uses the same 81 real reference pixels x=9..89. This
    avoids judging a different crop or artificial blank border at each move.
    """
    rng = np.random.default_rng(SPEC["seed"])
    fixed = rng.integers(0, 2, size=96)
    moving = np.zeros_like(fixed)
    generated_shift = SPEC["image_forward_shift_x_px"]
    moving[generated_shift:] = fixed[:-generated_shift]
    corrections = SPEC["image_search_corrections"]
    x = np.arange(9, 90)  # Python's final endpoint is excluded; this is 9..89.
    scores = []
    for scenario in ["same_brightness", "brighter", "reversed_brightness"]:
        for correction in corrections:
            # corrected[x] = moving[x-correction]. This convention moves the
            # CONTENT left when correction is negative. No circular wrap occurs.
            observed = moving[x - correction].astype(float)
            if scenario == "brighter":
                observed += 0.25  # Keep numbers as measured; do not clip them.
            elif scenario == "reversed_brightness":
                observed = 1 - observed
            # Label 0/1 classes. A +0.25 offset stays in the same two classes.
            labels = (observed > 0.5).astype(int)
            scores.append({"scenario": scenario, "correction_x_px": correction,
                           "mse": mse(fixed[x], observed),
                           "signed_ncc": signed_ncc(fixed[x], observed),
                           "mi_nats": binary_mi(fixed[x], labels)["nats"]})
    best = {}
    for scenario in ["same_brightness", "brighter", "reversed_brightness"]:
        subset = [r for r in scores if r["scenario"] == scenario]
        best[scenario] = {}
        for metric, minimize in [("mse", True), ("signed_ncc", False), ("mi_nats", False)]:
            optimum = (min if minimize else max)(r[metric] for r in subset)
            best[scenario][metric] = [r["correction_x_px"] for r in subset if abs(r[metric]-optimum) < 1e-12]
    return {"fixed_row": fixed.tolist(), "moving_row": moving.tolist(),
            "known_forward_x_px": generated_shift, "true_correction_x_px": -generated_shift,
            "common_roi": {"first_x": 9, "last_x": 89, "number_of_pixels": len(x)},
            "scenarios": ["same_brightness", "brighter", "reversed_brightness"],
            "scores": scores, "best_corrections": best,
            "note": "Repeated rows in figures help visibility; scores use the 81 unique strip samples once."}


def point_data(sigma_px=None, include_wrong_matches=True):
    """Make observed moving-point locations with two separate kinds of error.

    The frozen normal offsets are the SAME draws at every sigma, so moving
    the slider changes only their scale. The errors are added to moving
    clicks; the fixed locations are treated as exact in this simple model.
    Wrong matches are separate large displacements, not extra sigma.
    """
    sigma = SPEC["sigma_px"] if sigma_px is None else sigma_px
    fixed = np.array(SPEC["fixed_points"], dtype=float)
    forward = np.array(SPEC["forward_shift_xy"], dtype=float)
    noise = sigma * np.array(SPEC["normal_offsets"], dtype=float)
    moving = fixed + forward + noise
    if include_wrong_matches:
        moving[SPEC["outlier_indices"]] += np.array(SPEC["outlier_extra_xy"])
    return fixed, moving, noise


def translation_ransac(fixed, moving, threshold_px):
    """Try every one-pair translation hypothesis and count nearby votes.

    Ordinary RANSAC selects small subsets randomly. Here all 12 one-pair
    guesses are tried in visible order so a class can inspect every step.
    A pair votes if its distance after this guessed correction is at most
    threshold_px. First highest vote count wins; all ties are recorded.
    The final correction averages the winning group's suggested moves.
    """
    pair_moves = np.asarray(fixed) - np.asarray(moving)
    trials = []
    for index, candidate in enumerate(pair_moves):
        residuals = np.linalg.norm(moving + candidate - fixed, axis=1)
        accepted = residuals <= threshold_px
        trials.append({"pair_id": index + 1, "correction_x_px": float(candidate[0]),
                       "correction_y_px": float(candidate[1]),
                       "votes": int(accepted.sum()),
                       "voter_pair_ids": (np.flatnonzero(accepted)+1).tolist(),
                       "residuals_px": residuals.tolist()})
    maximum_votes = max(t["votes"] for t in trials)
    tied = [t for t in trials if t["votes"] == maximum_votes]
    winner = tied[0]
    accepted_indices = np.array(winner["voter_pair_ids"]) - 1
    final_correction = pair_moves[accepted_indices].mean(axis=0)
    # Compare with a simple baseline: average EVERY proposed movement.
    all_pairs_mean = pair_moves.mean(axis=0)
    unique_groups = {tuple(t["voter_pair_ids"]) for t in tied}
    return {"threshold_px": threshold_px, "trials": trials,
            "winner_pair_id": winner["pair_id"], "max_votes": maximum_votes,
            "winning_inlier_pair_ids": winner["voter_pair_ids"],
            "tied_best_pair_ids": [t["pair_id"] for t in tied],
            "distinct_best_consensus_groups": len(unique_groups),
            "refit_correction_xy_px": final_correction.tolist(),
            "all_pairs_mean_correction_xy_px": all_pairs_mean.tolist()}


def point_experiment():
    """Measure results on separate, clean points that never take part in voting."""
    fixed, moving, noise = point_data()
    result = translation_ransac(fixed, moving, SPEC["voting_threshold_px"])
    independent_fixed = np.array(SPEC["independent_points"], dtype=float)
    independent_moving = independent_fixed + np.array(SPEC["forward_shift_xy"])
    estimates = {"before": np.zeros(2),
                 "all_pairs_mean": np.array(result["all_pairs_mean_correction_xy_px"]),
                 "ransac_refit": np.array(result["refit_correction_xy_px"])}
    checks = {}
    for method, correction in estimates.items():
        # A straight-line distance is a ruler length in x/y pixel coordinates.
        errors = np.linalg.norm(independent_moving + correction - independent_fixed, axis=1)
        checks[method] = {"correction_xy_px": correction.tolist(),
                          "per_point_error_px": errors.tolist(),
                          "mean_independent_point_error_px": float(errors.mean())}
    result.update({"known_forward_xy_px": SPEC["forward_shift_xy"],
                   "true_correction_xy_px": (-np.array(SPEC["forward_shift_xy"])).tolist(),
                   "fixed_points": fixed.tolist(), "observed_moving_points": moving.tolist(),
                   "known_wrong_pair_ids": [i+1 for i in SPEC["outlier_indices"]],
                   "independent_fixed_points": independent_fixed.tolist(),
                   "independent_moving_points": independent_moving.tolist(),
                   "independent_checks": checks})
    noise_rows = [{"pair_id": i+1, "x_error_px": float(v[0]), "y_error_px": float(v[1]),
                   "distance_px": float(np.linalg.norm(v)),
                   "known_wrong_match": i in SPEC["outlier_indices"]}
                  for i, v in enumerate(noise)]
    sigma_rows = []
    for sigma in [0.0, 0.4, 0.8, 1.6]:
        scaled = sigma * np.array(SPEC["normal_offsets"])
        sigma_rows.append({"sigma_px": sigma,
                           "observed_mean_distance_px": float(np.linalg.norm(scaled, axis=1).mean()),
                           "largest_observed_distance_px": float(np.linalg.norm(scaled, axis=1).max())})
    thresholds = []
    for threshold in [0.2, 0.5, 1.0, 2.0, 4.0, 40.0]:
        trial = translation_ransac(fixed, moving, threshold)
        correction = np.array(trial["refit_correction_xy_px"])
        error = np.linalg.norm(independent_moving + correction - independent_fixed, axis=1).mean()
        thresholds.append({"threshold_px": threshold, "votes": trial["max_votes"],
                           "mean_independent_point_error_px": float(error)})
    result["threshold_sweep"] = thresholds
    return {"sigma_px": SPEC["sigma_px"], "rows": noise_rows,
            "sigma_sweep": sigma_rows,
            "definition": "Standard deviation of each x/y click-error coordinate in pixels; not a maximum or wrong-match percentage."}, result


def save_figure(fig, name, caption):
    """Give every figure a plain-language footer and save a readable PNG."""
    fig.text(0.02, 0.015, caption, fontsize=10, va="bottom", wrap=True)
    fig.tight_layout(rect=(0, 0.10, 1, 0.98))
    fig.savefig(FIGURES / name, facecolor="white", bbox_inches="tight")
    plt.close(fig)
    return "figures/" + name


def make_figures(toys, scan, noise, points):
    """Make experimental diagrams only; labels explain what every mark means."""
    paths = {}
    fig, ax = plt.subplots(figsize=(11, 4.8))
    ax.axis("off")
    rows = [[r[k] for k in ["pixel", "reference", "other", "difference", "squared_difference"]]
            for r in toys["mse"]["rows"]]
    table = ax.table(cellText=rows, colLabels=["Pixel address", "Reference", "Other", "Subtract", "Square"],
                     loc="center", cellLoc="center")
    table.auto_set_font_size(False)
    table.set_fontsize(13)
    table.scale(1, 2.0)
    ax.set_title("Slides 9-10 | MSE: four small comparisons, then one average", pad=20)
    paths["mse_steps"] = save_figure(fig, "fig01_mse_steps.png",
        "Add the last column: 1 + 0 + 0 + 1 = 2. Divide by 4 compared pixels: MSE = 0.5 squared brightness units. Lower means closer numbers.")

    # Explain NCC with numbered pairs before teaching graph axes later in the lesson.
    fig, axes = plt.subplots(2, 2, figsize=(11, 6.5))
    meanings = {"brighter":"Same up/down pattern; +2 brightness does not change it.",
                "reversed":"Opposite pattern: one rises as the other falls.",
                "zero":"No linear pattern in these four compared pairs.",
                "flat":"Cannot calculate: the other row has no variation."}
    for ax, name in zip(axes.flat, ["brighter", "reversed", "zero", "flat"]):
        ax.axis("off")
        score = toys["ncc"][name]["value"]
        display_score = "undefined" if score is None else f"{score:+.3f}"
        ax.set_title(name.title() + " | Signed NCC: " + display_score, fontsize=14, pad=4)
        table = ax.table(cellText=[SPEC["ncc_reference"], SPEC["ncc_"+name]],
                         rowLabels=["Reference", "Other"], colLabels=["Pair 1","Pair 2","Pair 3","Pair 4"],
                         cellLoc="center", bbox=[0.20,0.30,0.78,0.52])
        table.auto_set_font_size(False)
        table.set_fontsize(13)
        for column in range(4):
            table[(1,column)].get_text().set_color(BLUE)
            table[(2,column)].get_text().set_color(ORANGE)
        ax.text(0.5,0.10,meanings[name],ha="center",va="center",transform=ax.transAxes,fontsize=11,wrap=True)
    paths["ncc_patterns"] = save_figure(fig, "fig02_ncc_patterns.png",
        "Slides 12-13 | Each column is one compared pair of brightness numbers. Read across the two rows. +1=same centered pattern; -1=opposite; 0=no linear pattern. Undefined is not zero.")

    fig, axes = plt.subplots(1, 3, figsize=(11, 4.7))
    for ax, name in zip(axes, ["same", "reversed", "independent"]):
        counts = np.array(toys["mi"][name]["counts"])
        ax.imshow(counts, cmap="Blues", vmin=0, vmax=2)
        for row in range(2):
            for col in range(2):
                ax.text(col, row, str(counts[row, col]), ha="center", va="center", fontsize=24,
                        color="white" if counts[row,col] == 2 else "black")
        ax.set(xticks=[0, 1], yticks=[0, 1], xlabel="Other value", ylabel="Reference value")
        case_title = "No clue" if name == "independent" else name.title()
        ax.set_title(f"{case_title}\nMI = {toys['mi'][name]['nats']:.3f} nats")
    paths["mi_counts"] = save_figure(fig, "fig03_mi_counts.png",
        "Slides 14-15 | Each cell counts pixel pairs, not brightness. Same and reversed both give a perfect clue here. 0.693 = ln(2) for THIS balanced two-value example; it is not a universal MI maximum.")

    fixed = np.array(scan["fixed_row"])
    moving = np.array(scan["moving_row"])
    roi = np.arange(9, 90)
    fig, axes = plt.subplots(3, 1, figsize=(11, 4.5))
    for ax, correction in zip(axes, [0, -1, -3]):
        pair = np.vstack([fixed[roi], moving[roi-correction]])
        ax.imshow(pair, cmap="gray", vmin=0, vmax=1, aspect="auto", extent=[8.5,89.5,1.5,-0.5])
        ax.set(yticks=[0, 1], yticklabels=["Reference", "Movable"], xlabel="Reference pixel x address")
        ax.set_title(f"Correction {correction:+d} px | MSE = {mse(pair[0],pair[1]):.3f}", loc="left")
    paths["image_positions"] = save_figure(fig, "fig04_image_positions.png",
        "Slides 18-20 | White=1, black=0. Every row compares the same 81 real pixels x=9..89. At -3 px the two rows agree. No padded border is included.")

    # First introduce just ONE graph; three side-by-side graphs come afterwards.
    fig, ax = plt.subplots(figsize=(11, 6.0))
    same_rows = [r for r in scan["scores"] if r["scenario"] == "same_brightness"]
    xs = [r["correction_x_px"] for r in same_rows]
    ys = [r["mse"] for r in same_rows]
    ax.plot(xs, ys, "o-", color=BLUE, linewidth=2, markersize=7)
    zero_score = next(r["mse"] for r in same_rows if r["correction_x_px"] == 0)
    ax.scatter([0], [zero_score], s=150, facecolors="none", edgecolors=ORANGE, linewidth=3, zorder=5)
    ax.axvline(-3, color=GREEN, linestyle="--")
    ax.annotate(f"One dot: tried 0 px\nmeasured MSE = {zero_score:.3f}", xy=(0,zero_score),
                xytext=(1.2,0.23), arrowprops={"arrowstyle":"->", "color":ORANGE}, fontsize=13,
                bbox={"facecolor":"white", "edgecolor":ORANGE, "boxstyle":"round,pad=.4"})
    ax.annotate("Lowest dot at -3 px\nMatches the known correction", xy=(-3,0),
                xytext=(-5.8,0.12), arrowprops={"arrowstyle":"->", "color":GREEN}, fontsize=13,
                bbox={"facecolor":"white", "edgecolor":GREEN, "boxstyle":"round,pad=.4"})
    ax.set(xlabel="Across = tried correction (px); negative means LEFT, positive means RIGHT",
           ylabel="Up = MSE (squared brightness units)", title="Slides 17-18 | Read one graph, one dot at a time",
           xticks=range(-6,7), ylim=(-0.02,0.7))
    ax.grid(alpha=0.18)
    paths["one_mse_graph"] = save_figure(fig,"fig05a_one_mse_graph.png",
        "Every dot is one recorded answer from the same 81 pixels. The line joins dots to guide the eye; intermediate positions were not measured. Green dashed line is known truth. A lower MSE is preferred here.")

    for scenario, key, filename in [("same_brightness", "score_graphs", "fig05_score_graphs.png"),
                                     ("reversed_brightness", "inversion_graphs", "fig06_inversion_graphs.png")]:
        fig, axes = plt.subplots(1, 3, figsize=(12, 4.6))
        rows = [r for r in scan["scores"] if r["scenario"] == scenario]
        for ax, metric, label, direction, metric_name in zip(axes,
                ["mse", "signed_ncc", "mi_nats"],
                ["MSE (squared brightness units)", "Signed NCC (no unit)", "MI (nats)"],
                ["smaller", "larger", "larger"], ["MSE", "signed NCC", "MI"]):
            xs = [r["correction_x_px"] for r in rows]
            ys = [r[metric] for r in rows]
            ax.plot(xs, ys, "o-", color=BLUE, label="One dot = one tested move")
            ax.axvline(-3, color=GREEN, linestyle="--", label="Known answer: -3 px")
            ax.set(xlabel="Correction x (px): negative = left", ylabel=label,
                   title=f"Choose {direction} {metric_name}", xticks=[-6,-3,0,3,6])
            ax.grid(alpha=0.18)
        axes[0].legend(fontsize=8, loc="upper right")
        fig.suptitle("Slides 17-19 | " + ("Same brightness: three scores find -3 px" if scenario == "same_brightness" else
                      "Brightness reversal: MSE and signed NCC choose the wrong move"), y=1.01)
        paths[key] = save_figure(fig, filename,
            "Horizontal axis: tried movement. Vertical axis: calculated score. Joining lines guide the eye; only dots were tested. Dashed line is the planted answer, not an estimate. " +
            ("The lowest MSE / highest NCC / highest MI is at -3 px." if scenario == "same_brightness" else
             "At the correct move NCC=-1 and MSE=1 because dark and bright swap. MI still peaks at -3 px: the values predict one another."))

    fig, axes = plt.subplots(1, 3, figsize=(11, 4.5))
    offsets = np.array(SPEC["normal_offsets"])
    for ax, sigma in zip(axes, [0.0, 0.8, 1.6]):
        errors = sigma * offsets
        ax.scatter(errors[:,0], errors[:,1], color=BLUE, s=36, label="12 simulated clicks")
        ax.scatter([0], [0], marker="+", s=170, color=RED, label="Exact location")
        # A circle is just a one-pixel ruler, not a probability boundary.
        ax.add_patch(plt.Circle((0,0), 1, fill=False, color="gray", linestyle=":"))
        ax.set(xlim=(-3,3), ylim=(6,-3), aspect="equal", xlabel="x click error (px)",
               ylabel="y click error (px), down is +", title=f"Sigma = {sigma:.1f} px per coordinate")
        ax.grid(alpha=0.2)
    axes[0].legend(fontsize=8, loc="lower right")
    paths["click_noise"] = save_figure(fig, "fig07_click_noise.png",
        "Slides 22-24 | The same 12 frozen normal draws are scaled. Dotted circle is a 1-pixel ruler. Sigma controls expected x/y spread, not a maximum: some errors exceed sigma. No wrong matches are shown in this figure.")

    fig, ax = plt.subplots(figsize=(11, 4.7))
    trials = points["trials"]
    colors = [RED if t["pair_id"] in points["known_wrong_pair_ids"] else BLUE for t in trials]
    ax.bar([t["pair_id"] for t in trials], [t["votes"] for t in trials], color=colors)
    for trial in trials:
        ax.text(trial["pair_id"], trial["votes"]+0.12, str(trial["votes"]), ha="center")
    ax.set(xlabel="Pair used to suggest a correction (ID)", ylabel="Number of votes out of 12",
           title="Slides 25-27 | Try one suggested move; count pairs within 2 px", xticks=range(1,13), ylim=(0,10))
    paths["ransac_votes"] = save_figure(fig, "fig08_ransac_votes.png",
        "Each bar is a different guessed translation. Blue=known genuine pair; red=known wrong pair in this synthetic example. Pair 1 wins the first 8-vote tie. Genuine pair 11 is rejected because its click error is unusually large.")

    fig, axes = plt.subplots(1, 3, figsize=(12, 5.3))
    truth = np.array(points["independent_fixed_points"])
    start = np.array(points["independent_moving_points"])
    for ax, method, label in zip(axes, ["before", "all_pairs_mean", "ransac_refit"],
                                ["Before correction", "Average all 12 pairs", "RANSAC + average its 8 voters"]):
        check = points["independent_checks"][method]
        corrected = start + np.array(check["correction_xy_px"])
        for target, observed in zip(truth, corrected):
            ax.plot([target[0],observed[0]], [target[1],observed[1]], color=RED, linewidth=2)
        ax.scatter(truth[:,0],truth[:,1],s=90,facecolors="none",edgecolors=BLUE,label="Exact target")
        ax.scatter(corrected[:,0],corrected[:,1],s=20,color=ORANGE,label="Corrected point")
        ax.set(xlim=(13,63),ylim=(52,10),aspect="equal", xlabel="x address (px), right is +", ylabel="y address (px), down is +",
               title=f"{label}\nMean ruler distance: {check['mean_independent_point_error_px']:.3f} px")
        ax.grid(alpha=0.15)
    axes[0].legend(fontsize=8,loc="lower right")
    paths["ransac_alignment"] = save_figure(fig, "fig09_ransac_alignment.png",
        "Slide 28 | These SIX points never voted or fitted. Red segments are leftover distances. Clean test points isolate correction error; they are not new noisy clicks. Translation makes every leftover distance equal here.")

    fig, ax = plt.subplots(figsize=(11, 5.3))
    ax.axis("off")
    cells = []
    for method, name in [("before","Before"),("all_pairs_mean","Average all pairs"),("ransac_refit","RANSAC + refit")]:
        item = points["independent_checks"][method]
        cells.append([name, f"({item['correction_xy_px'][0]:+.3f}, {item['correction_xy_px'][1]:+.3f})",
                      f"{item['mean_independent_point_error_px']:.3f} px"])
    table = ax.table(cellText=cells,colLabels=["Method","Estimated correction (x, y) px","Independent-point mean error"],
                     cellLoc="center",loc="center",colWidths=[0.25,0.36,0.39])
    table.auto_set_font_size(False)
    table.set_fontsize(12)
    table.scale(1,2.1)
    ax.set_title("Slide 29 | A saved answer table, with units and a ruler check",pad=20)
    paths["result_table"] = save_figure(fig,"fig10_result_table.png",
        "Known correction=(-6,+4) px. Smaller independent-point error is closer to truth in THIS synthetic test. A useful result depends on image scale and the job; 0.175 px is not a universal pass mark.")
    return paths


def write_csv(path, rows):
    """Save ordinary tables so values can be inspected without Python."""
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def meaningful_checks(data):
    """Check known arithmetic and model answers, not just whether files exist."""
    assert data["toy_metrics"]["mse"]["value"] == 0.5
    ncc = data["toy_metrics"]["ncc"]
    assert abs(ncc["brighter"]["value"]-1) < 1e-12
    assert abs(ncc["reversed"]["value"]+1) < 1e-12
    assert abs(ncc["zero"]["value"]) < 1e-12
    assert ncc["flat"]["value"] is None
    mi = data["toy_metrics"]["mi"]
    assert abs(mi["same"]["nats"] - math.log(2)) < 1e-12
    assert abs(mi["reversed"]["nats"] - math.log(2)) < 1e-12
    assert abs(mi["independent"]["nats"]) < 1e-12
    scan = data["image_scan"]
    assert all(scan["best_corrections"]["same_brightness"][key] == [-3] for key in ["mse","signed_ncc","mi_nats"])
    assert scan["best_corrections"]["reversed_brightness"]["mi_nats"] == [-3]
    assert -3 not in scan["best_corrections"]["reversed_brightness"]["signed_ncc"]
    # Check all sample addresses are observed content after the planted shift.
    for correction in SPEC["image_search_corrections"]:
        sampled_addresses = np.arange(9,90) - correction
        assert sampled_addresses.min() >= 3 and sampled_addresses.max() < 96
    points = data["ransac"]
    assert points["max_votes"] == 8
    assert points["distinct_best_consensus_groups"] == 2
    assert points["independent_checks"]["ransac_refit"]["mean_independent_point_error_px"] < 0.2
    assert points["independent_checks"]["all_pairs_mean"]["mean_independent_point_error_px"] > 3
    # With exact clicks and no wrong matches the known correction is recovered.
    fixed, moving, _ = point_data(sigma_px=0, include_wrong_matches=False)
    exact = translation_ransac(fixed,moving,0.001)
    assert np.allclose(exact["refit_correction_xy_px"],[-6,4])
    return {"status":"passed", "checks":18,
            "scope":"Known arithmetic; undefined NCC; MI tables; known-shift maxima/minima; fixed valid ROI; RANSAC votes, independent error and exact no-noise recovery."}


def run_all():
    toys = toy_metrics()
    scan = image_scan()
    noise, points = point_experiment()
    paths = make_figures(toys, scan, noise, points)
    data = {"schema_version":1,"synthetic_examples_only":True,"seed":SPEC["seed"],
            "toy_metrics":toys,"image_scan":scan,"noise":noise,"ransac":points,"figures":paths}
    data["validation"] = meaningful_checks(data)
    # allow_nan=False prevents accidental invalid JSON such as NaN or Infinity.
    (RESULTS/"lesson_results.json").write_text(json.dumps(data,indent=2,allow_nan=False),encoding="utf-8")
    write_csv(RESULTS/"image_shift_scores.csv",scan["scores"])
    write_csv(RESULTS/"mse_worked_steps.csv",toys["mse"]["rows"])
    write_csv(RESULTS/"point_click_noise.csv",noise["rows"])
    write_csv(RESULTS/"ransac_trials.csv",[{k:v for k,v in r.items() if k!="residuals_px"} for r in points["trials"]])
    write_csv(RESULTS/"threshold_sweep.csv",points["threshold_sweep"])
    summary = [{"method":method, "correction_x_px":values["correction_xy_px"][0],
                "correction_y_px":values["correction_xy_px"][1],
                "independent_mean_error_px":values["mean_independent_point_error_px"]}
               for method,values in points["independent_checks"].items()]
    write_csv(RESULTS/"independent_point_results.csv",summary)
    return data


if __name__ == "__main__":
    answers = run_all()
    print("Saved 11 annotated figures, six CSV tables, and results/lesson_results.json.")
    print("Known-answer validation:", answers["validation"]["status"])
    for method, item in answers["ransac"]["independent_checks"].items():
        print(f"{method}: {item['mean_independent_point_error_px']:.6f} px independent error")
