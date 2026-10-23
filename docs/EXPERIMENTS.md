# Reproducing the experiments

Run commands from the repository root after [Python setup](SETUP.md). All images are bundled; the scripts have no runtime data-download step. CPU timings depend on the computer. Saved data include controlled perturbations of a few sources, not independent patients or scenes.

| Script | Purpose and saved output | Current presentation connection |
|---|---|---|
| `experiments/scripts/registration_lab.py` | Original public-photo feature/phase trials, contrast search, MRI added-shift test; outputs in `experiments/results/` and `experiments/figures/` | ORB, brightness registration, public MRI and evaluation |
| `experiments/beginner/scripts/teaching_lab.py` | Small MSE/NCC/MI counts, point noise and translation voting; outputs in the adjacent `results/` and `figures/` | Foundations and simple worked examples |
| `experiments/beginner/scripts/complete_lab.py` | Real ORB extraction, descriptors, residual thresholds and independent check points | Feature lessons and RMSE interpretation |
| `experiments/research/scripts/reproduce_studies.py` | R1–R6 method-level studies and counterexamples | Current primary result slides 18, 30, 47, 59, 70, 77 |
| `experiments/chronological/scripts/measurement_lessons.py` | Regenerates the worked distances, MI/NMI arithmetic, actual point checks and three small MRI score samples | Slides 16, 46, 54–55, 58, 61, 67–68, 73 |
| `experiments/chronological/scripts/replot_figures.py` | Replots recorded teaching data while removing obsolete slide-number captions; checks numerical plotting fingerprints | Current teaching figures |

```sh
python experiments/scripts/registration_lab.py --all
python experiments/beginner/scripts/teaching_lab.py
python experiments/beginner/scripts/complete_lab.py
python experiments/research/scripts/reproduce_studies.py
python experiments/chronological/scripts/measurement_lessons.py
python experiments/chronological/scripts/replot_figures.py
```

These commands regenerate files inside `experiments/`; full searches can take several minutes. The numerical scripts retain their original folder relationships. Old slide numbers inside source-script comments, result metadata or historical plots identify earlier source editions. Use [the current slide map](../content/SLIDE_DEMO_MAP.md) for the latest presentation. The six R studies reproduce selected ideas or illustrate limitations, rather than reproducing the papers' original patient datasets or benchmarks.

## Published evidence and fresh reruns

The published notebook uses `notebooks/evidence/recorded_results.json` and the current lesson plan. Its saved evidence remains unchanged when full scripts rerun. Likewise, the PowerPoint and single HTML embed saved figures and values; they do not update themselves from newly generated CSV files. This separation allows the researcher to compare a fresh run with the published evidence before deliberately updating teaching materials.

`content/measurement_lessons.json` is the published worked-data snapshot. A fresh measurement run writes the corresponding experiment copy to `experiments/chronological/content/measurement_lessons.json`. Library changes can alter feature counts, floating-point results and timings; inspect recorded versions, seeds and known-answer checks before comparing runs.
