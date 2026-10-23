# What each number means

**Mark Lester O. Dampios — PhDCS103 — Image Registration, Parts I–VI**

This guide explains the measurements in the chronological presentation and single browser lesson. The researcher uses small arithmetic examples, controlled transformations with known answers, and recorded CPU experiments. The authoritative worked values are in [measurement_lessons.json](content/measurement_lessons.json). The [executed notebook](notebooks/01_chronological_experiments.ipynb) and its [offline reading copy](notebooks/01_chronological_experiments.html) repeat the calculations beside the current slide numbers.

## Start with two different questions

1. **Do these picture values have a useful relationship?** MSE, signed NCC, MI and NMI answer different versions of this question. These are image similarity scores.
2. **Did the method put the locations in the correct places?** A known-offset error or independent-point error checks positions against a known answer. These are geometric errors.

A high similarity score can occur at a wrong position in repeated stripes. A correct position can retain brightness differences between MRI contrasts. Always name the measurement before interpreting its number.

## Addresses, directions and units

A **pixel** is one square in the image grid. Its address says **where**; its brightness says **how light or dark**.

- **(x,y)** lists horizontal first, vertical second. In these image plots, right and down are positive.
- **(y,x)** lists vertical first, horizontal second. R3 reports array shifts in this order.
- **px** means pixels. It is a picture-grid unit, not a percentage. A millimetre conversion requires physical pixel spacing that these teaching examples do not establish.
- **Known** means the researcher deliberately generated the movement and saved the answer.
- **Estimated** means the method selected an answer. A supplied estimate in a calculation toy is labelled explicitly.
- A **sampling offset** tells where to read from the moving image. A **content correction** tells where to move the visible content. For pure translation, their signs are opposite.

Example: content moved right 6 and up 4, written **(+6,−4)**. At fixed address (20,20), read moving address (26,16): sampling offset (+6,−4). To move that content back, apply correction **(−6,+4)**. Comparing an offset directly with its opposite-sign correction would create a meaningless error.

## The measurement names at a glance

| Name | It measures | Unit | How to read it |
|---|---|---|---|
| MSE | Average squared brightness difference | Squared brightness units | Smaller favours equal values; 0 means equal compared values. |
| Brightness RMSE | Square root of MSE | Brightness units | Smaller favours equal values; depends on brightness scale. |
| Signed NCC | Same-direction linear brightness pattern | No unit | +1 perfectly rises/falls together; −1 perfectly reverses; flat data are undefined. |
| MI | Information one brightness label supplies about the other | Nats with natural logs | Larger favours a more predictable relationship, including inversion. |
| Studholme-style NMI | Entropy-normalized information relationship | No unit; a ratio | Read with its formula, content and overlap. It is not a percentage. |
| Translation-component error | Distance between estimated and known translation vectors | Pixels | 0 is exact translation; it does not evaluate unmodelled rotation. |
| Known-offset error | Distance between chosen and known sampling offsets | Pixels | 0 is the known offset; it is separate from the similarity score. |
| Independent-point mean error | Average leftover position gap at unused known check points | Fixed-image pixels | 0 is exact at the checked points. State the point set and scale. |
| Point RMSE | Square root of average squared point distance | Fixed-image pixels | Weighs large point misses more than the arithmetic mean does. |
| Fit residual | Leftover gap on points used to fit or vote | Stated coordinate-grid pixels | Describes fit agreement; separate points are needed to check prediction. |
| Hamming distance | Number of disagreeing descriptor bits | Bit mismatches | Smaller means a more similar binary fingerprint, not a smaller position gap. |
| Match ratio | Best Hamming distance divided by second-best | No unit | A screening rule for ambiguous matches; not an accuracy percentage. |
| Keypoint/match/inlier count | Number surviving a named pipeline stage | Count | A large count alone does not establish correct geometry. |
| Sigma, σ | Spread of a specified noise distribution | Depends on what is perturbed | Read whether it describes point coordinates, brightness noise or image blur. |
| RANSAC threshold | Largest residual counted as agreement in that hypothesis test | Pixels of the stated coordinate grid | Wider collects more votes and may admit bad pairs. |
| Nominal search-grid spacing | Distance between choices offered by the search | Pixels | Finer choices do not guarantee equally fine accuracy. |

## MSE and brightness RMSE: four numbers

Compare first values **[0,1,2,3]** with second values **[1,1,2,2]**.

| Pair | First minus second | Squared gap |
|---|---:|---:|
| 1 | −1 | 1 |
| 2 | 0 | 0 |
| 3 | 0 | 0 |
| 4 | +1 | 1 |

The opposite signs must not cancel. Squaring keeps both misses positive.

**MSE = (1+0+0+1)/4 = 0.5 squared brightness units.**

**Brightness RMSE = sqrt(0.5) = 0.707107 brightness units.**

This toy uses brightness numbers 0–3. Dividing all values by 3 changes the RMSE to 0.235702 on a 0–1 scale. Thus an unexplained RMSE of “0.7” has no useful interpretation. MSE is useful when corresponding places should have similar brightness, such as repeated images with similar contrast. Different MRI contrasts can remain correctly positioned while having a nonzero brightness MSE.

## Signed NCC: rise and fall together

NCC first subtracts each row's mean. It then compares the resulting up/down patterns.

For **[0,1,2,3]**, mean = 1.5 and centered values = **[−1.5,−0.5,+0.5,+1.5]**. Their squared sum is 5.

- **[2,3,4,5]** has the same centered values. The paired-product sum is 5; the denominator is sqrt(5×5)=5. NCC = **+1**.
- **[3,2,1,0]** has the opposite centered values. The product sum is −5. NCC = **−1**.
- **[1,0,0,1]** centers to [0.5,−0.5,−0.5,0.5]. The paired products sum to 0. NCC = **0**: no linear relationship in these samples.
- A constant row centers to all zeros. The denominator is zero: NCC is **undefined**. It must not be presented as a successful perfect match.

Maximizing **signed** NCC seeks +1, so the correct inverted image at −1 can lose to a wrong position. Taking absolute NCC would be a different metric. NCC is useful when brightness changes approximately by a positive gain and offset.

## MI: count pairs, turn counts into probabilities, add clues

Use four compared addresses and two labels: **0 dark**, **1 bright**.

| Case | First labels | Second labels | Meaning |
|---|---|---|---|
| Same | 0,0,1,1 | 0,0,1,1 | First label predicts the same second label. |
| Reversed | 0,0,1,1 | 1,1,0,0 | First label predicts the opposite second label. |
| Independent | 0,0,1,1 | 0,1,0,1 | Each first label occurs with both second labels equally. |

Rows of the table below are first-image labels 0/1; columns are second-image labels 0/1.

| Case | Count table | Joint-probability table (divide by 4) |
|---|---|---|
| Same | [[2,0],[0,2]] | [[0.5,0],[0,0.5]] |
| Reversed | [[0,2],[2,0]] | [[0,0.5],[0.5,0]] |
| Independent | [[1,1],[1,1]] | [[0.25,0.25],[0.25,0.25]] |

Each separate image has dark twice and bright twice. Its single-image probabilities are 0.5 and 0.5. These row or column totals are called **marginals**. A **joint** probability counts a pair together.

For each nonzero joint cell, MI adds:

**joint probability × ln[joint probability / (first probability × second probability)].**

The same case has two occupied cells. Each contributes:

**0.5 × ln[0.5/(0.5×0.5)] = 0.5 × ln(2) = 0.346574 nats.**

**MI = 0.346574 + 0.346574 = 0.693147 nats.** Empty cells contribute zero.

The reversed case has the same contributions in the other corners, so MI is also 0.693147. In the independent case, each cell compares 0.25 with 0.5×0.5=0.25. Their ratio is 1; ln(1)=0; total MI is **0**.

**ln** means natural logarithm. Using it makes the information unit **nats**. MI 0.693 is not 69.3% accuracy. More labels, different brightness frequencies or different histogram bins change the score scale.

**Use case:** compare candidate positions of images whose intensities differ, including different MRI contrasts. At each candidate, count the paired brightness values and calculate MI. A search or optimizer chooses a position using those scores; MI alone does not return a shift. A larger score can still identify a wrong repeated structure, so the independent geometric check remains necessary.

## NMI: calculate the uncertainties, then divide

**Entropy** measures uncertainty in the counted labels. For every nonzero probability p, add **−p×ln(p)**. Two equally likely labels give:

**−0.5×ln(0.5) − 0.5×ln(0.5) = 0.693147 nats.**

**Joint entropy** does the same calculation on paired-label probabilities. The same and reversed cases have two probabilities of 0.5: joint entropy 0.693147. The independent case has four probabilities of 0.25: **4×[−0.25×ln(0.25)] = 1.386294 nats**.

The formula used here is **NMI = [H(first)+H(second)]/H(first,second)**.

| Case | H(first), nats | H(second), nats | H(joint), nats | NMI |
|---|---:|---:|---:|---:|
| Same | 0.693147 | 0.693147 | 0.693147 | 2 |
| Reversed | 0.693147 | 0.693147 | 0.693147 | 2 |
| Independent | 0.693147 | 0.693147 | 1.386294 | 1 |
| Both flat | 0 | 0 | 0 | Undefined: 0/0 |

NMI is a unitless **ratio**, not a percentage. NMI 2 does not mean 200% accuracy. These simple values describe label relationships in this toy, not an industry acceptance threshold.

**Use case:** NMI was proposed to reduce some sensitivity to changing overlap by normalizing with the observed image entropies. The recorded crop experiment changes both the sample count and the content being counted. It shows behaviour under those conditions; it does not guarantee the correct alignment or immunity to every crop. The four-pair calculation explains the formula; it does not reproduce a medical study.

## Translation-component error: the actual 0.5-pixel example

R3 reports **(y,x)**, vertical first. The known correction is **(−5.4,+3.7)** px; the 1-pixel-grid estimate is **(−5,+4)** px.

1. Vertical gap: −5 − (−5.4) = **+0.4 px**.
2. Horizontal gap: +4 − (+3.7) = **+0.3 px**.
3. Straight-line gap: **sqrt(0.4²+0.3²)=sqrt(0.25)=0.5 px**.

“Component” means the translation **part of the model**; this number combines both translation axes. It is a distance between the estimated and correct slides. With no rotation, exact translation means exact coordinate correction. When the separate R3 condition adds rotation, the same calculation checks only its translation part. A translation-only method cannot undo a turn, so that row's number is not full-transform geometric accuracy.

In the clean recorded example, the 0.1-pixel grid represents the correct shift exactly and the measured translation error is zero. Finer numerical spacing offers more choices; it does not guarantee equally fine accuracy in noisy or mismodelled images.

## Known-offset error: the actual 14.56-pixel mistake

R4's known sampling offset is **(x,y)=(+6,−4)**. The inverted-image MSE search chose **(+10,+10)**.

- x gap: 10−6 = **4 px**.
- y gap: 10−(−4) = **14 px**.
- Distance: **sqrt(4²+14²)=sqrt(212)=14.560220 px**.

At fixed address (20,20), the correct sample is moving (26,16); the wrong candidate samples (30,30). Their gap is the same (4,14). The similarity metric selected an answer using brightness; the known answer lets the researcher check the position separately. MI found the correct offset in this controlled test, but the test does not establish that MI always wins.

## Independent-point error: use a fresh ruler

A point that helped fit the answer can make the fit look better than its predictions elsewhere. Independent points did not fit or vote. In controlled data, their exact moved addresses come from the known generator. Apply the estimated undo to those addresses and measure the leftover gaps to their fixed addresses.

This calculation toy supplies one estimate, **undo scale 0.55**. No fitted algorithm result is claimed. The known generation scale is 2; the true undo would be 0.50.

| Fixed (x,y) | Known moving (×2) | Estimated return (×0.55) | Leftover distance |
|---|---|---|---:|
| (10,0) | (20,0) | (11,0) | 1 fixed px |
| (20,0) | (40,0) | (22,0) | 2 fixed px |
| (30,0) | (60,0) | (33,0) | 3 fixed px |

**Mean distance = (1+2+3)/3 = 2 fixed px.** The average is 2; individual misses differ.

**Point RMSE = sqrt((1²+2²+3²)/3) = 2.160247 fixed px.** It is not the same averaging rule. It is also not brightness RMSE.

The real R1 spread/sigma0.5 example uses 25 check points. Its first point follows **(51.2,51.2) → (52.319105,55.140483) → (51.419863,51.214955)**. The final gap is approximately **(0.219863,0.014955)** fixed px, with length **0.220371** fixed px. Averaging all 25 saved lengths gives **0.211944** fixed px. The recorded R2 angle0/blur0 example gives **0.210645** fixed px on its own 25-point check. Their perturbations differ, so their small numerical difference is not evidence of an algorithm ranking.

These are synthetic known-coordinate recovery checks. They are not anatomical landmark errors measured in patients.

## Public MRI: what the experiment actually achieved

The source pair contains genuine public **T1-weighted and proton-density (PD) MRI contrasts**, with 221 columns and 257 rows. This is not CT/MRI, and it is not camera inversion. Its original physical spacing, independent anatomical truth and patient-level validation are not established here.

The researcher first finds each metric's best integer correction on the supplied pair. Each native optimum is **(x,y)=(0,0)**. Next, the researcher adds a content shift **(+9,−6)** to T1. Each best correction then becomes **(−9,+6)**.

**Change in optimum = (−9,+6)−(0,0) = (−9,+6).**

Compare with the known inverse of the added movement, (−9,+6). The leftover is (0,0): **0 px perturbation-recovery error**. Doing nothing to undo the added movement leaves magnitude **sqrt(9²+6²)=10.816654 px**.

MSE, signed NCC and MI **all** recovered the added shift in this pair. The search used integer corrections from −16 to +16 on both axes and the same 27,756 fixed PD foreground pixels inside a 27-pixel-margin ROI. ROI means the **region of interest** selected for comparison. Background fill was excluded.

Three small score comparisons were calculated with the original functions and exact original mask to explain the before/after values:

| State | MSE, squared normalized brightness | Signed NCC, unitless | MI, nats |
|---|---:|---:|---:|
| Original supplied pair | 0.127777 | 0.334569 | 0.752974 |
| Added shift, before correction | 0.157896 | 0.154482 | 0.078739 |
| Added shift, after correction | 0.127777 | 0.334569 | 0.752974 |

The corrected scores return to the native scores. Their brightness difference remains because they are different MRI contrasts. Thus **0 px added-shift recovery error and nonzero brightness MSE are compatible**.

**Achievement:** recovery of a deliberate integer displacement relative to the original supplied pair's metric optima. **Unknown:** perfect native anatomical alignment, millimetre error, performance on other patients or clinical suitability. Zero here does not turn those unknowns into facts.

## Counts, sigma and RANSAC

**ORB fingerprints:** the default WTA_K=2 descriptor has 32 bytes, or 256 yes/no bits. Hamming distance counts disagreeing bits. A distance of 28 is 28 disagreeing bits, not 28 pixels. In a nearest-match ratio example, best distance 20 divided by second-best distance 40 gives 0.5; a rule below 0.75 retains it. This means it is less ambiguous under that rule, not that it is 50% or 75% accurate.

**RANSAC:** try a tentative movement from a small selection of matches, count which pairs agree within a residual threshold, and retain a strong agreement group. Then refine the fit using that group. A bad correspondence links different physical places; a noisy good correspondence can also miss the threshold. A returned library voting mask and residuals after refinement can differ because refinement changes the estimate.

The small beginner translation example uses a 2-pixel threshold in its correction coordinates. The real ORB research pipeline uses 3 pixels for forward moving-coordinate residuals. Their thresholds are not interchangeable. A larger threshold can admit more wrong matches; more votes alone do not certify truth.

**Point-measurement sigma:** a sigma of 0.8 px describes the standard deviation of each simulated x/y coordinate error. It is not a maximum radial miss and does not mean 80% noise. A particular good pair may have a larger error. Wrong-match fraction is a different variable.

**Image-blur sigma:** a smoothing scale in pixels, used to blur the picture. **Brightness-noise sigma:** a spread in brightness units. These are different uses of the same Greek symbol. Always state what is being changed and its unit.

## Are the numbers good or bad?

Answer in this order: **quantity, unit, known answer, baseline, stated task tolerance, limitation**.

For example: “The mean unused-point error is 0.175 fixed pixels, compared with 7.211 pixels before correction, on this controlled translation example. It is below the declared 2-pixel classroom target. It does not establish clinical accuracy.”

There is no universal industry rule that makes every MSE, NCC, MI, NMI or pixel error good. Pixel size, task, scene, image contrast, overlap, transform family and required accuracy matter. A classroom target helps interpret this demonstration; an application needs its own justified tolerance and validation.

When reading a graph, name the **horizontal variable**, **vertical quantity and unit**, **one dot**, **which direction is preferred**, and **the known-answer mark**. A curve connecting recorded dots guides the eye; it does not create observations between them. A search-grid interval is not an accuracy interval.

## Evidence and source boundaries

The worked data were generated by [measurement_lessons.py](experiments/chronological/scripts/measurement_lessons.py), with source checksums and ten meaningful checks stored in the JSON. R1/R2 coordinate rows, R3/R4 results and MRI search optima were read from actual recorded CPU outputs. The three-point scale example is explicitly a calculation toy. Only three small MRI score samples were newly computed; no feature pipeline or search was rerun.

The information calculations are teaching examples. Research connections reuse Umeyama [13], ORB [14] with RANSAC [3], Guizar-Sicairos [5], Viola–Wells [7], Studholme [15] and the Rohlfing evaluation warning [9] under their documented method-level or illustrative boundaries. The public MRI pair comes from the [pinned ITK teaching-data source](https://github.com/InsightSoftwareConsortium/ITK/tree/50c5b33430e98b91b53fbaae2dd94f0edb2a639a/Examples/Data). Full numbered references appear in the chronological presentation and [references.json](content/references.json).
