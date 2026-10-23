# Chronological slide and demo map

Mark Lester O. Dampios

This map applies only to the chronological PowerPoint. Numbers include the optional hidden slides. The original decks retain their own numbering.

| Slide | Part | Route | Topic | Combined-demo lesson |
|---:|---|---|---|---|
| 1 | Start | main | Image registration, one step at a time | Discussion / reference |
| 2 | Start | main | The lesson follows six questions | Discussion / reference |
| 3 | I | main | Part I. What moves in a picture? | [purpose-I](../demo/index.html#purpose-I) |
| 4 | I | main | Pixels are tiny squares with numbers | [pixels](../demo/index.html#pixels) |
| 5 | I | extra | Each pixel has an address | [pixels](../demo/index.html#pixels) |
| 6 | I | extra | Brightness values: what 0–1 means | [brightness](../demo/index.html#brightness) |
| 7 | I | main | Reference picture and movable picture | [align](../demo/index.html#align) |
| 8 | I | main | Experiment: move the picture | [align](../demo/index.html#align) |
| 9 | I | extra | Turn, size, transparency, overlap and undo | [transform-extras](../demo/index.html#transform-extras) |
| 10 | I | extra | Resampling and valid overlap | [transform-extras](../demo/index.html#transform-extras) |
| 11 | I | extra | A ruler for leftover movement | Discussion / reference |
| 12 | I | extra | Matching dots are guesses | [point-pairs](../demo/index.html#point-pairs) |
| 13 | I | extra | Point measurement noise: imperfect clicks | [sigma](../demo/index.html#sigma) |
| 14 | I | main | Sigma controls spread | [sigma](../demo/index.html#sigma) |
| 15 | I | extra | A wrong match differs from a shaky click | [sigma](../demo/index.html#sigma) |
| 16 | I | main | Independent point error: a fresh checking dot | [check-dot-trace](../demo/index.html#check-dot-trace) |
| 17 | I | extra | Least squares and matching points | [R1](../demo/index.html#R1) |
| 18 | I | main | Point layout and independent recovery error | [R1](../demo/index.html#R1) |
| 19 | II | main | Part II. How can recognizable places help? | [purpose-II](../demo/index.html#purpose-II) |
| 20 | II | main | ORB: finding distinctive places | [orb](../demo/index.html#orb) |
| 21 | II | main | ORB descriptors: a yes/no fingerprint | [orb](../demo/index.html#orb) |
| 22 | II | extra | Matching: compare and reject ambiguity | [orb](../demo/index.html#orb) |
| 23 | II | extra | Real ORB experiment: read each stage | [orb](../demo/index.html#orb) |
| 24 | II | main | Residual: the gap left for one claimed pair | [residual](../demo/index.html#residual) |
| 25 | II | extra | The voting distance is a ruler setting | [residual](../demo/index.html#residual) |
| 26 | II | extra | Residual threshold: the voting ruler | [residual](../demo/index.html#residual) |
| 27 | II | main | RANSAC: suggest a move and collect votes | [ransac](../demo/index.html#ransac) |
| 28 | II | main | Experiment: RANSAC step by step | [ransac](../demo/index.html#ransac) |
| 29 | II | extra | ORB matching under rotation and blur | [R2](../demo/index.html#R2) |
| 30 | II | main | ORB results under turn and blur | [R2](../demo/index.html#R2) |
| 31 | III | main | Part III. How can brightness numbers help? | [purpose-III](../demo/index.html#purpose-III) |
| 32 | III | extra | A score is a rule for comparing | [mse](../demo/index.html#mse) |
| 33 | III | main | MSE: subtract, square and average | [mse](../demo/index.html#mse) |
| 34 | III | extra | MSE step 2: square, add, divide | [mse](../demo/index.html#mse) |
| 35 | III | extra | Why brighter can fool MSE | [mse](../demo/index.html#mse) |
| 36 | III | main | RMSE: finish by taking a square root | [rmse](../demo/index.html#rmse) |
| 37 | III | extra | Brightness error and position error | [rmse](../demo/index.html#rmse) |
| 38 | III | main | Signed NCC compares an up-and-down pattern | [ncc](../demo/index.html#ncc) |
| 39 | III | extra | The sign matters: +1, 0, and −1 | [ncc](../demo/index.html#ncc) |
| 40 | III | main | Sampling offset and correction have opposite signs | [offset](../demo/index.html#offset) |
| 41 | III | main | Graphs are maps of recorded answers | [graph](../demo/index.html#graph) |
| 42 | III | extra | One graph dot belongs to one picture position | [graph](../demo/index.html#graph) |
| 43 | III | extra | A score belongs to one tried position | [graph](../demo/index.html#graph) |
| 44 | III | extra | Read every original graph and number | [translation](../demo/index.html#translation) |
| 45 | III | extra | Subpixel translation and search precision | Discussion / reference |
| 46 | III | main | Translation-component error: the slide part only | [translation-error](../demo/index.html#translation-error) |
| 47 | III | main | Search spacing and recovery error | [R3](../demo/index.html#R3) |
| 48 | IV | main | Part IV. What if the shades change? | [purpose-IV](../demo/index.html#purpose-IV) |
| 49 | IV | extra | Same contrast: keep the brightness rule | [contrast-rules](../demo/index.html#contrast-rules) |
| 50 | IV | main | Inverted contrast: dark becomes bright | [contrast-rules](../demo/index.html#contrast-rules) |
| 51 | IV | main | Nonlinear inverted contrast: unequal changes | [contrast-rules](../demo/index.html#contrast-rules) |
| 52 | IV | extra | MI step 1: count pairs in a table | [mi](../demo/index.html#mi) |
| 53 | IV | extra | MI step 2: a useful clue | [mi](../demo/index.html#mi) |
| 54 | IV | main | MI calculation: turn four counts into fractions | [mi-calculation](../demo/index.html#mi-calculation) |
| 55 | IV | main | MI calculation: weight the clues, then add | [mi-calculation](../demo/index.html#mi-calculation) |
| 56 | IV | extra | Three rules, three questions | [mi](../demo/index.html#mi) |
| 57 | IV | extra | Mutual information and changed brightness | Discussion / reference |
| 58 | IV | main | Known-offset error: how far was the chosen answer off? | [known-offset-error](../demo/index.html#known-offset-error) |
| 59 | IV | main | Recovery after brightness inversion | [R4](../demo/index.html#R4) |
| 60 | IV | main | Public MRI contrast example | [mri-achievement](../demo/index.html#mri-achievement) |
| 61 | IV | main | What did the public MRI experiment achieve? | [mri-achievement](../demo/index.html#mri-achievement) |
| 62 | V | main | Part V. When should we doubt the evidence? | [purpose-V](../demo/index.html#purpose-V) |
| 63 | V | extra | Compare the same real picture area | Discussion / reference |
| 64 | V | extra | When the evidence is not enough | Discussion / reference |
| 65 | V | main | A useful order for solving the problem | Discussion / reference |
| 66 | V | extra | NMI adjusts an information score | Discussion / reference |
| 67 | V | main | NMI calculation starts with uncertainty | [nmi-calculation](../demo/index.html#nmi-calculation) |
| 68 | V | main | NMI: the same numbers, a different calculation | [nmi-calculation](../demo/index.html#nmi-calculation) |
| 69 | V | extra | Common image area and information scores | Discussion / reference |
| 70 | V | main | Information scores as the crop shrinks | [R5](../demo/index.html#R5) |
| 71 | VI | main | Part VI. How do we check the answer fairly? | [purpose-VI](../demo/index.html#purpose-VI) |
| 72 | VI | extra | Check with points that did not vote | [test](../demo/index.html#test) |
| 73 | VI | main | Independent point error: measure, then average | [independent-error](../demo/index.html#independent-error) |
| 74 | VI | extra | Read the saved result table | [original-results](../demo/index.html#original-results) |
| 75 | VI | main | Is a number good or bad? | [table](../demo/index.html#table) |
| 76 | VI | extra | Image agreement and position accuracy | [R6](../demo/index.html#R6) |
| 77 | VI | main | Equal image scores at different positions | [R6](../demo/index.html#R6) |
| 78 | VI | main | Explain the lesson in plain words | [review](../demo/index.html#review) |
| 79 | VI | extra | Everything on the original laboratory screen | [screen-map](../demo/index.html#screen-map) |
| 80 | VI | extra | A checklist for every unfamiliar label | [complete-review](../demo/index.html#complete-review) |
| 81 | VI | extra | What these experiments support | [complete-review](../demo/index.html#complete-review) |
| 82 | VI | main | Registration prepares pictures for fusion | Discussion / reference |
| 83 | References | extra | References | Discussion / reference |
| 84 | References | extra | References, continued | Discussion / reference |
| 85 | References | extra | References, continued | Discussion / reference |
| 86 | References | extra | References, continued | Discussion / reference |

## Activity order

Every earlier activity is available once in the combined navigation. Some companion activities share a slide topic. Related prerequisite slides are context rather than a request to reverse the route.

| Order | Part | Demo lesson | Route | Primary slides | Earlier source |
|---:|---|---|---|---|---|
| 1 | I | [What moves in a picture?](../demo/index.html#purpose-I) | main | 3 | New purpose introduction |
| 2 | I | [A tiny square has an address and a value](../demo/index.html#pixels) | main | 4, 5 | beginner / pixels |
| 3 | I | [What do brightness values 0–1 mean?](../demo/index.html#brightness) | extra | 6 | beginner / brightness |
| 4 | I | [Slide one little picture onto the other](../demo/index.html#align) | main | 7, 8 | beginner / align |
| 5 | I | [A slide, a turn, a size change and a display blend](../demo/index.html#transform-extras) | extra | 9, 10 | beginner / transform-extras |
| 6 | I | [Full picture: deliberately move it and undo it](../demo/index.html#transform) | extra | 9, 10 | original / transform |
| 7 | I | [Matching dots are claimed partners](../demo/index.html#point-pairs) | extra | 12 | beginner / points |
| 8 | I | [Wobbly clicks: what sigma means](../demo/index.html#sigma) | main | 13, 14, 15 | beginner / sigma |
| 9 | I | [A checking dot: known place, imperfect undo, leftover gap](../demo/index.html#check-dot-trace) | main | 16 | Worked measurement lesson |
| 10 | I | [Research R1: do spread-out measuring dots help?](../demo/index.html#R1) | main | 17, 18 | research / R1 |
| 11 | II | [How can recognizable places help?](../demo/index.html#purpose-II) | main | 19 | New purpose introduction |
| 12 | II | [ORB: places, fingerprints and proposed pairs](../demo/index.html#orb) | main | 20, 21, 22, 23 | beginner / orb |
| 13 | II | [Residual and threshold: a leftover gap and an allowed gap](../demo/index.html#residual) | main | 24, 25, 26 | beginner / original-residual |
| 14 | II | [RANSAC: suggest a move, then count agreement](../demo/index.html#ransac) | main | 27, 28 | beginner / ransac |
| 15 | II | [Full point-fitting laboratory](../demo/index.html#feature) | extra | 28 | original / feature |
| 16 | II | [Research R2: actual ORB under turning and blur](../demo/index.html#R2) | main | 29, 30 | research / R2 |
| 17 | III | [How can brightness numbers help?](../demo/index.html#purpose-III) | main | 31 | New purpose introduction |
| 18 | III | [MSE: average the squared brightness gaps](../demo/index.html#mse) | main | 32, 33, 34, 35 | beginner / mse |
| 19 | III | [RMSE: take the square root at the end](../demo/index.html#rmse) | main | 36, 37 | beginner / rmse |
| 20 | III | [Signed NCC: do values rise and fall together?](../demo/index.html#ncc) | main | 38, 39 | beginner / ncc |
| 21 | III | [Looking right and moving left have opposite signs](../demo/index.html#offset) | main | 40 | beginner / sampling-offset |
| 22 | III | [One graph dot is one tested position](../demo/index.html#graph) | main | 41, 42, 43 | beginner / graph |
| 23 | III | [Full image search: try a grid of offsets](../demo/index.html#translation) | main | 41, 43, 44 | original / translation |
| 24 | III | [Translation-component error: subtract two slide answers](../demo/index.html#translation-error) | main | 46 | Worked measurement lesson |
| 25 | III | [Research R3: finer steps do not promise a correct answer](../demo/index.html#R3) | main | 47 | research / R3 |
| 26 | IV | [What if the shades change?](../demo/index.html#purpose-IV) | main | 48 | New purpose introduction |
| 27 | IV | [Same, inverted and nonlinear inverted shades](../demo/index.html#contrast-rules) | main | 49, 50, 51 | beginner / contrast-rules |
| 28 | IV | [MI: count how useful one value is as a clue](../demo/index.html#mi) | extra | 52, 53, 56 | beginner / mi |
| 29 | IV | [Calculate MI from four paired labels](../demo/index.html#mi-calculation) | main | 54, 55 | Worked measurement lesson |
| 30 | IV | [Full image search after changing shades](../demo/index.html#contrast) | extra | 56 | original / contrast |
| 31 | IV | [Known-offset error: compare the chosen and correct offsets](../demo/index.html#known-offset-error) | main | 58 | Worked measurement lesson |
| 32 | IV | [Research R4: test MI after brightness inversion](../demo/index.html#R4) | main | 59 | research / R4 |
| 33 | IV | [What the real MRI contrast pair actually demonstrated](../demo/index.html#mri-achievement) | main | 60, 61 | Worked measurement lesson |
| 34 | V | [When should we doubt the evidence?](../demo/index.html#purpose-V) | main | 62 | New purpose introduction |
| 35 | V | [Calculate entropy and the chosen NMI ratio](../demo/index.html#nmi-calculation) | main | 67, 68 | Worked measurement lesson |
| 36 | V | [Research R5: shrinking the comparison area](../demo/index.html#R5) | main | 70 | research / R5 |
| 37 | VI | [How do we check the answer fairly?](../demo/index.html#purpose-VI) | main | 71 | New purpose introduction |
| 38 | VI | [Use check points that did not help fit](../demo/index.html#test) | extra | 72, 73 | beginner / test |
| 39 | VI | [Independent point error: three fresh dots and their average](../demo/index.html#independent-error) | main | 73 | Worked measurement lesson |
| 40 | VI | [Read every original graph and number](../demo/index.html#original-results) | extra | 74, 75 | beginner / original-results |
| 41 | VI | [A result table needs a unit and a comparison](../demo/index.html#table) | main | 75 | beginner / table |
| 42 | VI | [Research R6: perfect shades can hide the wrong place](../demo/index.html#R6) | main | 76, 77 | research / R6 |
| 43 | VI | [Explain the experiment without hiding behind abbreviations](../demo/index.html#review) | main | 78 | beginner / review |
| 44 | VI | [A guided map of the detailed laboratory](../demo/index.html#screen-map) | extra | 79 | beginner / complete-map |
| 45 | VI | [A checklist for any remaining unfamiliar label](../demo/index.html#complete-review) | extra | 80, 81 | beginner / complete-review |
