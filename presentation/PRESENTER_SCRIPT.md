# Chronological presenter script

Mark Lester O. Dampios

42 minutes of planned discussion and selected demonstrations, plus 3 minutes for switching and pauses. Optional detail is hidden during normal PowerPoint playback.

## Slide 1: Image registration, one step at a time

Chronological slide 1 of 86. Part Start. Main route. Planned 0.3 minutes including the selected demonstration.

Next main slide: 2. The lesson follows six questions.

Full discussion:
Image registration means finding a movement that lines up corresponding parts of two pictures. Imagine putting a tracing over a drawing until the same corners cover each other. The researcher will first explain the question in ordinary words, then show a small worked example, then demonstrate a controlled experiment. The known movement supplies an answer for checking. Public-image experiments, simulated examples and recorded Python results retain their labels. The presentation covers only Parts I–VI. Questions follow the forty-five-minute route.

Numbered sources:
[1] Richard Szeliski (2004). Image Alignment and Stitching: A Tutorial. https://www.microsoft.com/en-us/research/publication/image-alignment-and-stitching-a-tutorial/

## Slide 2: The lesson follows six questions

Chronological slide 2 of 86. Part Start. Main route. Planned 0.3 minutes including the selected demonstration.

Next main slide: 3. Part I. What moves in a picture?.

Full discussion:
Read each question as a reason for learning the next part. We begin with what can move, learn two ways to suggest a movement, consider changed shades, examine failure, then check the result. The normal slideshow follows the marked main route. Optional worked examples remain immediately beside the topic they explain and are hidden in the normal slideshow. The browser offers the same main route and an all-lessons route. Both use the actual slide numbers in this deck.

## Slide 3: Part I. What moves in a picture?

Chronological slide 3 of 86. Part I. Main route. Planned 0.3 minutes including the selected demonstration.

Purpose in ordinary words:
Learn what a picture stores, what can move, and how to measure a leftover gap.

Demonstration:
Read the question before touching any controls. Imagine the familiar example.

What to notice:
Put a tracing of a small drawing over the original drawing.

Interpretation:
The computer needs an address system, an allowed kind of movement, and a way to check its answer.

Matching combined-demo lesson: purpose-I. Open chronological/demo/index.html#purpose-I.

Next main slide: 4. Pixels are tiny squares with numbers.

Full discussion:
Begin with the familiar situation before naming the technical topic. Put a tracing of a small drawing over the original drawing. Learn what a picture stores, what can move, and how to measure a leftover gap. The computer needs an address system, an allowed kind of movement, and a way to check its answer. Explain that this is the purpose of foundations. Ask the audience to predict what useful evidence would look like. The following slides explain the unfamiliar labels before the experiment. At the end of the part, return to the question: Where should the movable picture go?

## Slide 4: Pixels are tiny squares with numbers

Chronological slide 4 of 86. Part I. Main route. Planned 0.94 minutes including the selected demonstration.

Purpose in ordinary words:
Tell the position of a square apart from its brightness.

Demonstration:
Read a column address, then read the value printed inside that square.

What to notice:
An address answers where. A value answers how light or dark.

Interpretation:
Registration changes the spatial relationship between addresses.

Matching combined-demo lesson: pixels. Open chronological/demo/index.html#pixels.

Next main slide: 7. Reference picture and movable picture.

Full discussion:
A pixel is one little square in a picture. Its address tells us where it is, using x across to the right and y down the page. Count from zero here. Its value tells us its shade. In the small grid, zero is darkest and three is brightest. The public photographs are scaled from zero to one instead. This is a brightness scale, not a distance scale. Read address (2,1) as the third column and second row, whose printed shade value is three. Registration changes how locations correspond. It does not make the brightness value into an address.

Expanded explanation and source context:
Point to one square, not the whole picture. Say: A digital picture is a grid of little squares called pixels. For a gray picture, each square stores a brightness number. In our first number example, zero is the darkest shade and three is the brightest shade. This small range makes the arithmetic easy.

A real image can use a different range, such as zero to 255, or normalized values from zero to one. Normalized here means rewritten on a chosen common scale. The MSE examples must state their number scale because squaring bigger numbers produces a different score.

Ask: If a square has number 3, does that mean it is located at position 3? Answer: No. Brightness is what the square looks like. Position is where the square lives. A pixel needs both an address and a value. Keep those two ideas separate throughout the lesson. The colored outlines in the demo are labels added for teaching; they are not extra brightness values in the underlying gray image.

## Slide 5: Each pixel has an address

Chronological slide 5 of 86. Part I. Optional detail. Hidden during the normal forty-five-minute slideshow. Use for preparation or questions.

Purpose in ordinary words:
Tell the position of a square apart from its brightness.

Demonstration:
Read a column address, then read the value printed inside that square.

What to notice:
An address answers where. A value answers how light or dark.

Interpretation:
Registration changes the spatial relationship between addresses.

Matching combined-demo lesson: pixels. Open chronological/demo/index.html#pixels.

Next main slide: 7. Reference picture and movable picture.

Full discussion:
Say: Think of the picture as a town of squares. Each square has an address. The x part counts across and the y part counts downward. We start at zero in the top-left corner. So address (2,1) means go two steps right and one step down from the top-left square.

Point to the labeled horizontal and vertical directions. This differs from some school graphs, where upward is positive. In these image coordinates, downward is positive y. A move of(+3,0) is three pixels right. A move of(0,-2) is two pixels up.

Ask: If a dark square becomes bright without changing its address, did it move? Answer: No. Its value changed, not its location. Later, this distinction will explain why brightness comparisons and position errors answer different questions.

In Python, array indexing usually writes row before column. That means image[y,x], although a point address is written (x,y). The scripts explain this beside the relevant line rather than expecting the learner to remember a hidden convention.

Source context:
[1] Image Alignment and Stitching: A Tutorial. https://www.microsoft.com/en-us/research/publication/image-alignment-and-stitching-a-tutorial/

Numbered sources:
[1] Richard Szeliski (2004). Image Alignment and Stitching: A Tutorial. https://www.microsoft.com/en-us/research/publication/image-alignment-and-stitching-a-tutorial/

## Slide 6: Brightness values: what 0–1 means

Chronological slide 6 of 86. Part I. Optional detail. Hidden during the normal forty-five-minute slideshow. Use for preparation or questions.

Purpose in ordinary words:
Learn the scale before using brightness scores.

Demonstration:
Move the brightness control and compare the printed number with its shade.

What to notice:
Zero is black. One is white. Middle values are gray.

Interpretation:
A normalized brightness value has no pixel-distance unit.

Matching combined-demo lesson: brightness. Open chronological/demo/index.html#brightness.

Next main slide: 7. Reference picture and movable picture.

Full discussion:
Say: The brightness number tells us how light or dark a gray pixel is. It is different from the x/y address telling us where the pixel is. In the original browser, brightness calculations use values from zero to one. Black is zero, white is one, and values between them are gray shades.

One common conversion divides an 8-bit gray value by 255. Thus zero becomes 0,255 becomes 1, and 128 becomes approximately 0.502. This rescaling is called normalization. It does not move a picture, improve its alignment, or turn a score into an accuracy probability.

The earlier four-value MSE arithmetic uses toy brightness numbers 0,1,2,3 so subtraction is easy. Its numeric scale differs from the original browser's 0–1 scale. Dividing all brightness numbers by 3 divides brightness RMSE by 3 and brightness MSE by 9. Always state the scale when comparing these scores.

Checkpoint: Does brightness 0.5 mean the point is half a pixel from its correct position? Answer: No. It means a gray value halfway along this chosen brightness scale.

## Slide 7: Reference picture and movable picture

Chronological slide 7 of 86. Part I. Main route. Planned 0.94 minutes including the selected demonstration.

Purpose in ordinary words:
See image registration as a movement with a known answer.

Demonstration:
Move the teal cross until it covers the purple cross. Try the known answer.

What to notice:
A generated shift of +3 pixels needs a correction of −3 pixels.

Interpretation:
A zero leftover gap means the checked positions coincide in this controlled example.

Matching combined-demo lesson: align. Open chronological/demo/index.html#align.

Next main slide: 8. Experiment: move the picture.

Full discussion:
Say: We choose one picture as the reference, like the sheet of paper lying on the desk. We move the other sheet until matching parts overlap. In registration papers, the reference is often called fixed, and the adjustable picture is called moving. Fixed describes its role; it does not mean the image is perfect.

Point to both labels in the browser. The green and magenta outlines help the audience distinguish the pictures even when they overlap. When corresponding outlines coincide, there is less double edging.

Ask: Which picture is changed during this demonstration? Answer: The moving picture. The researcher keeps the reference coordinate system unchanged. The software estimates a correction and resamples the moving picture into that system. Resampling means filling the output squares using the appropriate source locations. For this first lesson, integer moves avoid introducing interpolation arithmetic before position itself is understood.

Source context:
[1] Image Alignment and Stitching: A Tutorial. https://www.microsoft.com/en-us/research/publication/image-alignment-and-stitching-a-tutorial/

Numbered sources:
[1] Richard Szeliski (2004). Image Alignment and Stitching: A Tutorial. https://www.microsoft.com/en-us/research/publication/image-alignment-and-stitching-a-tutorial/

## Slide 8: Experiment: move the picture

Chronological slide 8 of 86. Part I. Main route. Planned 1.76 minutes including the selected demonstration.

Purpose in ordinary words:
See image registration as a movement with a known answer.

Demonstration:
Move the teal cross until it covers the purple cross. Try the known answer.

What to notice:
A generated shift of +3 pixels needs a correction of −3 pixels.

Interpretation:
A zero leftover gap means the checked positions coincide in this controlled example.

Matching combined-demo lesson: align. Open chronological/demo/index.html#align.

Next main slide: 14. Sigma controls spread.

Full discussion:
Purpose: the researcher first demonstrates a known movement so the audience can recognize what recovery means. Use the small cross lesson on the main route. The full photograph is an optional companion after the local control explanations. A generated move describes how the moving picture was made. A correction undoes that move. A horizontal +3 slide requires a −3 correction. A turn changes angle. A scale changes size with one multiplier. Transparency only blends the display. A known inverse button uses the supplied answer; it is not an estimated registration method. Resampling means looking up values to fill a new grid. Only valid shared content should enter score comparisons.

Expanded explanation and source context:
Open the browser lesson for the corresponding lessons in this part. Before touching a slider, say what it changes: the candidate correction is a move applied to the moving picture. Positive horizontal correction means right. Negative means left. The researcher created the example by moving the picture three pixels right, so the known correction is minus three pixels.

Ask the audience to predict the result of correction zero, then minus one, then minus three. Move to each position and point to the same corner. At minus three, the corresponding corner returns to its reference position. Do not introduce a score until the audience can explain this spatial change.

If rotation or resizing is mentioned, call them turning and making larger or smaller first. The core beginner experiment stays with sliding so one idea changes at a time. The original advanced package includes broader transformations. This lesson does not claim that sliding alone solves every registration problem.

Checkpoint: What move undoes three pixels right? Answer: Three pixels left, provided no other geometry changed.

Source context:
[1] Image Alignment and Stitching: A Tutorial. https://www.microsoft.com/en-us/research/publication/image-alignment-and-stitching-a-tutorial/

Numbered sources:
[1] Richard Szeliski (2004). Image Alignment and Stitching: A Tutorial. https://www.microsoft.com/en-us/research/publication/image-alignment-and-stitching-a-tutorial/

## Slide 9: Turn, size, transparency, overlap and undo

Chronological slide 9 of 86. Part I. Optional detail. Hidden during the normal forty-five-minute slideshow. Use for preparation or questions.

Purpose in ordinary words:
Learn what each transformation control changes.

Demonstration:
Change one control at a time. Undo the known move.

What to notice:
Transparency changes how the overlay is displayed. It does not repair position.

Interpretation:
Resampling fills a new grid, and valid overlap marks picture content shared by both images.

Matching combined-demo lesson: transform-extras. Open chronological/demo/index.html#transform-extras.

Next main slide: 14. Sigma controls spread.

Full discussion:
Read each original transformation control as a physical action. Horizontal and vertical translation slide the picture. Rotation turns it around the image center; the displayed positive direction is clockwise. Isotropic means equal in all directions: scale 1.05makes both width and height five percent larger. Scale 0.9makes them ten percent smaller.

Opacity is transparency in the overlay. Moving-image opacity 50 percent helps the audience see both layers. Changing that display weight does not change the stored source brightness data or the registration estimate. The overlay's colors are teaching aids, not a new imaging modality.

Identity means no geometric change. Inverse means a transformation that reverses another one. The known-inverse button uses the generating parameters already known to the researcher. Calling that an oracle simply means the answer is supplied for comparison; it is not an automatic discovery.

Resampling fills output pixels from source positions. Bilinear interpolation mixes nearby values for positions between pixel centers. Cropping can remove content. A valid mask marks available source data, and valid overlap is the part supported by both images. Position recovery can therefore be exact while brightness RMSE remains nonzero.

Angle convention: the original JavaScript screen displays a positive rotation clockwise. The actual OpenCV experiment uses getRotationMatrix2D, whose positive angle appears counterclockwise. Read the named convention before comparing signs; neither numeric sign alone defines a universal screen direction.

Source context:
[1] Image Alignment and Stitching: A Tutorial. https://www.microsoft.com/en-us/research/publication/image-alignment-and-stitching-a-tutorial/
[8] Registration Overview. https://simpleitk.readthedocs.io/en/latest/registrationOverview.html

Numbered sources:
[1] Richard Szeliski (2004). Image Alignment and Stitching: A Tutorial. https://www.microsoft.com/en-us/research/publication/image-alignment-and-stitching-a-tutorial/
[8] SimpleITK contributors (2026). Registration Overview. https://simpleitk.readthedocs.io/en/latest/registrationOverview.html

## Slide 10: Resampling and valid overlap

Chronological slide 10 of 86. Part I. Optional detail. Hidden during the normal forty-five-minute slideshow. Use for preparation or questions.

Purpose in ordinary words:
Learn what each transformation control changes.

Demonstration:
Change one control at a time. Undo the known move.

What to notice:
Transparency changes how the overlay is displayed. It does not repair position.

Interpretation:
Resampling fills a new grid, and valid overlap marks picture content shared by both images.

Matching combined-demo lesson: transform-extras. Open chronological/demo/index.html#transform-extras.

Next main slide: 14. Sigma controls spread.

Full discussion:
An estimated transformation changes coordinates. To create an aligned output image, the software must sample the moving image at the corresponding locations. Inverse sampling visits each output pixel and asks which source location supplies its value. Bilinear interpolation combines the four surrounding pixels when that source location is between pixel centers.

Resampling is not perfectly reversible. Rotation or scaling can smooth details, and content outside the field of view is lost. This explains why an oracle correction can have zero geometric point error while its pixel difference remains nonzero.

Padded borders are not observed anatomy or scene content. Including a large black border can change MSE, NCC, or MI for reasons unrelated to the structures under study. The notebooks create validity masks and compute intensity scores over explicitly defined support. The contrast-search experiment uses common support across candidate shifts, so changing overlap cannot win merely by hiding difficult pixels.

If asked why an image is not identical after undoing its transform, separate geometric reversibility from interpolation and cropping. For categorical masks, nearest-neighbor sampling is generally appropriate because interpolated category numbers have no semantic meaning.

Sources:
[1] Image Alignment and Stitching: A Tutorial. https://www.microsoft.com/en-us/research/publication/image-alignment-and-stitching-a-tutorial/
[8] Registration Overview. https://simpleitk.readthedocs.io/en/latest/registrationOverview.html

Numbered sources:
[1] Richard Szeliski (2004). Image Alignment and Stitching: A Tutorial. https://www.microsoft.com/en-us/research/publication/image-alignment-and-stitching-a-tutorial/
[8] SimpleITK contributors (2026). Registration Overview. https://simpleitk.readthedocs.io/en/latest/registrationOverview.html

## Slide 11: A ruler for leftover movement

Chronological slide 11 of 86. Part I. Optional detail. Hidden during the normal forty-five-minute slideshow. Use for preparation or questions.

Next main slide: 14. Sigma controls spread.

Full discussion:
Use the ruler before interpreting later tables. The leftover straight-line gap is a distance in pixels. A horizontal gap of three and vertical gap of four make a five-pixel straight-line distance. A mean distance adds the distances and divides by their count. It is not the same operation as averaging squared gaps and taking a root. Later experiments fit some measured pairs and check separate unused positions. Those unused positions did not help choose the movement. Known generated geometry makes their intended locations available.

Expanded explanation and source context:
Say: Suppose one corner should be at address (10,8), but after our correction it is at(12,8). Our little ruler reports two pixels of leftover distance. If it is at(13,12), the horizontal difference is three and the vertical difference is four. The straight-line distance is five pixels, like a 3-4-5 triangle.

The technical name is geometric point error. Geometric means about positions and shapes. It measures where a point ended up. It does not measure whether the two pixel brightness values are equal.

If several points are checked, the mean is the sum of their distances divided by their count. For distances 1,2,3, add to get 6, then divide by 3 to get 2 pixels. This is average distance. It is not an accuracy percentage.

Ask: Can the positions match while the pictures have different brightness? Answer: Yes. Position and appearance are separate. In these constructed examples, the researcher knows the correct positions. Real data may not provide that answer so easily.

Source context:
[9] Image Similarity and Tissue Overlaps as Surrogates for Image Registration Accuracy: Widely Used but Unreliable. https://pmc.ncbi.nlm.nih.gov/articles/PMC3274625/

Numbered sources:
[9] Torsten Rohlfing (2012). Image Similarity and Tissue Overlaps as Surrogates for Image Registration Accuracy: Widely Used but Unreliable. https://pmc.ncbi.nlm.nih.gov/articles/PMC3274625/

## Slide 12: Matching dots are guesses

Chronological slide 12 of 86. Part I. Optional detail. Hidden during the normal forty-five-minute slideshow. Use for preparation or questions.

Purpose in ordinary words:
Distinguish a believable pair from a deliberately wrong pair.

Demonstration:
Inspect which dot in one picture is claimed to match a dot in the other.

What to notice:
A wrong partner differs from clicking near the right partner.

Interpretation:
Fitting a movement requires evidence about corresponding places.

Matching combined-demo lesson: point-pairs. Open chronological/demo/index.html#point-pairs.

Next main slide: 14. Sigma controls spread.

Full discussion:
Say: Imagine placing a sticker on a corner in the reference picture and another sticker on what you think is the same corner in the moving picture. Those two stickers form a point pair. The displacement between them suggests how to move the picture.

In this lesson, the point pairs are deliberately generated so we can see good and bad examples. This is not an automatic corner detector. The original Notebook 02 uses actual ORB image features, which is a later step after this idea is understood.

If fixed is at(12,12) and its moving partner is at(18,8), the moving location is six right and four up. A correction of six left and four down brings it back. We write that correction as(-6,+4)pixels.

Ask: Must every suggested pair refer to the same real corner? Answer: No. An algorithm or a person can choose a wrong partner. The next lessons separate a slightly shaky location from a genuinely wrong correspondence.

## Slide 13: Point measurement noise: imperfect clicks

Chronological slide 13 of 86. Part I. Optional detail. Hidden during the normal forty-five-minute slideshow. Use for preparation or questions.

Purpose in ordinary words:
Understand point-measurement noise before the noisy-point experiment.

Demonstration:
Increase sigma and compare the spread of measured dots. Keep the wrong-match setting separate.

What to notice:
Sigma is a typical spread in each x/y coordinate, in pixels. It is not a maximum.

Interpretation:
Imprecise measurements can change an estimated movement even when all partner identities are correct.

Matching combined-demo lesson: sigma. Open chronological/demo/index.html#sigma.

Next main slide: 14. Sigma controls spread.

Full discussion:
Say: Imagine trying to click the center of the same tiny sticker several times. Your hand does not land at exactly the same pixel each time. The sticker itself has not wandered. Your recorded location is imperfect.

Point measurement noise means that uncertainty or jitter in the measured coordinates. In this lesson, x and y each receive a simulated random error. It is different from speckled image brightness and different from choosing an entirely wrong corner.

Point to the true marker and its measured marker. The connecting short segment shows one realized measurement error. The researcher knows the true location because this is a generated example. A real experiment would need a justified way to estimate localization uncertainty.

Ask: If the click is one pixel to the right of the true point, is that necessarily a wrong correspondence? Answer: No. It can be the right physical corner with an imperfect recorded position. A wrong correspondence refers to a different part. This distinction matters when interpreting the sigma and wrong-match controls.

## Slide 14: Sigma controls spread

Chronological slide 14 of 86. Part I. Main route. Planned 0.94 minutes including the selected demonstration.

Purpose in ordinary words:
Understand point-measurement noise before the noisy-point experiment.

Demonstration:
Increase sigma and compare the spread of measured dots. Keep the wrong-match setting separate.

What to notice:
Sigma is a typical spread in each x/y coordinate, in pixels. It is not a maximum.

Interpretation:
Imprecise measurements can change an estimated movement even when all partner identities are correct.

Matching combined-demo lesson: sigma. Open chronological/demo/index.html#sigma.

Next main slide: 16. Independent point error: a fresh checking dot.

Full discussion:
A point pair claims that one location corresponds to a location in the other picture. A shaky click can land near the right location. A wrong match chooses a different partner altogether. Point-measurement noise is the deliberately added wobble in measured coordinates. Sigma, written σ, describes a typical spread of the x errors and of the y errors separately. Sigma 0.5 means a half-pixel per-coordinate standard deviation in the stated construction. It does not promise that every point is within half a pixel. The fixed random offsets keep the slider comparison repeatable. This sigma differs from image-blur sigma and brightness-noise spread. Explain all three units locally before changing a control.

Expanded explanation and source context:
Introduce the symbol after the idea: sigma is the standard deviation of the simulated click error in each coordinate. Standard deviation is a way to describe spread. A sigma of two pixels means the x errors have that scale of spread and the y errors have that scale too. It does not mean every dot moves exactly two pixels.

The simulation uses a bell-shaped Gaussian random model. In that model, some coordinate errors can be farther away than sigma. The straight-line two-dimensional distance is also different from a single-coordinate error. Do not label sigma as the average radial distance, a maximum, or a percent.

Move the sigma slider while keeping the same frozen random directions and draws. This lets the audience see a cleaner change of spread without changing everything at once. Sigma zero removes this small click jitter, while deliberately wrong pairs remain wrong.

Ask: Can a three-pixel coordinate error happen with sigma one? Answer: Yes. Sigma describes the distribution's spread, not a hard fence. A small displayed sample will not have exactly the theoretical spread.

## Slide 15: A wrong match differs from a shaky click

Chronological slide 15 of 86. Part I. Optional detail. Hidden during the normal forty-five-minute slideshow. Use for preparation or questions.

Purpose in ordinary words:
Understand point-measurement noise before the noisy-point experiment.

Demonstration:
Increase sigma and compare the spread of measured dots. Keep the wrong-match setting separate.

What to notice:
Sigma is a typical spread in each x/y coordinate, in pixels. It is not a maximum.

Interpretation:
Imprecise measurements can change an estimated movement even when all partner identities are correct.

Matching combined-demo lesson: sigma. Open chronological/demo/index.html#sigma.

Next main slide: 16. Independent point error: a fresh checking dot.

Full discussion:
Return sigma to zero and keep the deliberately wrong matches visible. The correct generated pairs now agree exactly with the known move, but the wrong pairs still suggest different moves. This simple test prevents the learner from treating every bad result as one kind of noise.

Inlier is a technical label for a pair that agrees with a candidate model within the chosen tolerance. Outlier is a pair that does not agree with that candidate under that rule. The label depends on the model and threshold; it is not a magical declaration of anatomical truth.

A wrong match can be a gross error. A correct physical match with a large localization error may also fall outside the voting threshold. Therefore, the demo distinguishes construction truth from algorithm vote labels using separate legend entries.

Ask: If an algorithm colors a point green as an inlier, is it guaranteed correct? Answer: No. A set of wrong pairs can agree on a wrong move. Independent checking is still necessary.

## Slide 16: Independent point error: a fresh checking dot

Chronological slide 16 of 86. Part I. Main route. Planned 0.91 minutes including the selected demonstration.

Purpose in ordinary words:
See where an independent point error comes from before reading a result table.

Demonstration:
Follow the first dot from x=10 to x=20, then back with the supplied undo multiplier. Try the exact 0.50.

What to notice:
Using 0.55 returns it to x=11. Its correct place is x=10, so the error is 1 fixed pixel.

Interpretation:
The dot did not help choose the movement. It is a fresh position check, not a brightness score.

Matching combined-demo lesson: check-dot-trace. Open chronological/demo/index.html#check-dot-trace.

Next main slide: 18. Point layout and independent recovery error.

45-minute spoken route (one worked case; the longer discussion is for preparation):
This dot began at ten. Doubling put it at twenty. Our supplied undo returns it to eleven, so it is one pixel from home. The dot did not help choose the undo. That makes it a checking dot. Try the exact half-size undo and watch its error become zero.

Full discussion:
Purpose: make independent point error visible before the first research result table. A point is a location, such as a corner. The researcher knows that this checking dot began at x=10, y=0. The deliberately constructed forward movement doubles every coordinate, placing it at x=20. The exact undo would multiply by one half, 0.50. For this arithmetic example, the researcher supplies an imperfect undo multiplier of 0.55. It returns the dot to x=11, leaving a one-pixel horizontal gap to its correct x=10 place. The y coordinate remains zero. This is a controlled calculation, not a claim that an algorithm actually estimated 0.55.

Independent means this dot did not help fit or vote for the chosen movement. It is a fresh checking location. Its correct position is known from the construction. The final ruler uses fixed-picture pixels because the estimated undo returns points into the fixed picture. A fitting residual instead measures agreement between a prediction and a measured claimed partner and can use a different coordinate direction. Those checks answer different questions. A later lesson repeats the same recipe for three checking dots and averages the distances. Lower distance means closer to the known intended location under this ruler. Zero means this checked point returns exactly; it does not prove brightness values are identical or validate anatomy.

Numbered sources:
[1] Richard Szeliski (2004). Image Alignment and Stitching: A Tutorial. https://www.microsoft.com/en-us/research/publication/image-alignment-and-stitching-a-tutorial/
[9] Torsten Rohlfing (2012). Image Similarity and Tissue Overlaps as Surrogates for Image Registration Accuracy: Widely Used but Unreliable. https://pmc.ncbi.nlm.nih.gov/articles/PMC3274625/
[13] Shinji Umeyama (1991). Least-Squares Estimation of Transformation Parameters Between Two Point Patterns. https://doi.org/10.1109/34.88573

## Slide 17: Least squares and matching points

Chronological slide 17 of 86. Part I. Optional detail. Hidden during the normal forty-five-minute slideshow. Use for preparation or questions.

Purpose in ordinary words:
Test a least-squares point-fitting idea from Umeyama [13].

Demonstration:
Keep the same sigma. Compare dots spread across the picture with dots clustered in a patch.

What to notice:
The 16 fitting pairs help estimate the move. The 25 separate check points do not.

Interpretation:
A small fitting gap can coexist with a larger unused-point error. This is a bounded classroom adaptation.

Matching combined-demo lesson: R1. Open chronological/demo/index.html#R1.

Next main slide: 18. Point layout and independent recovery error.

Full discussion:
A landmark is a recognizable position supplied in both pictures. A correspondence is the claim that two positions show the same physical place. The researcher supplies sixteen correct correspondences and deliberately adds small position errors to the moving measurements. Least squares chooses the movement that makes the total of squared fitting gaps as small as possible. Squaring means multiplying a gap by itself, so larger gaps have more influence.

Umeyama's method estimates a rotation, translation, and scale from paired point patterns. The implementation here uses the established scikit-image similarity estimator. This is a two-dimensional method-level reproduction with correct pairs. It does not reproduce every experiment or higher-dimensional setting from the paper.

The class compares points distributed across the picture with sixteen points crowded near the center. The same fixed random offsets are used at the same per-coordinate noise setting, called sigma. The researcher checks twenty-five separate exact points across the image. Those points never help fit the answer. Their mean recovery distance uses the fixed-image pixel ruler. The fitting residual instead uses moving-image pixels.

The follow-up question concerns precision away from a small cluster. It does not claim that the paper or later literature failed to consider point geometry. The reproduced method assumes that the pairings are supplied correctly. Wrong pairs and deformation require additional handling. A nearly zero fitting residual alone does not establish a precise correction throughout an image.

Published study: Shinji Umeyama. Least-Squares Estimation of Transformation Parameters Between Two Point Patterns (1991).
Primary source: https://doi.org/10.1109/34.88573

What the paper contributes:
For paired point patterns and the stated rank conditions, a closed-form singular-value-decomposition solution minimizes squared correspondence error while enforcing a proper rotation rather than a reflection.

Evidence locations:
p. 377, Section I, Eq. (1): The least-squares objective uses paired points and a similarity transform.
p. 378, Section II, theorem and Eqs. (32)–(43): Centroids, covariance, scale, rotation and translation; rank/uniqueness condition.
pp. 379–380, Section III and Figs. 1–3; Section IV: Numerical example distinguishes a zero-error reflection from a constrained proper rotation.

Published limitation or scope boundary:
The theorem operates on given paired point patterns and states rank conditions for uniqueness. It solves the least-squares objective; it does not assert robust recovery of the true transform from arbitrary incorrect correspondences.
Evidence location: p. 378, theorem and rank condition; p. 380, Section IV

Classroom adaptation:
Use 16 known 2D correspondences under one known similarity transform. Compare spatially spread versus tightly clustered fitting layouts at localization-noise sigma 0, 0.5, and 2 pixels, reusing fixed normal draws. Fit the SVD solution and check 25 separate points. Also retain a coincident-point degeneracy failure.

What this experiment does not reproduce:
The complete original numerical analysis or comparison with every earlier method
Automatic discovery of point correspondences
Clinical or multi-scene image registration

Follow-up question for this class:
With the same coordinate-noise draws, does fitting widely spread points or tightly clustered points give the smaller error at independent points?

Supported conclusion:
Whether this implementation recovers the constructed similarity under the recorded point layout and perturbation settings.

Boundary on the conclusion:
That least squares rejects outliers, discovers correct correspondences, or generalizes to arbitrary image pairs.

The classroom question does not carry a claim of novel or currently unsolved research.

Numbered sources:
[13] Shinji Umeyama (1991). Least-Squares Estimation of Transformation Parameters Between Two Point Patterns. https://doi.org/10.1109/34.88573

## Slide 18: Point layout and independent recovery error

Chronological slide 18 of 86. Part I. Main route. Planned 1.32 minutes including the selected demonstration.

Purpose in ordinary words:
Test a least-squares point-fitting idea from Umeyama [13].

Demonstration:
Keep the same sigma. Compare dots spread across the picture with dots clustered in a patch.

What to notice:
The 16 fitting pairs help estimate the move. The 25 separate check points do not.

Interpretation:
A small fitting gap can coexist with a larger unused-point error. This is a bounded classroom adaptation.

Matching combined-demo lesson: R1. Open chronological/demo/index.html#R1.

Next main slide: 19. Part II. How can recognizable places help?.

Full discussion:
A coordinate can fall between pixel centers. Half a pixel means half of one grid step. The point-fitting model permits a slide, a turn and an even size change. The fitting pairs estimate that movement; the unused known positions check it.

Research connection [13], Umeyama (1991): estimate a shared turn, size and slide from supplied point pairs by least squares. Least squares chooses the movement that makes the sum of squared point gaps as small as possible. It uses point-coordinate distances, not image-brightness MSE. Here sixteen measured pairs fit the move, and twenty-five known positions that did not fit it check recovery. A residual means one gap left between a prediction and its claimed partner. The first result column averages such forward gaps in moving-image pixels. The second averages unused-point gaps after the estimated inverse in fixed-image pixels. Name both units before comparing rows. A cluster gives weaker information about the whole picture. This run uses no deliberately wrong identities. It is a bounded method adaptation, not the full original paper benchmark.

Expanded explanation and source context:
A landmark is a recognizable position supplied in both pictures. A correspondence is the claim that two positions show the same physical place. The researcher supplies sixteen correct correspondences and deliberately adds small position errors to the moving measurements. Least squares chooses the movement that makes the total of squared fitting gaps as small as possible. Squaring means multiplying a gap by itself, so larger gaps have more influence.

Umeyama's method estimates a rotation, translation, and scale from paired point patterns. The implementation here uses the established scikit-image similarity estimator. This is a two-dimensional method-level reproduction with correct pairs. It does not reproduce every experiment or higher-dimensional setting from the paper.

The class compares points distributed across the picture with sixteen points crowded near the center. The same fixed random offsets are used at the same per-coordinate noise setting, called sigma. The researcher checks twenty-five separate exact points across the image. Those points never help fit the answer. Their mean recovery distance uses the fixed-image pixel ruler. The fitting residual instead uses moving-image pixels.

The follow-up question concerns precision away from a small cluster. It does not claim that the paper or later literature failed to consider point geometry. The reproduced method assumes that the pairings are supplied correctly. Wrong pairs and deformation require additional handling. A nearly zero fitting residual alone does not establish a precise correction throughout an image.

Published study: Shinji Umeyama. Least-Squares Estimation of Transformation Parameters Between Two Point Patterns (1991).
Primary source: https://doi.org/10.1109/34.88573

What the paper contributes:
For paired point patterns and the stated rank conditions, a closed-form singular-value-decomposition solution minimizes squared correspondence error while enforcing a proper rotation rather than a reflection.

Evidence locations:
p. 377, Section I, Eq. (1): The least-squares objective uses paired points and a similarity transform.
p. 378, Section II, theorem and Eqs. (32)–(43): Centroids, covariance, scale, rotation and translation; rank/uniqueness condition.
pp. 379–380, Section III and Figs. 1–3; Section IV: Numerical example distinguishes a zero-error reflection from a constrained proper rotation.

Published limitation or scope boundary:
The theorem operates on given paired point patterns and states rank conditions for uniqueness. It solves the least-squares objective; it does not assert robust recovery of the true transform from arbitrary incorrect correspondences.
Evidence location: p. 378, theorem and rank condition; p. 380, Section IV

Classroom adaptation:
Use 16 known 2D correspondences under one known similarity transform. Compare spatially spread versus tightly clustered fitting layouts at localization-noise sigma 0, 0.5, and 2 pixels, reusing fixed normal draws. Fit the SVD solution and check 25 separate points. Also retain a coincident-point degeneracy failure.

What this experiment does not reproduce:
The complete original numerical analysis or comparison with every earlier method
Automatic discovery of point correspondences
Clinical or multi-scene image registration

Follow-up question for this class:
With the same coordinate-noise draws, does fitting widely spread points or tightly clustered points give the smaller error at independent points?

Supported conclusion:
Whether this implementation recovers the constructed similarity under the recorded point layout and perturbation settings.

Boundary on the conclusion:
That least squares rejects outliers, discovers correct correspondences, or generalizes to arbitrary image pairs.

The classroom question does not carry a claim of novel or currently unsolved research.

Purpose of this experiment:
Test whether equally small fitting residuals ensure accurate recovery away from a clustered fit region.

Recorded settings:
16 known correspondences; spread 192 x 192 px versus cluster 4 x 4 px; similarity fit; sigma 0, 0.5, 2 per moving coordinate.

Interpretation of the measured rows:
At the same sigma, fitting residuals are almost identical but clustered correspondences extrapolate poorly.

Limits of this classroom run:
New 2-D points, one draw, no wrong matches; no robustness or original numerical benchmark replication.

Read the condition first, name the measurement and its unit, and compare it with the known generated answer. Full raw measurements and figures are retained in the notebook and results files.

Numbered sources:
[13] Shinji Umeyama (1991). Least-Squares Estimation of Transformation Parameters Between Two Point Patterns. https://doi.org/10.1109/34.88573

## Slide 19: Part II. How can recognizable places help?

Chronological slide 19 of 86. Part II. Main route. Planned 0.3 minutes including the selected demonstration.

Purpose in ordinary words:
Find recognizable little places, pair them, and test which pairs agree on one movement.

Demonstration:
Read the question before touching any controls. Imagine the familiar example.

What to notice:
Match the same corners on two copies of a treasure map.

Interpretation:
A few useful places can guide alignment, but a similar-looking place can produce a wrong pair.

Matching combined-demo lesson: purpose-II. Open chronological/demo/index.html#purpose-II.

Next main slide: 20. ORB: finding distinctive places.

Full discussion:
Begin with the familiar situation before naming the technical topic. Match the same corners on two copies of a treasure map. Find recognizable little places, pair them, and test which pairs agree on one movement. A few useful places can guide alignment, but a similar-looking place can produce a wrong pair. Explain that this is the purpose of feature-based registration. Ask the audience to predict what useful evidence would look like. The following slides explain the unfamiliar labels before the experiment. At the end of the part, return to the question: Which claimed pairs belong to the same movement?

## Slide 20: ORB: finding distinctive places

Chronological slide 20 of 86. Part II. Main route. Planned 0.94 minutes including the selected demonstration.

Purpose in ordinary words:
Learn how actual ORB output supplies candidate point pairs.

Demonstration:
Follow detection, short yes/no fingerprints, descriptor comparisons and the ambiguity filter in order.

What to notice:
A descriptor is a pattern summary. Its bit disagreement count is not a distance in image pixels.

Interpretation:
ORB proposes pairs of distinctive local places; geometric checking still has to test their agreement.

Matching combined-demo lesson: orb. Open chronological/demo/index.html#orb.

Next main slide: 21. ORB descriptors: a yes/no fingerprint.

Full discussion:
ORB is a method that locates distinctive little image places and describes their nearby light/dark patterns. A feature here is a local place, not a named object such as a car. A corner can be easier to find again than a blank wall. A patch is a small neighborhood around the place. ORB estimates a local direction so that its pattern tests can turn with the image. It checks several image sizes as well. The next slide shows its yes/no pattern summary before any output count or matching threshold is interpreted.

Expanded explanation and source context:
ORB is a named computer-vision method: Oriented FAST and Rotated BRIEF. Explain its job before unpacking the acronym. It identifies potentially distinctive locations, called keypoints, and builds a short description of the local image around each location. A keypoint is not automatically a known anatomical landmark or a guaranteed correct match.

Imagine trying to recognize a place using a featureless wall versus a marked street corner. The corner's surrounding pattern gives more clues. ORB's detector looks for characteristic local brightness patterns; its description stage summarizes neighborhoods for comparison. It uses orientation (a local direction) and an image pyramid (copies of the picture at several sizes) to support matching across some turns and size changes. That support has limits and is not a guarantee for arbitrary views or modalities.

The new notebook actually runs OpenCV ORB on a bundled public photograph with a known introduced transform. The browser companion shows saved results of that real run. The original browser RANSAC panel instead generates point pairs; it does not run ORB. Keep those activities clearly separated.

Checkpoint: Does detecting two thousand keypoints mean two thousand correct matches? Answer: No. Detection and matching are separate stages.

Source context:
[2] ORB (Oriented FAST and Rotated BRIEF). https://docs.opencv.org/4.13.0/d1/d89/tutorial_py_orb.html
[4] Camera Calibration and 3D Reconstruction: estimateAffinePartial2D. https://docs.opencv.org/4.13.0/d9/d0c/group__calib3d.html
[10] skimage.data.camera. https://scikit-image.org/docs/stable/api/skimage.data#skimage.data.camera

Numbered sources:
[2] OpenCV contributors (2026). ORB (Oriented FAST and Rotated BRIEF). https://docs.opencv.org/4.13.0/d1/d89/tutorial_py_orb.html
[4] OpenCV contributors (2026). Camera Calibration and 3D Reconstruction: estimateAffinePartial2D. https://docs.opencv.org/4.13.0/d9/d0c/group__calib3d.html
[10] scikit-image contributors; image by Lav Varshney (2026). skimage.data.camera. https://scikit-image.org/docs/stable/api/skimage.data#skimage.data.camera

## Slide 21: ORB descriptors: a yes/no fingerprint

Chronological slide 21 of 86. Part II. Main route. Planned 0.94 minutes including the selected demonstration.

Purpose in ordinary words:
Learn how actual ORB output supplies candidate point pairs.

Demonstration:
Follow detection, short yes/no fingerprints, descriptor comparisons and the ambiguity filter in order.

What to notice:
A descriptor is a pattern summary. Its bit disagreement count is not a distance in image pixels.

Interpretation:
ORB proposes pairs of distinctive local places; geometric checking still has to test their agreement.

Matching combined-demo lesson: orb. Open chronological/demo/index.html#orb.

Next main slide: 24. Residual: the gap left for one claimed pair.

Full discussion:
A descriptor is a short fingerprint of the neighborhood around a detected place. Each brightness comparison produces a yes/no bit, stored as zero or one. The eight-test fingerprint is a toy. Actual ORB here stores 256 bits. Hamming distance counts disagreeing bits between two fingerprints. It is not a distance in pixels. To reduce ambiguity, compare the best descriptor match with the second best. The chosen ratio rule retains a best-to-runner-up distance ratio below 0.75. This is an experimental setting, not a universal quality threshold. The ratio rule proposes pairs; the geometric fit still needs to test whether the proposed partners agree on one movement.

Expanded explanation and source context:
A descriptor is a description made for comparing one keypoint neighborhood with another. ORB uses binary descriptions. Binary means two possible symbols, zero and one. A bit is one such symbol; eight bits make a byte. With the default two-way comparison setting used here, an ORB descriptor contains 32 bytes, or 256 bits.

A simplified teaching example compares two chosen brightness locations in a patch, meaning a small cutout around the point. Write one if the first is darker than the second and zero otherwise. Repeating comparisons produces a small pattern of bits. This illustrates a BRIEF-style binary description. The toy eight-comparison diagram is not a claim to reproduce OpenCV's exact trained 256-test layout.

The real notebook prints actual descriptor bytes and a bit excerpt from the executed ORB output. Think of this as a comparison fingerprint, not a unique identity document. Two unrelated image regions can produce similar descriptions. That is why the next stages filter ambiguous proposals and test geometric consistency.

Checkpoint: Are these zeros and ones the x/y coordinates of the keypoint? Answer: No. Position says where it is; the descriptor summarizes what its neighborhood looks like.

Source context:
[2] ORB (Oriented FAST and Rotated BRIEF). https://docs.opencv.org/4.13.0/d1/d89/tutorial_py_orb.html

Numbered sources:
[2] OpenCV contributors (2026). ORB (Oriented FAST and Rotated BRIEF). https://docs.opencv.org/4.13.0/d1/d89/tutorial_py_orb.html

## Slide 22: Matching: compare and reject ambiguity

Chronological slide 22 of 86. Part II. Optional detail. Hidden during the normal forty-five-minute slideshow. Use for preparation or questions.

Purpose in ordinary words:
Learn how actual ORB output supplies candidate point pairs.

Demonstration:
Follow detection, short yes/no fingerprints, descriptor comparisons and the ambiguity filter in order.

What to notice:
A descriptor is a pattern summary. Its bit disagreement count is not a distance in image pixels.

Interpretation:
ORB proposes pairs of distinctive local places; geometric checking still has to test their agreement.

Matching combined-demo lesson: orb. Open chronological/demo/index.html#orb.

Next main slide: 24. Residual: the gap left for one claimed pair.

Full discussion:
Compare toy fingerprints 10010111 and 10011001. Tests 5,6,and 7disagree, so their Hamming distance is three. A smaller Hamming distance means more agreeing bits for descriptions of equal length. It is not a distance in image pixels, not a probability, and not proof that the points represent the same physical part.

For each descriptor, a nearest-neighbor matcher finds candidates with the smallest descriptor distance. Nearest here means similar description, not necessarily nearby x/y coordinates. The ratio test compares the best distance with the second-best distance. If they are 12 and 20, the ratio is 0.6. With a chosen limit 0.75, this candidate passes because 0.6 is smaller than 0.75. If the distances are 18 and 20, the ratio is 0.9 and the match is considered ambiguous.

The limit 0.75 is a selected filtering parameter. It does not mean 75 percent accuracy. Filtering produces tentative point pairs. RANSAC then tests whether a group of those pairs agrees with one spatial model. Enough useful and well-distributed evidence is still required.

Source context:
[2] ORB (Oriented FAST and Rotated BRIEF). https://docs.opencv.org/4.13.0/d1/d89/tutorial_py_orb.html
[4] Camera Calibration and 3D Reconstruction: estimateAffinePartial2D. https://docs.opencv.org/4.13.0/d9/d0c/group__calib3d.html

Numbered sources:
[2] OpenCV contributors (2026). ORB (Oriented FAST and Rotated BRIEF). https://docs.opencv.org/4.13.0/d1/d89/tutorial_py_orb.html
[4] OpenCV contributors (2026). Camera Calibration and 3D Reconstruction: estimateAffinePartial2D. https://docs.opencv.org/4.13.0/d9/d0c/group__calib3d.html

## Slide 23: Real ORB experiment: read each stage

Chronological slide 23 of 86. Part II. Optional detail. Hidden during the normal forty-five-minute slideshow. Use for preparation or questions.

Purpose in ordinary words:
Learn how actual ORB output supplies candidate point pairs.

Demonstration:
Follow detection, short yes/no fingerprints, descriptor comparisons and the ambiguity filter in order.

What to notice:
A descriptor is a pattern summary. Its bit disagreement count is not a distance in image pixels.

Interpretation:
ORB proposes pairs of distinctive local places; geometric checking still has to test their agreement.

Matching combined-demo lesson: orb. Open chronological/demo/index.html#orb.

Next main slide: 24. Residual: the gap left for one claimed pair.

Full discussion:
The complete notebook performs these stages on a public camera photograph. The researcher deliberately creates a moved, rotated, and scaled version and keeps the generating transformation only for evaluation. ORB detects and describes image points without receiving that answer.

Read the detected-point counts first. These are counts of locations, not correct matches. Next read how many pairs survive the ratio test. Then read how many agree with the fitted model under the chosen residual threshold. Finally read the independent point error in pixels. Each number answers a different question.

The match illustration displays only a selected subset of lines for readability; the caption states the subset size and the total. The browser's saved ORB trace represents this executed Python run. It does not pretend that the JavaScript panel detects new ORB features after an upload.

Show the featureless-input case too. If no usable descriptor set is found, the code reports no estimate. It must not convert that absence into a zero error. This controlled study of one image and a known transform is educational evidence, not a benchmark across patients or scenes.

Executed example:
Real OpenCV ORB run: 1,169 detected fixed points and 1,170 moving points; 789 pairs pass the descriptor-ratio rule; 750 pairs have a returned RANSAC voting flag and 39 do not. These saved flags describe the selected voting stage. After the final least-squares refinement, some gaps near the threshold change; the returned flags need not equal a fresh threshold test on the final model. The 25 unused test points have mean correction error 0.1251 fixed-image pixels, with maximum 0.1618 pixels. This is one constructed transform on one public image.

Source context:
[2] ORB (Oriented FAST and Rotated BRIEF). https://docs.opencv.org/4.13.0/d1/d89/tutorial_py_orb.html
[3] Random Sample Consensus: A Paradigm for Model Fitting with Applications to Image Analysis and Automated Cartography. https://www.sri.com/publication/artificial-intelligence-pubs/random-sample-consensus-a-paradigm-for-model-fitting-with-applications-to-image-analysis-and-automated-cartography/
[4] Camera Calibration and 3D Reconstruction: estimateAffinePartial2D. https://docs.opencv.org/4.13.0/d9/d0c/group__calib3d.html
[10] skimage.data.camera. https://scikit-image.org/docs/stable/api/skimage.data#skimage.data.camera

Numbered sources:
[2] OpenCV contributors (2026). ORB (Oriented FAST and Rotated BRIEF). https://docs.opencv.org/4.13.0/d1/d89/tutorial_py_orb.html
[3] Martin A. Fischler and Robert C. Bolles (1981). Random Sample Consensus: A Paradigm for Model Fitting with Applications to Image Analysis and Automated Cartography. https://www.sri.com/publication/artificial-intelligence-pubs/random-sample-consensus-a-paradigm-for-model-fitting-with-applications-to-image-analysis-and-automated-cartography/
[4] OpenCV contributors (2026). Camera Calibration and 3D Reconstruction: estimateAffinePartial2D. https://docs.opencv.org/4.13.0/d9/d0c/group__calib3d.html
[10] scikit-image contributors; image by Lav Varshney (2026). skimage.data.camera. https://scikit-image.org/docs/stable/api/skimage.data#skimage.data.camera

## Slide 24: Residual: the gap left for one claimed pair

Chronological slide 24 of 86. Part II. Main route. Planned 0.94 minutes including the selected demonstration.

Purpose in ordinary words:
Understand the voting ruler before changing RANSAC settings.

Demonstration:
Read where a proposal predicts a dot, where its claimed partner is, and the gap between them.

What to notice:
A residual is one pair’s leftover gap. A threshold is the largest allowed gap for support.

Interpretation:
In the original forward fit the ruler uses moving-image pixels. It does not certify final alignment quality.

Matching combined-demo lesson: residual. Open chronological/demo/index.html#residual.

Next main slide: 27. RANSAC: suggest a move and collect votes.

Full discussion:
Purpose: understand the rule RANSAC will use to count agreement. A proposed movement predicts where a point should go. Its claimed partner is the measured location it is supposed to meet. A residual is the leftover gap between the prediction and the claimed partner. In the example, predicted (13,14) and claimed (10,10) differ by three across and four down, so the straight-line residual is five pixels. A residual threshold is the allowed gap for support. With a three-pixel threshold, five pixels fails. In the displayed toy comparisons equality counts as support. A wider threshold admits more points and may admit wrong claims. A narrower threshold may reject noisy correct claims. The original forward residual uses moving-image pixels. The later independent inverse check uses fixed-image pixels and separate known positions.

Expanded explanation and source context:
Residual means what is left over after using a model. In the original RANSAC panel, the fitted model predicts moving coordinates from fixed coordinates. Suppose it predicts moving location (13,14) for a fixed point, while the claimed moving partner is at (10,10). The horizontal gap is three and the vertical gap is four, so the straight-line residual is five pixels.

Both locations in this comparison are on the moving-image coordinate grid. Therefore this original residual is measured in moving-image pixels. It tests the model against the claimed pair. A wrong claim can sometimes agree with a wrong model, so a residual is not automatically a truth-based registration error.

The simpler beginner translation walkthrough writes the correction in the reverse direction and measures its agreement in fixed coordinates. Both conventions can be valid if named. The complete notebook and original screen explicitly state their forward convention so the threshold unit is understandable.

Checkpoint: Does residual five mean the image brightness values differ by five? Answer: No. This residual is a spatial ruler distance for a proposed point correspondence.

Source context:
[3] Random Sample Consensus: A Paradigm for Model Fitting with Applications to Image Analysis and Automated Cartography. https://www.sri.com/publication/artificial-intelligence-pubs/random-sample-consensus-a-paradigm-for-model-fitting-with-applications-to-image-analysis-and-automated-cartography/
[4] Camera Calibration and 3D Reconstruction: estimateAffinePartial2D. https://docs.opencv.org/4.13.0/d9/d0c/group__calib3d.html

Numbered sources:
[3] Martin A. Fischler and Robert C. Bolles (1981). Random Sample Consensus: A Paradigm for Model Fitting with Applications to Image Analysis and Automated Cartography. https://www.sri.com/publication/artificial-intelligence-pubs/random-sample-consensus-a-paradigm-for-model-fitting-with-applications-to-image-analysis-and-automated-cartography/
[4] OpenCV contributors (2026). Camera Calibration and 3D Reconstruction: estimateAffinePartial2D. https://docs.opencv.org/4.13.0/d9/d0c/group__calib3d.html

## Slide 25: The voting distance is a ruler setting

Chronological slide 25 of 86. Part II. Optional detail. Hidden during the normal forty-five-minute slideshow. Use for preparation or questions.

Purpose in ordinary words:
Understand the voting ruler before changing RANSAC settings.

Demonstration:
Read where a proposal predicts a dot, where its claimed partner is, and the gap between them.

What to notice:
A residual is one pair’s leftover gap. A threshold is the largest allowed gap for support.

Interpretation:
In the original forward fit the ruler uses moving-image pixels. It does not certify final alignment quality.

Matching combined-demo lesson: residual. Open chronological/demo/index.html#residual.

Next main slide: 27. RANSAC: suggest a move and collect votes.

Full discussion:
The threshold is the largest residual distance allowed for a vote. Residual means what remains after applying the candidate correction. In the default toy experiment, that threshold is two pixels. It is a chosen teaching setting, not an industry accuracy standard.

For a residual of 1.5 pixels and threshold 2 pixels, the pair votes. A residual of 3 pixels does not. The boundary includes equality. Increasing the threshold lets more pairs vote, possibly including wrong pairs. Decreasing it can reject useful but imperfect measurements.

Sigma and threshold are different knobs. Sigma changes the generated measured coordinates. Threshold changes the algorithm's agreement test on those coordinates. A higher vote count after loosening the threshold does not automatically mean better geometry.

Ask: If we increase the threshold from two to twenty, what does the larger inlier count prove? Answer: Only that more pairs fall inside the wider rule for that candidate. Check the correction against independent known positions before judging accuracy.

Source context:
[3] Random Sample Consensus: A Paradigm for Model Fitting with Applications to Image Analysis and Automated Cartography. https://www.sri.com/publication/artificial-intelligence-pubs/random-sample-consensus-a-paradigm-for-model-fitting-with-applications-to-image-analysis-and-automated-cartography/

Numbered sources:
[3] Martin A. Fischler and Robert C. Bolles (1981). Random Sample Consensus: A Paradigm for Model Fitting with Applications to Image Analysis and Automated Cartography. https://www.sri.com/publication/artificial-intelligence-pubs/random-sample-consensus-a-paradigm-for-model-fitting-with-applications-to-image-analysis-and-automated-cartography/

## Slide 26: Residual threshold: the voting ruler

Chronological slide 26 of 86. Part II. Optional detail. Hidden during the normal forty-five-minute slideshow. Use for preparation or questions.

Purpose in ordinary words:
Understand the voting ruler before changing RANSAC settings.

Demonstration:
Read where a proposal predicts a dot, where its claimed partner is, and the gap between them.

What to notice:
A residual is one pair’s leftover gap. A threshold is the largest allowed gap for support.

Interpretation:
In the original forward fit the ruler uses moving-image pixels. It does not certify final alignment quality.

Matching combined-demo lesson: residual. Open chronological/demo/index.html#residual.

Next main slide: 27. RANSAC: suggest a move and collect votes.

Full discussion:
Unpack the entire label RANSAC residual threshold. RANSAC tries proposed geometric models and gathers supporting pairs. A residual is the gap remaining for a claimed pair under one model. The threshold is the maximum gap allowed for that pair to support the proposal.

The original default is three moving-image pixels. A residual of 2 passes. A residual of 3 also passes because equality is included. A residual of 4 does not. That is a selected model-fitting tolerance, not a declaration that three-pixel final error is acceptable for every application.

Increasing the threshold can add useful noisy pairs and can also admit wrong ones. Decreasing it can reject incorrect evidence but may also reject genuine matches with imprecise locations. Sigma changes the simulated measurements; the residual threshold changes the voting test. They are different inputs.

Read the threshold experiment together with independent point error. More inliers alone do not establish a better correction. The original simulation tries 250 randomly sampled two-pair similarity proposals because its model includes turn and uniform size as well as shift. This differs from the twelve-suggestion translation-only teaching walkthrough.

OpenCV detail: the saved RANSAC inlier flags come from its voting stage. The final model is then refined with least squares. A few final gaps near the boundary can cross the threshold after this refinement; the notebook displays both returned flags and final measured gaps rather than calling them identical.

Source context:
[3] Random Sample Consensus: A Paradigm for Model Fitting with Applications to Image Analysis and Automated Cartography. https://www.sri.com/publication/artificial-intelligence-pubs/random-sample-consensus-a-paradigm-for-model-fitting-with-applications-to-image-analysis-and-automated-cartography/
[4] Camera Calibration and 3D Reconstruction: estimateAffinePartial2D. https://docs.opencv.org/4.13.0/d9/d0c/group__calib3d.html

Numbered sources:
[3] Martin A. Fischler and Robert C. Bolles (1981). Random Sample Consensus: A Paradigm for Model Fitting with Applications to Image Analysis and Automated Cartography. https://www.sri.com/publication/artificial-intelligence-pubs/random-sample-consensus-a-paradigm-for-model-fitting-with-applications-to-image-analysis-and-automated-cartography/
[4] OpenCV contributors (2026). Camera Calibration and 3D Reconstruction: estimateAffinePartial2D. https://docs.opencv.org/4.13.0/d9/d0c/group__calib3d.html

## Slide 27: RANSAC: suggest a move and collect votes

Chronological slide 27 of 86. Part II. Main route. Planned 0.94 minutes including the selected demonstration.

Purpose in ordinary words:
Understand why a fitting method needs protection from wrong pairs.

Demonstration:
Step through one proposal, measure residuals, collect support, and compare proposals.

What to notice:
A loose ruler admits more claims. A tight ruler may reject noisy correct claims.

Interpretation:
RANSAC means random sample consensus: try small samples and seek a larger group agreeing on one model.

Matching combined-demo lesson: ransac. Open chronological/demo/index.html#ransac.

Next main slide: 28. Experiment: RANSAC step by step.

Full discussion:
New model and ruler direction: this beginner toy proposes a correction slide back into the fixed picture and uses a two-fixed-pixel voting distance. The previous worked residual explained the original forward model in moving pixels. The idea of an allowed gap is shared, but the coordinate direction and units must be stated for each implementation.

RANSAC expands to random sample consensus. In ordinary words, suggest a movement from a small sample and ask how many proposed partners agree with it within the allowed gap. Try several suggestions, keep a well-supported one, then fit again using its supporting pairs. A supporting pair is called an inlier. A rejected pair is called an outlier relative to that proposal and rule; a rejection does not magically prove the true physical identity. The beginner live example fits a slide only. The original generated-pair panel fits a similarity movement. The saved OpenCV ORB experiment starts from actual detected points. Keep these different activities labeled.

Expanded explanation and source context:
Say: Suppose most friends know the same destination, but a few give directions to a different place. We can try one suggested move and see how many point pairs support it. Then we try another suggestion. This is the basic idea of RANSAC, Random Sample Consensus: random tries, a small sample, and agreement.

Our teaching model is translation only. One point pair can suggest its two-coordinate slide. The algorithm measures how far every corrected moving point is from its paired reference point. Pairs within the allowed ruler distance vote for that candidate.

The demo steps through candidates so the learner can see why a bad proposal loses votes. It uses constructed pairs, not ORB descriptors. In more complex models, a single pair is not enough; the sample size depends on the transform. Do not generalize this one-pair example to rotations, similarity transforms, or homographies.

Ask: Does a candidate need every point to agree? Answer: No. RANSAC is useful precisely because some pairs can be wrong, provided enough useful evidence supports an appropriate model.

Walkthrough boundary: ordinary RANSAC selects small subsets randomly. This teaching implementation deliberately tries all twelve one-pair translation suggestions in visible order so every vote can be inspected. It demonstrates the consensus idea exhaustively; it does not implement random sampling. The original image-registration package shows the library-based robust estimator.

Source context:
[3] Random Sample Consensus: A Paradigm for Model Fitting with Applications to Image Analysis and Automated Cartography. https://www.sri.com/publication/artificial-intelligence-pubs/random-sample-consensus-a-paradigm-for-model-fitting-with-applications-to-image-analysis-and-automated-cartography/

Numbered sources:
[3] Martin A. Fischler and Robert C. Bolles (1981). Random Sample Consensus: A Paradigm for Model Fitting with Applications to Image Analysis and Automated Cartography. https://www.sri.com/publication/artificial-intelligence-pubs/random-sample-consensus-a-paradigm-for-model-fitting-with-applications-to-image-analysis-and-automated-cartography/

## Slide 28: Experiment: RANSAC step by step

Chronological slide 28 of 86. Part II. Main route. Planned 2.31 minutes including the selected demonstration.

Purpose in ordinary words:
Understand why a fitting method needs protection from wrong pairs.

Demonstration:
Step through one proposal, measure residuals, collect support, and compare proposals.

What to notice:
A loose ruler admits more claims. A tight ruler may reject noisy correct claims.

Interpretation:
RANSAC means random sample consensus: try small samples and seek a larger group agreeing on one model.

Matching combined-demo lesson: ransac. Open chronological/demo/index.html#ransac.

Next main slide: 30. ORB results under turn and blur.

Full discussion:
Open the dot lesson labeled for the corresponding lessons in this part. First reveal the known generated translation (+6,-4)and the correction (-6,+4), then hide the answer if desired. Show the all-pairs average as a simple comparator. It can be pulled by deliberately bad correspondences.

Step to one candidate. Identify the selected pair, read its proposed horizontal and vertical correction, and point to one supporting and one rejecting pair. Count the votes. Step through more candidates before revealing the winning candidate. Explain any ties instead of treating the selected index as extra certainty.

The winning group's proposed corrections are averaged to refine the translation. This refit uses the selected consensus group. It is not a claim that averaging all original pairs is robust. Read the final correction and compare its independent geometric error with the all-pairs average.

Change sigma or the voting threshold one at a time. Keep the construction settings and seed visible. The purpose is to understand each stage, not to find settings that always make the displayed number look better. A few successful toy trials do not prove general reliability.

In the saved default example, several proposals tie at eight votes and they do not all select exactly the same group. One proposal swaps genuine noisy pair 4 for genuine noisy pair 11. The visible implementation chooses the first highest-vote proposal as its stated tie rule. The tie is useful uncertainty information, not proof of a unique best geometric solution.

Executed example:
The default first-winning group is pairs 1,2,4,5,6,7,9,10. Pair 11 is a genuine generated match rejected by the two-pixel voting rule because of its realized click error. Pair 5 proposes an alternative tied group containing 11 instead of 4. The shared frozen offsets make this inspectable.

Source context:
[3] Random Sample Consensus: A Paradigm for Model Fitting with Applications to Image Analysis and Automated Cartography. https://www.sri.com/publication/artificial-intelligence-pubs/random-sample-consensus-a-paradigm-for-model-fitting-with-applications-to-image-analysis-and-automated-cartography/

Numbered sources:
[3] Martin A. Fischler and Robert C. Bolles (1981). Random Sample Consensus: A Paradigm for Model Fitting with Applications to Image Analysis and Automated Cartography. https://www.sri.com/publication/artificial-intelligence-pubs/random-sample-consensus-a-paradigm-for-model-fitting-with-applications-to-image-analysis-and-automated-cartography/

## Slide 29: ORB matching under rotation and blur

Chronological slide 29 of 86. Part II. Optional detail. Hidden during the normal forty-five-minute slideshow. Use for preparation or questions.

Purpose in ordinary words:
Test an ORB idea [14] with RANSAC [3] using recorded OpenCV runs.

Demonstration:
Select an image turn and blur. Read detections, filtered matches, support and independent error.

What to notice:
The browser selects a saved CPU result. Blur sigma is a softening footprint in pixels, not point-click noise.

Interpretation:
Many detected or accepted points do not automatically imply a smaller geometric error.

Matching combined-demo lesson: R2. Open chronological/demo/index.html#R2.

Next main slide: 30. ORB results under turn and blur.

Full discussion:
A keypoint is a detected image location. Its descriptor describes the nearby brightness pattern with zeros and ones. ORB supplies these locations and descriptions. Hamming distance counts how many descriptor bits disagree. The ratio test compares the best descriptor match with the second-best candidate, rejecting ambiguous suggestions. The chosen ratio limit is a filtering setting, not a percentage accuracy.

The researcher actually runs OpenCV ORB on a bundled public camera photograph and transformed copies. Twelve conditions combine four turns with three moving-image blur settings. A Gaussian blur mixes nearby brightness values and softens small details. The blur sigma here measures the width of that image filter in pixels. It is different from simulated point-click noise sigma in R1.

ORB itself detects and describes features. Matching and geometric fitting complete the registration pipeline. RANSAC, supported by Fischler and Bolles [3], selects pairs agreeing with a similarity model. Its threshold is three moving-image pixels. OpenCV's returned support flags describe its voting stage; refinement can change final gaps near the threshold. Twenty-five unused points check inverse recovery in fixed-image pixels.

The reproduction uses a contemporary established library, one public image, and known transformations. It does not repeat the original ORB paper's full benchmark or runtime comparisons with SIFT and SURF. Counts of detected points, filtered pairs, and RANSAC supporters answer different questions. None is an accuracy percentage. The browser replays these executed Python conditions and clearly labels the recorded results.

Published study: Ethan Rublee, Vincent Rabaud, Kurt Konolige, Gary Bradski. ORB: An efficient alternative to SIFT or SURF (2011).
Primary source: https://doi.org/10.1109/ICCV.2011.6126544

What the paper contributes:
ORB combines oriented FAST keypoints with a rotated, learned binary descriptor to obtain an efficient feature method; the original paper evaluates its matching behavior on its own experiments.

Evidence locations:
p. 2564, abstract and Section 1: Oriented FAST and rotated binary descriptor; matching and efficiency motivation.
pp. 2569-2570, Sections 6.1-6.3: Original CPU benchmarks and applications differ from this classroom alignment test; the phone tracking example assumes a planar, well-textured keyframe surface.

Published limitation or scope boundary:
The specific phone-tracking application in Section 6.3 assumes a planar surface with sufficient texture. This is an application assumption, not a statement that every ORB use is planar. The original comparative timings describe its own implementation and hardware.
Evidence location: p. 2570, Sections 6.1 and 6.3

Classroom adaptation:
Run actual Python/OpenCV ORB and RANSAC on a 256 x 256 public photograph under four rotations (0, 15, 45, 75 degrees) and three moving-image blur settings (sigma 0, 1.5, 3 pixels). Replay saved real descriptors, matches, and fitted transforms in the browser. Fit in the forward fixed-to-moving direction and separately evaluate an inverse independent-point check.

What this experiment does not reproduce:
Re-training the learned rBRIEF test pattern
Original descriptor benchmark datasets and complete comparisons with SIFT/SURF
Original smartphone implementation or hardware speed claims

Follow-up question for this class:
How do rotation and blur change usable match support and independent geometric error in this particular ORB-plus-RANSAC pipeline?

Supported conclusion:
How the chosen ORB-plus-RANSAC pipeline behaves on the recorded controlled transformations.

Boundary on the conclusion:
That the original paper's comparative speed or descriptor rankings have been replicated, or that feature counts certify correct geometry.

The classroom question does not carry a claim of novel or currently unsolved research.

Numbered sources:
[14] Ethan Rublee, Vincent Rabaud, Kurt Konolige, Gary Bradski (2011). ORB: An efficient alternative to SIFT or SURF. https://doi.org/10.1109/ICCV.2011.6126544

## Slide 30: ORB results under turn and blur

Chronological slide 30 of 86. Part II. Main route. Planned 1.1 minutes including the selected demonstration.

Purpose in ordinary words:
Test an ORB idea [14] with RANSAC [3] using recorded OpenCV runs.

Demonstration:
Select an image turn and blur. Read detections, filtered matches, support and independent error.

What to notice:
The browser selects a saved CPU result. Blur sigma is a softening footprint in pixels, not point-click noise.

Interpretation:
Many detected or accepted points do not automatically imply a smaller geometric error.

Matching combined-demo lesson: R2. Open chronological/demo/index.html#R2.

Next main slide: 31. Part III. How can brightness numbers help?.

Full discussion:
A keypoint is a detected image location. Its descriptor describes the nearby brightness pattern with zeros and ones. ORB supplies these locations and descriptions. Hamming distance counts how many descriptor bits disagree. The ratio test compares the best descriptor match with the second-best candidate, rejecting ambiguous suggestions. The chosen ratio limit is a filtering setting, not a percentage accuracy.

The researcher actually runs OpenCV ORB on a bundled public camera photograph and transformed copies. Twelve conditions combine four turns with three moving-image blur settings. A Gaussian blur mixes nearby brightness values and softens small details. The blur sigma here measures the width of that image filter in pixels. It is different from simulated point-click noise sigma in R1.

ORB itself detects and describes features. Matching and geometric fitting complete the registration pipeline. RANSAC, supported by Fischler and Bolles [3], selects pairs agreeing with a similarity model. Its threshold is three moving-image pixels. OpenCV's returned support flags describe its voting stage; refinement can change final gaps near the threshold. Twenty-five unused points check inverse recovery in fixed-image pixels.

The reproduction uses a contemporary established library, one public image, and known transformations. It does not repeat the original ORB paper's full benchmark or runtime comparisons with SIFT and SURF. Counts of detected points, filtered pairs, and RANSAC supporters answer different questions. None is an accuracy percentage. The browser replays these executed Python conditions and clearly labels the recorded results.

Published study: Ethan Rublee, Vincent Rabaud, Kurt Konolige, Gary Bradski. ORB: An efficient alternative to SIFT or SURF (2011).
Primary source: https://doi.org/10.1109/ICCV.2011.6126544

What the paper contributes:
ORB combines oriented FAST keypoints with a rotated, learned binary descriptor to obtain an efficient feature method; the original paper evaluates its matching behavior on its own experiments.

Evidence locations:
p. 2564, abstract and Section 1: Oriented FAST and rotated binary descriptor; matching and efficiency motivation.
pp. 2569-2570, Sections 6.1-6.3: Original CPU benchmarks and applications differ from this classroom alignment test; the phone tracking example assumes a planar, well-textured keyframe surface.

Published limitation or scope boundary:
The specific phone-tracking application in Section 6.3 assumes a planar surface with sufficient texture. This is an application assumption, not a statement that every ORB use is planar. The original comparative timings describe its own implementation and hardware.
Evidence location: p. 2570, Sections 6.1 and 6.3

Classroom adaptation:
Run actual Python/OpenCV ORB and RANSAC on a 256 x 256 public photograph under four rotations (0, 15, 45, 75 degrees) and three moving-image blur settings (sigma 0, 1.5, 3 pixels). Replay saved real descriptors, matches, and fitted transforms in the browser. Fit in the forward fixed-to-moving direction and separately evaluate an inverse independent-point check.

What this experiment does not reproduce:
Re-training the learned rBRIEF test pattern
Original descriptor benchmark datasets and complete comparisons with SIFT/SURF
Original smartphone implementation or hardware speed claims

Follow-up question for this class:
How do rotation and blur change usable match support and independent geometric error in this particular ORB-plus-RANSAC pipeline?

Supported conclusion:
How the chosen ORB-plus-RANSAC pipeline behaves on the recorded controlled transformations.

Boundary on the conclusion:
That the original paper's comparative speed or descriptor rankings have been replicated, or that feature counts certify correct geometry.

The classroom question does not carry a claim of novel or currently unsolved research.

Purpose of this experiment:
Observe how a recognizable-place pipeline changes when the movable picture turns or becomes smoother.

Recorded settings:
256 px public camera; maximum 1,000 keypoints; WTA_K=2; ratio <0.75; threshold 3 moving px; 4 angles x 3 blur levels.

Interpretation of the measured rows:
Strong blur reduced match counts and increased independent geometric error in these measured conditions.

Limits of this classroom run:
One public photo; synthetic movement; no detector benchmark, real camera acquisition or timing comparison. Returned inlier masks precede final refinement.

Read the condition first, name the measurement and its unit, and compare it with the known generated answer. Full raw measurements and figures are retained in the notebook and results files.

Numbered sources:
[14] Ethan Rublee, Vincent Rabaud, Kurt Konolige, Gary Bradski (2011). ORB: An efficient alternative to SIFT or SURF. https://doi.org/10.1109/ICCV.2011.6126544

## Slide 31: Part III. How can brightness numbers help?

Chronological slide 31 of 86. Part III. Main route. Planned 0.3 minutes including the selected demonstration.

Purpose in ordinary words:
Compare light and dark numbers while trying movements.

Demonstration:
Read the question before touching any controls. Imagine the familiar example.

What to notice:
Slide two numbered strips and write down a score at each stop.

Interpretation:
A computer can compare many pixels even when distinctive point pairs are difficult to find.

Matching combined-demo lesson: purpose-III. Open chronological/demo/index.html#purpose-III.

Next main slide: 33. MSE: subtract, square and average.

Full discussion:
Begin with the familiar situation before naming the technical topic. Slide two numbered strips and write down a score at each stop. Compare light and dark numbers while trying movements. A computer can compare many pixels even when distinctive point pairs are difficult to find. Explain that this is the purpose of intensity-based registration. Ask the audience to predict what useful evidence would look like. The following slides explain the unfamiliar labels before the experiment. At the end of the part, return to the question: Which tried movement gives the best score for this comparison rule?

## Slide 32: A score is a rule for comparing

Chronological slide 32 of 86. Part III. Optional detail. Hidden during the normal forty-five-minute slideshow. Use for preparation or questions.

Purpose in ordinary words:
Learn the comparison rule one arithmetic step at a time.

Demonstration:
Subtract paired values, square the gaps, add them, then divide by the count.

What to notice:
For gaps [−1,0,0,1], the squared gaps average to 0.5.

Interpretation:
Smaller MSE means less squared brightness mismatch under the same scaling and samples. It is not a position distance.

Matching combined-demo lesson: mse. Open chronological/demo/index.html#mse.

Next main slide: 33. MSE: subtract, square and average.

Full discussion:
Say: A score is a number produced by a rule. Imagine comparing two spelling answers by exact letters, word length, or meaning. Those rules would answer different questions. Picture-comparison rules also answer different questions.

We will learn three. MSE asks how different the brightness numbers are at paired places. Signed NCC asks whether brightness changes follow the same upward or downward pattern. Mutual information asks how much knowing a value in one picture helps predict a value in the other. The last two explanations will become concrete with tiny lists and count tables.

Before interpreting any score, ask four things: what was compared, what units or scale are used, which direction is preferred, and which assumption makes that comparison sensible. The scores are not automatically percentages of correct alignment.

Checkpoint: Does a larger number always mean better? Answer: No. For MSE, smaller is preferred. For the signed NCC and mutual information objectives used here, larger is preferred. We will label that beside every graph.

## Slide 33: MSE: subtract, square and average

Chronological slide 33 of 86. Part III. Main route. Planned 0.94 minutes including the selected demonstration.

Purpose in ordinary words:
Learn the comparison rule one arithmetic step at a time.

Demonstration:
Subtract paired values, square the gaps, add them, then divide by the count.

What to notice:
For gaps [−1,0,0,1], the squared gaps average to 0.5.

Interpretation:
Smaller MSE means less squared brightness mismatch under the same scaling and samples. It is not a position distance.

Matching combined-demo lesson: mse. Open chronological/demo/index.html#mse.

Next main slide: 36. RMSE: finish by taking a square root.

Full discussion:
MSE means mean squared error. Its purpose is to measure disagreement between brightness values at paired addresses. First find each gap: reference [0,1,2,3] minus other [1,1,2,2] gives [−1,0,0,1]. Squaring gives [1,0,0,1], preventing positive and negative gaps from cancelling. Add to get two, then divide by four pairs to get MSE 0.5. Mean means average. Smaller is better for this mismatch rule, and zero means the compared brightness numbers match exactly. Its units are squared brightness units on this toy zero-to-three scale. A brightness change can increase MSE even when geometry is correct. MSE is not the geometric position error in pixels.

Expanded explanation and source context:
Say: Put the two lists directly under each other. Each column is one pair of compared brightness values. Subtract the lower value from the upper value. In the first column, zero minus one is minus one. The next two columns both give zero. The last gives one.

Point to the arithmetic table and work through every column aloud. A zero difference means that pair has equal brightness. A minus sign says which value was smaller. It does not mean a distance is negative.

If we simply add these differences, minus one and plus one cancel, giving zero even though two pairs are unequal. We need a rule that preserves the size of each mismatch without allowing that cancellation. Squaring each difference prevents that cancellation. Optional detail shows the steps separately.

Checkpoint: Which columns match exactly? Answer: The middle two. We are comparing brightness numbers at the chosen positions. This table alone does not prove that the positions represent the same real object. The researcher uses known geometry to check that separately.

## Slide 34: MSE step 2: square, add, divide

Chronological slide 34 of 86. Part III. Optional detail. Hidden during the normal forty-five-minute slideshow. Use for preparation or questions.

Purpose in ordinary words:
Learn the comparison rule one arithmetic step at a time.

Demonstration:
Subtract paired values, square the gaps, add them, then divide by the count.

What to notice:
For gaps [−1,0,0,1], the squared gaps average to 0.5.

Interpretation:
Smaller MSE means less squared brightness mismatch under the same scaling and samples. It is not a position distance.

Matching combined-demo lesson: mse. Open chronological/demo/index.html#mse.

Next main slide: 36. RMSE: finish by taking a square root.

Full discussion:
Say: Squaring a number means multiplying it by itself. Minus one times minus one gives plus one. One times one also gives one. Our squared differences are therefore 1,0,0,1. Add them to get 2. There are four pairs, so divide 2 by 4. The answer is 0.5.

Now unpack the name: mean means average, squared refers to multiplying each difference by itself, and error means the brightness mismatch according to this rule. MSE is mean squared error. For this toy brightness scale, the unit is squared brightness units. A value of 0.5 does not mean 50 percent accurate.

Lower MSE means smaller average squared brightness mismatch on the compared cells. Zero means those particular values are identical. A one-cell difference of two contributes four after squaring, so this rule gives extra weight to larger mismatches.

Ask: Could an unaligned repeated pattern also produce a low score? Answer: It can. That is one reason a brightness score is not automatically a geometric proof.

## Slide 35: Why brighter can fool MSE

Chronological slide 35 of 86. Part III. Optional detail. Hidden during the normal forty-five-minute slideshow. Use for preparation or questions.

Purpose in ordinary words:
Learn the comparison rule one arithmetic step at a time.

Demonstration:
Subtract paired values, square the gaps, add them, then divide by the count.

What to notice:
For gaps [−1,0,0,1], the squared gaps average to 0.5.

Interpretation:
Smaller MSE means less squared brightness mismatch under the same scaling and samples. It is not a position distance.

Matching combined-demo lesson: mse. Open chronological/demo/index.html#mse.

Next main slide: 36. RMSE: finish by taking a square root.

Full discussion:
Compare[0,1,2,3] with[2,3,4,5]. The four positions correspond exactly, but every value in the second list is two brighter. Each squared difference is four, so MSE is four on this toy scale. That does not mean the picture is four pixels away.

Say: MSE is doing exactly what its rule says: it penalizes unequal brightness. It has no knowledge that we deliberately brightened the picture without moving it. If a registration task expects equal values at corresponding locations, that rule may be useful. If the appearance relationship changes, it can prefer an unsuitable move.

Ask: What stayed the same? Answer: The ordering and pattern of the values, and their locations. What changed? Their brightness numbers. The next rule focuses on how the values vary together instead of requiring equal values.

Important boundary: a score can be useful under an assumption without working for every image pair. The researcher explains the assumption before presenting the result.

## Slide 36: RMSE: finish by taking a square root

Chronological slide 36 of 86. Part III. Main route. Planned 0.94 minutes including the selected demonstration.

Purpose in ordinary words:
Learn what the extra R in RMSE changes.

Demonstration:
Finish the MSE calculation, then take its square root. Compare the units.

What to notice:
The square root of 0.5 is about 0.707. A brightness RMSE keeps brightness units.

Interpretation:
Name the measured quantity: brightness RMSE differs from a point-distance statistic in pixels.

Matching combined-demo lesson: rmse. Open chronological/demo/index.html#rmse.

Next main slide: 38. Signed NCC compares an up-and-down pattern.

Full discussion:
Use the same worked lists as the earlier lesson: reference[0,1,2,3] and other[1,1,2,2]. Differences are[-1,0,0,1]. Squaring gives[1,0,0,1]. Add to get 2 and divide by 4 pairs to get MSE 0.5.

RMSE adds one last operation: take the square root. The square root is the positive number that gives 0.5 when multiplied by itself. It is approximately 0.7071, because 0.7071 times 0.7071 is approximately 0.5. Now unpack the name: root mean squared error. The root undoes the squared unit, so this brightness RMSE is in the original brightness units rather than squared brightness units.

In this lab, RMSE compares brightness values over pixels valid in both images. It does not measure landmark distances. RMSE can have other units in other applications; the quantity being compared determines its unit. Zero means those compared brightness values are equal. It does not by itself establish correct anatomy or a universally good alignment.

This four-list arithmetic uses the toy 0–3 scale. The original image browser uses 0–1 brightness values. The notebook shows both scales so the units cannot be confused.

Source context:
[8] Registration Overview. https://simpleitk.readthedocs.io/en/latest/registrationOverview.html
[9] Image Similarity and Tissue Overlaps as Surrogates for Image Registration Accuracy: Widely Used but Unreliable. https://pmc.ncbi.nlm.nih.gov/articles/PMC3274625/

Numbered sources:
[8] SimpleITK contributors (2026). Registration Overview. https://simpleitk.readthedocs.io/en/latest/registrationOverview.html
[9] Torsten Rohlfing (2012). Image Similarity and Tissue Overlaps as Surrogates for Image Registration Accuracy: Widely Used but Unreliable. https://pmc.ncbi.nlm.nih.gov/articles/PMC3274625/

## Slide 37: Brightness error and position error

Chronological slide 37 of 86. Part III. Optional detail. Hidden during the normal forty-five-minute slideshow. Use for preparation or questions.

Purpose in ordinary words:
Learn what the extra R in RMSE changes.

Demonstration:
Finish the MSE calculation, then take its square root. Compare the units.

What to notice:
The square root of 0.5 is about 0.707. A brightness RMSE keeps brightness units.

Interpretation:
Name the measured quantity: brightness RMSE differs from a point-distance statistic in pixels.

Matching combined-demo lesson: rmse. Open chronological/demo/index.html#rmse.

Next main slide: 38. Signed NCC compares an up-and-down pattern.

Full discussion:
Imagine two tracing sheets lined up perfectly, but one is darker. Their corner positions agree while their brightness values differ. The image RMSE can therefore be above zero while the geometric point error is zero.

Now imagine an identical small gray patch appearing at the wrong position in a repeated pattern. Its brightness numbers might agree even though the intended structure is misplaced. A small brightness error alone is therefore not a geometric guarantee.

For a point, use a ruler. If its corrected location is three pixels horizontally and four pixels vertically away from the known correct location, its straight-line distance is five pixels. For several independent points, the lab averages their straight-line distances. This is not the same calculation as taking the square root of an average squared brightness difference.

The original transformation demo uses a known inverse to restore exact coordinate geometry. Its RMSE may still remain above zero because rotation/scaling and resampling alter pixel values and can lose cropped content. State which type of error is on screen before calling a value good or bad.

Executed example:
On the public-image experiment's common valid support, image RMSE is 0.185308 before correction, 0.017196 after estimated correction, and 0.016414 with the supplied correct inverse. The last value is above zero because resampling changes values. All three use normalized 0–1 brightness, not pixel distances.

Source context:
[9] Image Similarity and Tissue Overlaps as Surrogates for Image Registration Accuracy: Widely Used but Unreliable. https://pmc.ncbi.nlm.nih.gov/articles/PMC3274625/

Numbered sources:
[9] Torsten Rohlfing (2012). Image Similarity and Tissue Overlaps as Surrogates for Image Registration Accuracy: Widely Used but Unreliable. https://pmc.ncbi.nlm.nih.gov/articles/PMC3274625/

## Slide 38: Signed NCC compares an up-and-down pattern

Chronological slide 38 of 86. Part III. Main route. Planned 0.94 minutes including the selected demonstration.

Purpose in ordinary words:
Understand plus one, zero, minus one and a flat row before reading a curve.

Demonstration:
Compare a brighter rising row, a reversed row, an unhelpful linear pattern and a constant row.

What to notice:
+1 is perfect same-direction linear agreement. −1 is perfect opposite direction. A flat row makes NCC undefined.

Interpretation:
The chosen signed-NCC search seeks the highest signed value. Zero does not rule out every nonlinear relationship.

Matching combined-demo lesson: ncc. Open chronological/demo/index.html#ncc.

Next main slide: 40. Sampling offset and correction have opposite signs.

Full discussion:
Signed normalized cross-correlation, abbreviated signed NCC, asks whether paired values rise and fall together in a linear pattern. Signed means the minus sign matters. Against [0,1,2,3], [2,3,4,5] gives plus one: the same rising pattern despite a brightness offset. [3,2,1,0] gives minus one: a perfect opposite-direction linear pattern. [1,0,0,1] gives zero linear correlation in this toy. Zero does not prove that no nonlinear relationship exists. A constant row gives no variation, so the formula divides by zero and the score is undefined. The score has no units. The chosen search maximizes the signed value, so minus one is not a high score under this objective. No absolute-value NCC objective is used here.

Expanded explanation and source context:
Say: Read each list from left to right. Both start low and rise in the same way. Even though the second is brighter, their pattern of variation matches perfectly. Signed normalized cross-correlation, shortened to signed NCC, gives plus one for this perfect positive linear relationship.

The calculation first subtracts each list's own average. The first average is 1.5. The second average is 3.5. Both centered lists become[-1.5,-0.5,0.5,1.5]. Centered means rewritten as above or below that list's average. The calculation then compares these centered patterns on a common normalized scale.

The optional calculation is explained in the mathematical details for this topic. The main idea comes first: are deviations above and below average happening together? Positive means together; negative means opposite. The score has no pixel-distance unit and is not a percentage.

Ask: Does plus one always prove correct spatial alignment? Answer: No. It describes the compared brightness pattern. Geometry still requires an appropriate model and independent checking.

## Slide 39: The sign matters: +1, 0, and −1

Chronological slide 39 of 86. Part III. Optional detail. Hidden during the normal forty-five-minute slideshow. Use for preparation or questions.

Purpose in ordinary words:
Understand plus one, zero, minus one and a flat row before reading a curve.

Demonstration:
Compare a brighter rising row, a reversed row, an unhelpful linear pattern and a constant row.

What to notice:
+1 is perfect same-direction linear agreement. −1 is perfect opposite direction. A flat row makes NCC undefined.

Interpretation:
The chosen signed-NCC search seeks the highest signed value. Zero does not rule out every nonlinear relationship.

Matching combined-demo lesson: ncc. Open chronological/demo/index.html#ncc.

Next main slide: 40. Sampling offset and correction have opposite signs.

Full discussion:
Compare[0,1,2,3] with[3,2,1,0]. The first rises while the second falls. Their signed NCC is minus one. That is a strong opposite relationship, not a weak same-direction relationship. When the objective maximizes signed NCC, plus one is preferred to minus one. Taking the absolute value would create a different rule.

The example[1,0,0,1] has zero signed NCC with our reference list. Zero means no linear agreement in these paired values. It does not mean there is no possible nonlinear relationship in any dataset.

For[2,2,2,2], there is no up-and-down variation at all. The denominator of the usual NCC formula becomes zero. The correct explanation is cannot calculate because there is no variation. The demo must not quietly report a numeric zero for that case.

Ask: If we invert brightness but keep the positions correct, must NCC become positive? Answer: No. It may be minus one. This separates a brightness relationship from a spatial movement. Explain the sign before asking the audience to interpret a graph.

## Slide 40: Sampling offset and correction have opposite signs

Chronological slide 40 of 86. Part III. Main route. Planned 0.94 minutes including the selected demonstration.

Purpose in ordinary words:
Prevent sign confusion when reading an image-search answer.

Demonstration:
Follow a feature from reference x=10 to moving x=30.

What to notice:
Correct the point by −20 pixels; sample the moving picture at +20 pixels relative to the reference address.

Interpretation:
Always name whether a number is a generated move, an applied correction or a sampling offset.

Matching combined-demo lesson: offset. Open chronological/demo/index.html#offset.

Next main slide: 41. Graphs are maps of recorded answers.

Full discussion:
This is the source of a particularly confusing sign in the original translation screen. Suppose a feature at fixed x 10 is stored in the moving image at x 30because the researcher shifted the picture 20 pixels right. To move that feature back, the point correction is minus 20.

But when filling the fixed-grid output at x 10, the software must look in the moving image at x 30 to get the right value. The sampling offset is therefore plus 20. Here F means fixed-picture brightness, M means moving-picture brightness, and p is a reference address. The browser tests M(p+(u,v)) against F(p). Its candidate controls describe the source lookup offset. The point correction applied to the moving picture is(-u,-v).

The known default translation is(+20,-12). The matching sampling offset is(+20,-12); the point correction is(-20,+12). Zero candidate offset means no correction. The browser displays both conventions in its help rather than expecting the learner to guess.

The new simpler one-dimensional teaching graph labels an applied correction directly. Its known value is minus 3 for a picture generated plus 3 right. Both examples are valid, but their axis labels refer to different directions and must be read carefully.

Source context:
[1] Image Alignment and Stitching: A Tutorial. https://www.microsoft.com/en-us/research/publication/image-alignment-and-stitching-a-tutorial/
[8] Registration Overview. https://simpleitk.readthedocs.io/en/latest/registrationOverview.html

Numbered sources:
[1] Richard Szeliski (2004). Image Alignment and Stitching: A Tutorial. https://www.microsoft.com/en-us/research/publication/image-alignment-and-stitching-a-tutorial/
[8] SimpleITK contributors (2026). Registration Overview. https://simpleitk.readthedocs.io/en/latest/registrationOverview.html

## Slide 41: Graphs are maps of recorded answers

Chronological slide 41 of 86. Part III. Main route. Planned 0.94 minutes including the selected demonstration.

Purpose in ordinary words:
Read axes and one point before judging a whole score curve.

Demonstration:
Try one correction. Locate its dot. Change the correction and watch both the picture and the dot.

What to notice:
Across is the candidate movement in pixels. Up is the stated score. Lowest MSE and highest signed NCC use different directions.

Interpretation:
A curve records the comparison rule’s answers, not percentages of correct alignment.

Matching combined-demo lesson: graph. Open chronological/demo/index.html#graph.

Next main slide: 46. Translation-component error: the slide part only.

Full discussion:
Read the graph as a record of attempted answers. The horizontal coordinate is one tried correction in pixels. The vertical coordinate is the MSE recorded at that correction, in squared brightness units. A dot is a measurement for one candidate. The line simply joins neighboring recorded candidates to help the eye. The dashed line is the known answer and the highlighted point is the current candidate. Name the zero-to-one brightness normalization and the shared sample region before comparing score heights. This first graph lesson limits choices to MSE and signed NCC; MI comes after its explanation in Part IV.

Expanded explanation and source context:
Say: A graph is a tidy way to keep many little experiment answers. Along the bottom, we list the candidate horizontal corrections. Candidate means a move we are considering. Along the side, we show the score produced after trying that move.

Read one dot as a sentence: when the researcher tried this horizontal correction, the score was this value. To read it, go down from the dot to the horizontal axis for the move and across to the vertical axis for the score. Axis means the labeled measuring line at the edge of the graph.

The line connects neighboring recorded dots to help our eyes follow them. It does not mean the computer evaluated every fractional move between the dots. This teaching scan tries thirteen integer corrections from minus six through plus six. The experiment holds the picture data and compared region fixed.

Ask: Is a tall dot automatically better? Answer: Only if larger values are preferred by the chosen rule. MSE prefers the low dot. We will label the preferred direction on each graph.

## Slide 42: One graph dot belongs to one picture position

Chronological slide 42 of 86. Part III. Optional detail. Hidden during the normal forty-five-minute slideshow. Use for preparation or questions.

Purpose in ordinary words:
Read axes and one point before judging a whole score curve.

Demonstration:
Try one correction. Locate its dot. Change the correction and watch both the picture and the dot.

What to notice:
Across is the candidate movement in pixels. Up is the stated score. Lowest MSE and highest signed NCC use different directions.

Interpretation:
A curve records the comparison rule’s answers, not percentages of correct alignment.

Matching combined-demo lesson: graph. Open chronological/demo/index.html#graph.

Next main slide: 46. Translation-component error: the slide part only.

Full discussion:
Open the combined demo lesson named graph, which follows the current slide badge. Choose the same-contrast example. Point to the highlighted candidate and read its horizontal coordinate aloud. Then point to the overlay and explain that the moving image receives exactly that correction.

Move one slider step. The picture position changes and the highlighted graph dot changes together. Read the new score. This connects the abstract graph to something visible. The vertical score is not a distance unless the graph explicitly says geometric point error.

Ask the audience to predict which dot belongs to the correctly returned corner before revealing the known answer. The true correction is minus three pixels because the researcher originally moved the image three pixels right. Zero on the horizontal axis means no correction. Zero on an MSE axis means no difference among the compared brightness values. Those are two different meanings of zero.

Explain every displayed marker using the legend. A marker for the known answer comes from the construction. A marker for the selected score optimum comes from the rule. Their agreement is something to check, not assume.

## Slide 43: A score belongs to one tried position

Chronological slide 43 of 86. Part III. Optional detail. Hidden during the normal forty-five-minute slideshow. Use for preparation or questions.

Purpose in ordinary words:
Read axes and one point before judging a whole score curve.

Demonstration:
Try one correction. Locate its dot. Change the correction and watch both the picture and the dot.

What to notice:
Across is the candidate movement in pixels. Up is the stated score. Lowest MSE and highest signed NCC use different directions.

Interpretation:
A curve records the comparison rule’s answers, not percentages of correct alignment.

Matching combined-demo lesson: graph. Open chronological/demo/index.html#graph.

Next main slide: 46. Translation-component error: the slide part only.

Full discussion:
A graph is a notebook of recorded answers. First name the horizontal axis: a candidate horizontal movement in pixels. Then name the vertical axis: the score calculated at that movement. One dot belongs to one tried position. A low MSE dot means less squared brightness mismatch. A high signed NCC dot means a stronger same-direction linear pattern. Neither height is a percentage of correct alignment. Hold all other settings fixed before comparing candidates. In the full two-dimensional browser search, the curve shows only one horizontal row while the vertical candidate stays fixed. A correct horizontal offset can still have a wrong vertical offset. Demonstrate the small numbered-strip graph first, then the full image search. Mutual information is introduced in Part IV before its separate contrast search.

Numbered sources:
[1] Richard Szeliski (2004). Image Alignment and Stitching: A Tutorial. https://www.microsoft.com/en-us/research/publication/image-alignment-and-stitching-a-tutorial/
[8] SimpleITK contributors (2026). Registration Overview. https://simpleitk.readthedocs.io/en/latest/registrationOverview.html

## Slide 44: Read every original graph and number

Chronological slide 44 of 86. Part III. Optional detail. Hidden during the normal forty-five-minute slideshow. Use for preparation or questions.

Purpose in ordinary words:
See how the computer chooses a candidate from many measured scores.

Demonstration:
Use unchanged shades. Search, inspect the chosen position, and compare it with the known answer.

What to notice:
The curve is one horizontal row of a two-dimensional search. Its vertical offset stays fixed.

Interpretation:
Use the same valid samples for fair candidate comparisons. Mutual information is explained in Part IV before its contrast search.

Matching combined-demo lesson: translation. Open chronological/demo/index.html#translation.

Next main slide: 46. Translation-component error: the slide part only.

Full discussion:
Imagine a large table of scores indexed by horizontal and vertical offset. The original search tries 81 horizontal values times 81 vertical values, for 6,561 candidates. The on-screen curve shows only the 81 horizontal values at the current selected y. Changing y selects a different row of the score table, so the displayed curve can change.

Read an orange marker as the current candidate, the blue curve as recorded scores, and the dashed vertical line as the known horizontal offset. A known xdoes not guarantee a correct two-dimensional position if yis wrong. MSE is minimized; signed NCC and MI are maximized under the chosen objectives. A positive score is not an accuracy percentage.

The cyan ROI is a region of interest: a chosen measurement area. In the original translation scan it covers 96by 96 pixels, but scores sample every other row and column, yielding 48 times 48=2,304 values for each candidate. The same samples prevent changing border fill from unfairly improving the score. MI groups brightness into 32bins before counting paired values; those are brightness groups, not 32spatial regions.

Runtime is seconds on this computer for that operation. Browser resolution 256by 256differs from the main old Python experiments 384by 384, so raw pixel errors and runtime should not be compared blindly.

Source context:
[8] Registration Overview. https://simpleitk.readthedocs.io/en/latest/registrationOverview.html
[9] Image Similarity and Tissue Overlaps as Surrogates for Image Registration Accuracy: Widely Used but Unreliable. https://pmc.ncbi.nlm.nih.gov/articles/PMC3274625/

Numbered sources:
[8] SimpleITK contributors (2026). Registration Overview. https://simpleitk.readthedocs.io/en/latest/registrationOverview.html
[9] Torsten Rohlfing (2012). Image Similarity and Tissue Overlaps as Surrogates for Image Registration Accuracy: Widely Used but Unreliable. https://pmc.ncbi.nlm.nih.gov/articles/PMC3274625/

## Slide 45: Subpixel translation and search precision

Chronological slide 45 of 86. Part III. Optional detail. Hidden during the normal forty-five-minute slideshow. Use for preparation or questions.

Next main slide: 46. Translation-component error: the slide part only.

Full discussion:
A pixel is one step on the image grid. A subpixel translation is a shift containing a fraction of that step, such as 5.4 pixels. Guizar-Sicairos and colleagues describe efficient refinement of a Fourier-domain registration estimate using a small local matrix-multiply discrete Fourier transform. The class uses scikit-image phase_cross_correlation, an established implementation linked to that method.

The researcher creates an exact known Fourier translation with periodic boundaries. Periodic means that content leaving one edge reappears at the opposite edge. This artificial boundary makes the controlled test especially clear and differs from an ordinary cropped photograph. The generated array-axis shift is (5.4, -3.7), so its correction is (-5.4, +3.7) in (row, column), also called (y, x), order.

An upsampling factor of ten refines the nominal translation grid to one tenth of a pixel. A factor of one hundred gives one hundredth. These describe numerical spacing. They do not promise that an unknown true movement is recovered within that spacing. The known generated correction provides the independent reference for translation-component error, measured in pixels.

The notebook also changes noise, hides a rectangle, and adds a small turn. The turned case violates the translation-only assumption. Its reported translation-component error does not summarize the remaining rotation or establish overall registration accuracy. The class does not reproduce the original paper's full complexity or performance comparison. The follow-up question tests a clear assumption rather than claiming a new unresolved problem.

Implementation detail: normalization=None selects ordinary Fourier cross-correlation. The library function is named phase_cross_correlation, but this run does not use phase-only normalization. Its local upsampled-DFT refinement is the reproduced core method.

Published study: Manuel Guizar-Sicairos, Samuel T. Thurman, James R. Fienup. Efficient subpixel image registration algorithms (2008).
Primary source: https://doi.org/10.1364/OL.33.000156

What the paper contributes:
The paper develops efficient 2D translation-registration algorithms, including local matrix-multiply DFT refinement, with accuracy comparable to conventional FFT upsampling at lower computation and memory cost in the reported experiments.

Evidence locations:
p. 156, opening paragraphs and Eqs. (1)-(3): Translation-only formulation, normalized reconstruction error, and Fourier-domain cross-correlation.
p. 157, single-step/two-step DFT descriptions and Fig. 1: Local upsampled-DFT refinement and explicit statement that noise ultimately limits registration accuracy.
p. 158, closing discussion and Fig. 2: Original hardware-specific timings; phase correlation and window functions are described as extensions.

Published limitation or scope boundary:
The problem is translation registration; p. 157 explicitly identifies noise as an eventual accuracy limit. The paper discusses phase correlation and windowing as extensions, so an implementation using those settings must be labeled accordingly.
Evidence location: p. 156, opening scope; p. 157, Fig. 1 discussion; p. 158, closing discussion

Classroom adaptation:
Use a periodic Fourier-generated fractional translation, upsampling factors 1, 10, and 100, and the public scikit-image implementation with normalization=None. Compare clean, noisy, occluded, and extra-rotation cases. In the rotation-violating case, the reported scalar checks the translation component only; it is not a measure of complete geometric recovery.

What this experiment does not reproduce:
All three original algorithms and their complete optimization comparisons
Original hardware timings or memory benchmarks
General rotation, scale, deformation, or clinical registration

Follow-up question for this class:
Does increasing the upsampling factor always reduce the measured translation error?

Supported conclusion:
How numerical refinement behaves for these constructed fractional translations and preprocessing settings.

Boundary on the conclusion:
That 1/upsample_factor pixels is guaranteed accuracy, or that original runtime advantages have been reproduced.

The classroom question does not carry a claim of novel or currently unsolved research.

Numbered sources:
[5] Manuel Guizar-Sicairos, Samuel T. Thurman, and James R. Fienup (2008). Efficient subpixel image registration algorithms. https://doi.org/10.1364/OL.33.000156

## Slide 46: Translation-component error: the slide part only

Chronological slide 46 of 86. Part III. Main route. Planned 1.11 minutes including the selected demonstration.

Purpose in ordinary words:
Explain the 0.500-pixel R3 result using across and down gaps.

Demonstration:
Compare returned correction (y,x)=(-5,+4) with known (-5.4,+3.7). Move the candidate sliders.

What to notice:
The component gaps are +0.4 down and +0.3 across. sqrt(0.4²+0.3²)=0.5 pixels.

Interpretation:
This checks the slide part. It does not measure a remaining turn or the full transformed image.

Matching combined-demo lesson: translation-error. Open chronological/demo/index.html#translation-error.

Next main slide: 47. Search spacing and recovery error.

45-minute spoken route (one worked case; the longer discussion is for preparation):
Translation means slide. Compare the known and returned slide answers: they differ by 0.4 down and 0.3 across. Squaring, adding and taking a root gives half a pixel. This number checks only the slide part. It does not check whether a turn was fixed.

Full discussion:
Purpose: explain the exact 0.500 entry in the recorded R3 clean, factor-one run. Translation means a slide across and down, without a turn or size change. A component is one part of a movement. Here translation-component error checks only the returned slide components. The known correction is (y,x)=(-5.4,+3.7) pixels. The recorded whole-pixel answer is (-5,+4). Subtract known from returned: -5-(-5.4)=+0.4 down and 4-3.7=+0.3 across. Square each gap, add, and take the square root: sqrt(0.16+0.09)=sqrt(0.25)=0.5 pixels. This is the straight-line distance between two slide answers, not an average brightness mismatch. A half-pixel error means half of one grid step in this displacement space.

The routine prints row then column, or y then x. Other tables print x then y, so always read the labels. The returned numbers are corrections, which undo the generated shift. A finer numerical grid permits a more precise answer but does not guarantee correctness. The rotated trial also contains a turn. Its reported translation-component error does not measure the full residual geometry caused by that turn. Use unused known positions to check a complete transformation. The browser sliders change a supplied candidate for learning the ruler; the research selector separately displays actual saved CPU results.

Numbered sources:
[5] Manuel Guizar-Sicairos, Samuel T. Thurman, and James R. Fienup (2008). Efficient subpixel image registration algorithms. https://doi.org/10.1364/OL.33.000156
[6] scikit-image contributors (2026). skimage.registration: phase_cross_correlation. https://scikit-image.org/docs/stable/api/skimage.registration.html

## Slide 47: Search spacing and recovery error

Chronological slide 47 of 86. Part III. Main route. Planned 1.21 minutes including the selected demonstration.

Purpose in ordinary words:
Inspect subpixel refinement based on Guizar-Sicairos et al. [5].

Demonstration:
Compare factors 1, 10 and 100, then try a recorded noisy, covered or rotated condition.

What to notice:
Factor 100 permits a 0.01-pixel grid. It is not proof of 0.01-pixel accuracy.

Interpretation:
This saved run uses ordinary Fourier cross-correlation with local DFT refinement; rotation challenges a translation-only model.

Matching combined-demo lesson: R3. Open chronological/demo/index.html#R3.

Next main slide: 48. Part IV. What if the shades change?.

Full discussion:
Purpose: understand subpixel precision without assuming that a finer numeric grid guarantees correctness. A pixel is one grid square. Subpixel means a fraction of a pixel. The Fourier cross-correlation procedure efficiently asks which slide makes the patterns agree, then uses a small locally refined calculation. No Fourier derivation is required for this lesson. Factor ten permits tenth-pixel steps; factor one hundred permits hundredth-pixel steps. Compare those grid steps with the measured error in the saved rows. In a clean controlled shift, refinement helps. Noise, missing content and especially a turn can limit recovery. A translation-only method cannot undo a turn. The source is Guizar-Sicairos and colleagues [5]. This implementation sets normalization=None: it uses ordinary Fourier cross-correlation, despite the library function’s name phase_cross_correlation.

Expanded explanation and source context:
A pixel is one step on the image grid. A subpixel translation is a shift containing a fraction of that step, such as 5.4 pixels. Guizar-Sicairos and colleagues describe efficient refinement of a Fourier-domain registration estimate using a small local matrix-multiply discrete Fourier transform. The class uses scikit-image phase_cross_correlation, an established implementation linked to that method.

The researcher creates an exact known Fourier translation with periodic boundaries. Periodic means that content leaving one edge reappears at the opposite edge. This artificial boundary makes the controlled test especially clear and differs from an ordinary cropped photograph. The generated array-axis shift is (5.4, -3.7), so its correction is (-5.4, +3.7) in (row, column), also called (y, x), order.

An upsampling factor of ten refines the nominal translation grid to one tenth of a pixel. A factor of one hundred gives one hundredth. These describe numerical spacing. They do not promise that an unknown true movement is recovered within that spacing. The known generated correction provides the independent reference for translation-component error, measured in pixels.

The notebook also changes noise, hides a rectangle, and adds a small turn. The turned case violates the translation-only assumption. Its reported translation-component error does not summarize the remaining rotation or establish overall registration accuracy. The class does not reproduce the original paper's full complexity or performance comparison. The follow-up question tests a clear assumption rather than claiming a new unresolved problem.

Implementation detail: normalization=None selects ordinary Fourier cross-correlation. The library function is named phase_cross_correlation, but this run does not use phase-only normalization. Its local upsampled-DFT refinement is the reproduced core method.

Published study: Manuel Guizar-Sicairos, Samuel T. Thurman, James R. Fienup. Efficient subpixel image registration algorithms (2008).
Primary source: https://doi.org/10.1364/OL.33.000156

What the paper contributes:
The paper develops efficient 2D translation-registration algorithms, including local matrix-multiply DFT refinement, with accuracy comparable to conventional FFT upsampling at lower computation and memory cost in the reported experiments.

Evidence locations:
p. 156, opening paragraphs and Eqs. (1)-(3): Translation-only formulation, normalized reconstruction error, and Fourier-domain cross-correlation.
p. 157, single-step/two-step DFT descriptions and Fig. 1: Local upsampled-DFT refinement and explicit statement that noise ultimately limits registration accuracy.
p. 158, closing discussion and Fig. 2: Original hardware-specific timings; phase correlation and window functions are described as extensions.

Published limitation or scope boundary:
The problem is translation registration; p. 157 explicitly identifies noise as an eventual accuracy limit. The paper discusses phase correlation and windowing as extensions, so an implementation using those settings must be labeled accordingly.
Evidence location: p. 156, opening scope; p. 157, Fig. 1 discussion; p. 158, closing discussion

Classroom adaptation:
Use a periodic Fourier-generated fractional translation, upsampling factors 1, 10, and 100, and the public scikit-image implementation with normalization=None. Compare clean, noisy, occluded, and extra-rotation cases. In the rotation-violating case, the reported scalar checks the translation component only; it is not a measure of complete geometric recovery.

What this experiment does not reproduce:
All three original algorithms and their complete optimization comparisons
Original hardware timings or memory benchmarks
General rotation, scale, deformation, or clinical registration

Follow-up question for this class:
Does increasing the upsampling factor always reduce the measured translation error?

Supported conclusion:
How numerical refinement behaves for these constructed fractional translations and preprocessing settings.

Boundary on the conclusion:
That 1/upsample_factor pixels is guaranteed accuracy, or that original runtime advantages have been reproduced.

The classroom question does not carry a claim of novel or currently unsolved research.

Purpose of this experiment:
Separate numerical search spacing from measured recovery accuracy and the transform model's assumptions.

Recorded settings:
256 px periodic Fourier shift; upsample 1/10/100; clean, noise sigma 0.03, occlusion, extra 5-degree rotation.

Interpretation of the measured rows:
The clean decimal shift is exactly represented on a 0.1 px grid; the rotated condition remains wrong on a 0.01 px grid.

Limits of this classroom run:
Periodic boundary; one image and noise draw. Rotated-case error measures the translation component, not full geometric alignment.

Read the condition first, name the measurement and its unit, and compare it with the known generated answer. Full raw measurements and figures are retained in the notebook and results files.

Numbered sources:
[5] Manuel Guizar-Sicairos, Samuel T. Thurman, and James R. Fienup (2008). Efficient subpixel image registration algorithms. https://doi.org/10.1364/OL.33.000156

## Slide 48: Part IV. What if the shades change?

Chronological slide 48 of 86. Part IV. Main route. Planned 0.3 minutes including the selected demonstration.

Purpose in ordinary words:
Line up pictures even when the same place has different shades.

Demonstration:
Read the question before touching any controls. Imagine the familiar example.

What to notice:
The same drawing can have dark shapes on white paper or white shapes on dark paper.

Interpretation:
Different kinds of images can show the same structures with different brightness rules.

Matching combined-demo lesson: purpose-IV. Open chronological/demo/index.html#purpose-IV.

Next main slide: 50. Inverted contrast: dark becomes bright.

Full discussion:
Begin with the familiar situation before naming the technical topic. The same drawing can have dark shapes on white paper or white shapes on dark paper. Line up pictures even when the same place has different shades. Different kinds of images can show the same structures with different brightness rules. Explain that this is the purpose of multimodal registration. Ask the audience to predict what useful evidence would look like. The following slides explain the unfamiliar labels before the experiment. At the end of the part, return to the question: Can one shade still give a useful clue about the other?

## Slide 49: Same contrast: keep the brightness rule

Chronological slide 49 of 86. Part IV. Optional detail. Hidden during the normal forty-five-minute slideshow. Use for preparation or questions.

Purpose in ordinary words:
Know exactly what the appearance options change before comparing methods.

Demonstration:
Trace 0, 0.25, 0.5, 0.75 and 1 through each brightness rule.

What to notice:
Same keeps v. Inverted gives 1−v. Nonlinear inverted gives 1−v^0.7, so middle shades change unequally.

Interpretation:
These rules alter shades, not the known geometry. They simulate a contrast relationship rather than a new medical acquisition.

Matching combined-demo lesson: contrast-rules. Open chronological/demo/index.html#contrast-rules.

Next main slide: 50. Inverted contrast: dark becomes bright.

Full discussion:
Contrast describes differences between light and dark values. In the original contrast dropdown, same contrast means the researcher leaves the original brightness mapping unchanged: the output value is v itself. It does not mean all pixels have the same brightness as one another, and it does not mean the two pictures are already aligned.

For example, a pixel with normalized brightness 0.25 remains 0.25 after the appearance rule. If the researcher separately moves the picture 20 pixels right, that value now lives at a different address. The brightness rule and spatial movement are separate operations.

Use the same-contrast mode first so the audience can see that comparing equal expected brightness is sensible for the constructed example. When the correct integer translation is undone and valid sampling support is used, corresponding values can agree exactly. More general resampling can still introduce differences.

Checkpoint: Does selecting same contrast reset the movement sliders to zero? Answer: No. It chooses the value rule. The known shift and candidate correction controls still determine the geometry.

## Slide 50: Inverted contrast: dark becomes bright

Chronological slide 50 of 86. Part IV. Main route. Planned 0.94 minutes including the selected demonstration.

Purpose in ordinary words:
Know exactly what the appearance options change before comparing methods.

Demonstration:
Trace 0, 0.25, 0.5, 0.75 and 1 through each brightness rule.

What to notice:
Same keeps v. Inverted gives 1−v. Nonlinear inverted gives 1−v^0.7, so middle shades change unequally.

Interpretation:
These rules alter shades, not the known geometry. They simulate a contrast relationship rather than a new medical acquisition.

Matching combined-demo lesson: contrast-rules. Open chronological/demo/index.html#contrast-rules.

Next main slide: 51. Nonlinear inverted contrast: unequal changes.

Full discussion:
Contrast here names the rule connecting input shades to output shades. Same contrast means keep each value v unchanged. Inverted contrast means new value equals one minus v on the zero-to-one scale: black becomes white, white becomes black, and halfway gray remains halfway gray. The photograph can still occupy a wrong position under either rule. The next lesson changes middle shades unevenly. All these examples are deliberately simulated brightness relationships. A modality is a type of acquisition, such as MRI or CT. The supplied T1-weighted and proton-density images are two contrasts within MRI, the same broad modality; an algebraic inversion does not create a CT scan or a new MRI acquisition.

Expanded explanation and source context:
Say: Invert means reverse this brightness scale. Subtract the old brightness value from one. A black zero becomes white one. A dark 0.25 becomes a lighter 0.75. A middle 0.5 stays 0.5. A light 0.75 becomes a darker 0.25.

This is a change of pixel values, not an instruction to flip the picture left-to-right or turn it upside down. The point addresses do not change merely because brightness was inverted. Any separately introduced translation still has to be corrected.

The same structures can therefore be aligned even though their brightness values are opposite. A direct squared-difference rule penalizes that mismatch. Signed NCC can be strongly negative at correct geometry because the brightness patterns vary oppositely. Mutual information can still find a statistical relationship, subject to its sampling and bin choices.

The researcher creates this inversion as a controlled lesson. It is not a real CT or MRI acquisition. Check the known geometry separately rather than treating any single similarity score as proof of correct position.

Source context:
[7] Alignment by Maximization of Mutual Information. https://doi.org/10.1023/A:1007958904918
[8] Registration Overview. https://simpleitk.readthedocs.io/en/latest/registrationOverview.html

Numbered sources:
[7] Paul Viola and William M. Wells III (1997). Alignment by Maximization of Mutual Information. https://doi.org/10.1023/A:1007958904918
[8] SimpleITK contributors (2026). Registration Overview. https://simpleitk.readthedocs.io/en/latest/registrationOverview.html

## Slide 51: Nonlinear inverted contrast: unequal changes

Chronological slide 51 of 86. Part IV. Main route. Planned 0.94 minutes including the selected demonstration.

Purpose in ordinary words:
Know exactly what the appearance options change before comparing methods.

Demonstration:
Trace 0, 0.25, 0.5, 0.75 and 1 through each brightness rule.

What to notice:
Same keeps v. Inverted gives 1−v. Nonlinear inverted gives 1−v^0.7, so middle shades change unequally.

Interpretation:
These rules alter shades, not the known geometry. They simulate a contrast relationship rather than a new medical acquisition.

Matching combined-demo lesson: contrast-rules. Open chronological/demo/index.html#contrast-rules.

Next main slide: 54. MI calculation: turn four counts into fractions.

Full discussion:
First explain linear versus nonlinear without requiring a graph formula. A straight brightness rule changes values at a constant rate. A curved rule changes different parts of the brightness range at different rates. Nonlinear refers to that curved relationship.

The original browser specifically computes one minus v to the power 0.7. Read the parentheses carefully:1 − (v^0.7). For an old brightness 0.25, the result is approximately 0.621. For 0.5, it is approximately 0.384. Plain inversion would give 0.75 and 0.5 instead. The endpoints still exchange: zero becomes one and one becomes zero.

Use a gray ramp containing several middle shades. A picture containing only zeros and ones cannot show the difference between these two particular reversal rules, since both map the endpoints identically. This was one reason the earlier binary-only lesson was insufficient.

The locations remain unchanged by this value operation. The original Python paper experiment used a different remapping,(1 − v)^0.65, which must not be presented as this exact browser rule. The new complete notebook reproduces the browser's formula and labels the constructed example explicitly.

Source context:
[7] Alignment by Maximization of Mutual Information. https://doi.org/10.1023/A:1007958904918
[8] Registration Overview. https://simpleitk.readthedocs.io/en/latest/registrationOverview.html

Numbered sources:
[7] Paul Viola and William M. Wells III (1997). Alignment by Maximization of Mutual Information. https://doi.org/10.1023/A:1007958904918
[8] SimpleITK contributors (2026). Registration Overview. https://simpleitk.readthedocs.io/en/latest/registrationOverview.html

## Slide 52: MI step 1: count pairs in a table

Chronological slide 52 of 86. Part IV. Optional detail. Hidden during the normal forty-five-minute slideshow. Use for preparation or questions.

Purpose in ordinary words:
Learn mutual information through small counts before a decimal score.

Demonstration:
Count matching value pairs. Compare same, reversed and unhelpful clues.

What to notice:
Both the same and reversed two-value rules can be useful clues. In this balanced toy, useful clues give ln(2), about 0.693 nats.

Interpretation:
MI uses paired-value probabilities. Its scale depends on bins and samples and is not an accuracy percentage.

Matching combined-demo lesson: mi. Open chronological/demo/index.html#mi.

Next main slide: 54. MI calculation: turn four counts into fractions.

Full discussion:
MI means mutual information. Its purpose is to measure how useful one brightness value is as a clue about the other. Start with four paired addresses, not a decimal score. A joint histogram is a count table: row says the first value, column says the second value, cell says how often that pair occurred. Bins are brightness groups used to form such counts for real-valued images. They are not spatial boxes. In the balanced two-label toy, knowing the first label perfectly predicts the second under both same and reversed rules. In the unhelpful toy, either second label remains equally possible. Probabilities are counts divided by the total number of pairs. The logarithm convention names the unit: natural logarithms give nats.

Expanded explanation and source context:
Start with four paired values. The fixed list is[0,0,1,1], and the same-pattern moving list is[0,0,1,1]. There are two (0,0)pairs and two (1,1)pairs. Put the first value along the row label and the second along the column label. Write the counts in the matching cells.

This is a joint count table. Joint simply means we count two things together. In images with many brightness levels, nearby values are grouped into bins. A histogram is a count of values in bins. A joint histogram counts paired bins.

Point at the cells, not a formula. Ask: When the fixed value is zero in this example, what moving value do we see? Answer: Zero. When fixed is one, moving is one. The relationship is predictable.

Make clear that this tiny table uses two possible values and four pairs. It is a constructed teaching example, not a test on medical images. We keep all four pairs for every comparison so the table has a consistent sample count.

Source context:
[7] Alignment by Maximization of Mutual Information. https://doi.org/10.1023/A:1007958904918
[8] Registration Overview. https://simpleitk.readthedocs.io/en/latest/registrationOverview.html

Numbered sources:
[7] Paul Viola and William M. Wells III (1997). Alignment by Maximization of Mutual Information. https://doi.org/10.1023/A:1007958904918
[8] SimpleITK contributors (2026). Registration Overview. https://simpleitk.readthedocs.io/en/latest/registrationOverview.html

## Slide 53: MI step 2: a useful clue

Chronological slide 53 of 86. Part IV. Optional detail. Hidden during the normal forty-five-minute slideshow. Use for preparation or questions.

Purpose in ordinary words:
Learn mutual information through small counts before a decimal score.

Demonstration:
Count matching value pairs. Compare same, reversed and unhelpful clues.

What to notice:
Both the same and reversed two-value rules can be useful clues. In this balanced toy, useful clues give ln(2), about 0.693 nats.

Interpretation:
MI uses paired-value probabilities. Its scale depends on bins and samples and is not an accuracy percentage.

Matching combined-demo lesson: mi. Open chronological/demo/index.html#mi.

Next main slide: 54. MI calculation: turn four counts into fractions.

Full discussion:
In the balanced two-value teaching example, a perfectly useful clue gives ln(2), approximately 0.693 nats. Both a same-label rule and a reversed-label rule can give that value. An unhelpful clue gives zero here. The number is not 69.3 percent accuracy and 0.693 is not a universal maximum for real images. MI depends on the bins, samples and their estimated paired probabilities. Histogram MI can be large for a consistent nonlinear relationship. It still does not establish that a repeated structure has the correct identity. Compare known positions separately.

Expanded explanation and source context:
Now reverse the moving list to[1,1,0,0]. Every fixed zero now predicts moving one, and every fixed one predicts moving zero. The relationship is opposite, but still perfectly predictable in this tiny table. Mutual information, or MI, measures the reduction in uncertainty from knowing the paired value. Call it how useful one value is as a clue before introducing the technical term.

For the mixed list[0,1,0,1], knowing that fixed is zero leaves both moving values equally possible. The same is true when fixed is one. The clue provides no help in this constructed independent table, so MI is zero.

The same and reversed tables both give ln(2), approximately 0.693 nats, when using the natural logarithm. A nat is a unit for this information calculation. The formula is optional. The value 0.693 is the maximum only for this balanced two-value construction. It is not a universal target for real images.

MI is not a percentage and does not guarantee geometric truth. Bin choices, samples, image content, and overlap can affect it.

For this optional number, ln is the natural-log operation on a calculator. The main lesson needs only the equal-clue versus no-clue comparison; the detailed calculation is in the learning guide.

Source context:
[7] Alignment by Maximization of Mutual Information. https://doi.org/10.1023/A:1007958904918
[8] Registration Overview. https://simpleitk.readthedocs.io/en/latest/registrationOverview.html

Numbered sources:
[7] Paul Viola and William M. Wells III (1997). Alignment by Maximization of Mutual Information. https://doi.org/10.1023/A:1007958904918
[8] SimpleITK contributors (2026). Registration Overview. https://simpleitk.readthedocs.io/en/latest/registrationOverview.html

## Slide 54: MI calculation: turn four counts into fractions

Chronological slide 54 of 86. Part IV. Main route. Planned 1.26 minutes including the selected demonstration.

Purpose in ordinary words:
Turn the useful-clue story into a number without skipping the arithmetic.

Demonstration:
Count four pairs, divide by four, compare each actual fraction with its no-clue product, then add weighted ln terms.

What to notice:
0.5 × ln(0.5/0.25) + 0.5 × ln(0.5/0.25) = 0.6931 nats. ln is the natural-log calculator button.

Interpretation:
MI measures paired-label dependence. It can help when corresponding structures have different shades, but it is not position accuracy.

Matching combined-demo lesson: mi-calculation. Open chronological/demo/index.html#mi-calculation.

Next main slide: 55. MI calculation: weight the clues, then add.

45-minute spoken route (one worked case; the longer discussion is for preparation):
We counted four pairs. Divide each count by four. Half the first labels are zero, and half the second labels are zero. With no clue, half of a half predicts one quarter of pairs would be zero-zero. We actually saw one half. That useful difference is what MI measures.

Full discussion:
MI means mutual information. Its purpose is to ask how useful one brightness label is as a clue to its partner. Use the same four addresses throughout: first values [0,0,1,1], second values [0,0,1,1]. We observed two (0,0) pairs, two (1,1) pairs and no mixed pairs. A count table for paired labels is called a joint histogram. Divide each cell count by four to obtain its joint probability, meaning the fraction of all paired addresses in that cell. The two nonempty cells each have probability 0.5. Add along a row or column to get a marginal probability: the fraction for one image without considering its partner. Both labels have marginal fraction 0.5 in each image.

If the first label supplied no clue to the second, the expected fraction of (0,0) pairs would be 0.5 times 0.5, or 0.25. The actual fraction is 0.5, twice as large. MI compares these actual joint fractions with the no-clue prediction, then weights each comparison by how often that pair actually occurs. The next slide performs that arithmetic. Bins are the brightness-label groups used for counting real images. These two toy labels are not spatial rectangles or percentages of correct registration. A consistent reversed rule can be just as informative as the same-label rule.

Numbered sources:
[7] Paul Viola and William M. Wells III (1997). Alignment by Maximization of Mutual Information. https://doi.org/10.1023/A:1007958904918
[8] SimpleITK contributors (2026). Registration Overview. https://simpleitk.readthedocs.io/en/latest/registrationOverview.html

## Slide 55: MI calculation: weight the clues, then add

Chronological slide 55 of 86. Part IV. Main route. Planned 1.52 minutes including the selected demonstration.

Purpose in ordinary words:
Turn the useful-clue story into a number without skipping the arithmetic.

Demonstration:
Count four pairs, divide by four, compare each actual fraction with its no-clue product, then add weighted ln terms.

What to notice:
0.5 × ln(0.5/0.25) + 0.5 × ln(0.5/0.25) = 0.6931 nats. ln is the natural-log calculator button.

Interpretation:
MI measures paired-label dependence. It can help when corresponding structures have different shades, but it is not position accuracy.

Matching combined-demo lesson: mi-calculation. Open chronological/demo/index.html#mi-calculation.

Next main slide: 58. Known-offset error: how far was the chosen answer off?.

45-minute spoken route (one worked case; the longer discussion is for preparation):
The actual fraction is twice the no-clue prediction. Press ln of two on a calculator, then multiply by the fraction one half. Do that for each of the two observed pair types and add. MI is about 0.693 nats. A reversed but predictable rule gives the same useful clue.

Full discussion:
Continue the same four-pair example. The formula is MI = sum over observed cells of p(first,second) times ln[p(first,second)/(p(first)p(second))]. Read p as a fraction and sum as add. The actual joint fraction p(first,second) is 0.5 for each nonempty cell. The no-clue product p(first)p(second) is 0.25. Their ratio is two. ln is the natural-logarithm calculator button. Only two button values are needed for this example: ln(1)=0 and ln(2) is about 0.693147. A ratio of one gives no extra clue relative to the no-clue prediction. The natural-log convention gives information units named nats. Multiply ln(2) by the actual fraction 0.5 to get about 0.346574 for each of the two observed cells. Add to get about 0.693147 nats. Empty cells contribute zero and are skipped rather than dividing by zero.

For the independent four-pair example [(0,0),(0,1),(1,0),(1,1)], every joint cell is 0.25 and every no-clue product is also 0.25. Every ratio is one, every log term is zero, and MI is zero. For a consistent reversed rule, the nonempty cells move to the other diagonal and MI remains about 0.693147. In this balanced two-label toy that is the largest possible MI. It is not a universal real-image ceiling, an accuracy percentage or a positional distance.

Use MI when corresponding structures can have a useful statistical brightness relationship without equal shades. In registration the search tries several movements and seeks high MI on comparable valid samples. Histograms, bins, samples and repeated structures affect the score. A high MI does not establish correct point identity. The later known-offset and independent-point lessons check that separately.

Numbered sources:
[7] Paul Viola and William M. Wells III (1997). Alignment by Maximization of Mutual Information. https://doi.org/10.1023/A:1007958904918
[8] SimpleITK contributors (2026). Registration Overview. https://simpleitk.readthedocs.io/en/latest/registrationOverview.html

## Slide 56: Three rules, three questions

Chronological slide 56 of 86. Part IV. Optional detail. Hidden during the normal forty-five-minute slideshow. Use for preparation or questions.

Purpose in ordinary words:
Learn mutual information through small counts before a decimal score.

Demonstration:
Count matching value pairs. Compare same, reversed and unhelpful clues.

What to notice:
Both the same and reversed two-value rules can be useful clues. In this balanced toy, useful clues give ln(2), about 0.693 nats.

Interpretation:
MI uses paired-value probabilities. Its scale depends on bins and samples and is not an accuracy percentage.

Matching combined-demo lesson: mi. Open chronological/demo/index.html#mi.

Next main slide: 58. Known-offset error: how far was the chosen answer off?.

Full discussion:
Use the comparison table as a translation dictionary. MSE compares exact brightness differences and prefers a smaller average square. Signed NCC compares centered linear patterns and prefers a larger signed score when maximized. MI compares dependence in paired-value counts and prefers a larger information value within the same defined measurement procedure.

Ask the learner to explain each rule without using its abbreviation. If the answer is simply more accurate, return to the worked example. A score has to name the property it measures. It is not a universal measure of correctness.

Ask: Which rules treat a reversed pattern differently? Answer: The signed NCC example becomes minus one, while MI can stay high because the inverse relationship is predictable. MSE penalizes the unequal values. These observations describe this controlled example, not a universal competition between algorithms.

The next step is to try several moves and put each recorded score on a graph. The rule stays fixed while the candidate correction changes.

Source context:
[7] Alignment by Maximization of Mutual Information. https://doi.org/10.1023/A:1007958904918
[8] Registration Overview. https://simpleitk.readthedocs.io/en/latest/registrationOverview.html

Numbered sources:
[7] Paul Viola and William M. Wells III (1997). Alignment by Maximization of Mutual Information. https://doi.org/10.1023/A:1007958904918
[8] SimpleITK contributors (2026). Registration Overview. https://simpleitk.readthedocs.io/en/latest/registrationOverview.html

## Slide 57: Mutual information and changed brightness

Chronological slide 57 of 86. Part IV. Optional detail. Hidden during the normal forty-five-minute slideshow. Use for preparation or questions.

Next main slide: 58. Known-offset error: how far was the chosen answer off?.

Full discussion:
Mutual information measures how informative one paired value is about the other. The class begins with the existing counted-pair lesson. Here it uses a public photograph with a known generated shift. Same contrast keeps a normalized value v, inversion changes it to 1-v, and nonlinear inversion changes it to 1-(v raised to 0.7). These rules change brightness, while the known spatial movement remains separately controlled.

Viola and Wells established an alignment approach based on mutual information. This classroom experiment adapts the metric idea. It uses a thirty-two-bin histogram and an exhaustive bounded integer translation search. It does not reproduce the paper's Parzen density estimation, stochastic optimization, or full multimodal/three-dimensional examples. This adaptation must remain explicit.

Every candidate uses the same valid reference region, containing 3,136 paired values. The search tests 441 two-dimensional integer sampling offsets. A source sampling offset tells the software where to read a value from the moving picture. The applied correction has the opposite sign. The correct offset is (+6, -4), corresponding to the point correction (-6, +4).

The table reports the positional error of the offset selected by each objective, in pixels. These table entries share a geometric unit even though the underlying objectives have different units: MSE uses squared brightness, NCC has no units, and natural-log MI uses nats. The researcher compares each selected answer with the known shift. This controlled appearance remapping does not create genuinely acquired MRI or CT modalities, and a single result does not establish that MI always succeeds.

Published study: Paul Viola, William M. Wells III. Alignment by Maximization of Mutual Information (1997).
Primary source: https://doi.org/10.1023/A:1007958904918

What the paper contributes:
Alignment can be formulated by maximizing statistical dependence between model and image intensities; the paper uses nonparametric density estimation and stochastic optimization and reports MRI and vision experiments.

Evidence locations:
pp. 143-144, Sections 4-5, especially Eq. (13): Mutual-information alignment formulation.
pp. 145-146, Sections 5.1-5.2.1: Parzen-window density estimation and a local stochastic maximization procedure, unlike the class histogram grid search.
p. 147, Section 6.1 and Fig. 8: Original PD/T2 double-echo MRI example, synthetic nonlinear intensity change, and acknowledgement that normalized correlation could work for the relatively similar original MRI pair.
pp. 150-151, Sections 6.3-6.3.1, Figs. 12-14: A single-view relation can be insufficient; the paper develops a multiview construction.

Published limitation or scope boundary:
The paper's single-view model can fail when the aligned model and image lack a consistent relationship; it then develops a multiview construction. Its local optimization also requires an initialization and has a finite capture range in the reported examples.
Evidence location: p. 150, Section 6.3, Figs. 12–13; p. 151, Section 6.3.1

Classroom adaptation:
Use a 96 x 96 public photograph, a known (+6, -4)-pixel forward displacement, and three explicitly simulated intensity rules: v, 1-v, and 1-v^0.7. Compare MSE, signed NCC, and 32-bin histogram MI at all 441 integer sampling offsets in [-10,10]^2 on the same 3,136 source-valid fixed pixels. Convert the selected sampling offset to the opposite-sign point correction.

What this experiment does not reproduce:
The original EMMA Parzen-density stochastic-gradient optimizer
Original MRI subjects, head models, or view-based recognition experiments
A clinical validation or a real CT/MRI acquisition from the remapped photograph

Follow-up question for this class:
Which tested contrast changes preserve enough statistical dependence for the bounded MI search to select the known correction?

Supported conclusion:
Whether the tested metric and search recover the introduced shift under each controlled remapping.

Boundary on the conclusion:
That MI always works across modalities, that the original optimizer has been replicated, or that simulated contrast represents a genuine medical acquisition.

The classroom question does not carry a claim of novel or currently unsolved research.

Numbered sources:
[7] Paul Viola and William M. Wells III (1997). Alignment by Maximization of Mutual Information. https://doi.org/10.1023/A:1007958904918

## Slide 58: Known-offset error: how far was the chosen answer off?

Chronological slide 58 of 86. Part IV. Main route. Planned 1.01 minutes including the selected demonstration.

Purpose in ordinary words:
Explain the error column in the contrast search.

Demonstration:
Subtract known (x,y)=(6,-4) from the chosen (10,10), then measure the straight-line gap.

What to notice:
The gaps are 4 across and 14 down, giving about 14.5602 pixels. The known answer itself gives zero.

Interpretation:
This geometric comparison is shared by MSE, NCC and MI even though their internal score units differ.

Matching combined-demo lesson: known-offset-error. Open chronological/demo/index.html#known-offset-error.

Next main slide: 59. Recovery after brightness inversion.

45-minute spoken route (one worked case; the longer discussion is for preparation):
The correct lookup is six across and minus four down. This saved MSE answer picked ten across and ten down. Subtract to get gaps four and fourteen. Their straight-line distance is 14.560 pixels. MI picked the known answer here, so its offset error is zero.

Full discussion:
Purpose: explain what the error column in the contrast experiment measures. An offset is an across-and-down instruction. In this experiment it says where to read the moving image while filling a fixed-image address. It is a sampling offset, not an applied content correction. The researcher deliberately generated the geometry, so the correct sampling offset is known: (x,y)=(+6,-4) pixels. The saved inverted-contrast MSE search chose (+10,+10). Subtract the known answer component by component: 10-6=4 across and 10-(-4)=14 down. The straight-line distance between these two candidate answers is sqrt(4 squared plus 14 squared), about 14.5602 pixels. This is known-offset error. It is not the MSE brightness value.

The saved MI search chose (+6,-4), giving component gaps zero and error zero. The saved signed-NCC answer is (-10,-10), whose gaps are (-16,-6) and distance sqrt(256+36), about 17.0880 pixels. The common geometric error column makes these chosen answers comparable even though their internal objective scores have different units. Every candidate uses the same 3,136 valid samples. Smaller known-offset error means closer to the supplied answer in this translation-only construction. Zero means this known offset was recovered; it does not establish all anatomy or a clinical tolerance. An applied correction has the opposite sign in this translation-only sampling convention. The new sliders let the learner supply a candidate and watch this ruler calculate; they do not rerun the saved search.

Numbered sources:
[7] Paul Viola and William M. Wells III (1997). Alignment by Maximization of Mutual Information. https://doi.org/10.1023/A:1007958904918
[8] SimpleITK contributors (2026). Registration Overview. https://simpleitk.readthedocs.io/en/latest/registrationOverview.html
[9] Torsten Rohlfing (2012). Image Similarity and Tissue Overlaps as Surrogates for Image Registration Accuracy: Widely Used but Unreliable. https://pmc.ncbi.nlm.nih.gov/articles/PMC3274625/

## Slide 59: Recovery after brightness inversion

Chronological slide 59 of 86. Part IV. Main route. Planned 2.31 minutes including the selected demonstration.

Purpose in ordinary words:
Investigate a multimodal-registration idea from Viola and Wells [7].

Demonstration:
Choose appearance and score, then read the saved selected offset and its known-answer error.

What to notice:
Every selected row is an executed Python result. All 441 candidates use the same valid central samples.

Interpretation:
The experiment uses histogram MI rather than reproducing the paper’s full estimator and optimizer. Simulated inversion differs from a real modality pair.

Matching combined-demo lesson: R4. Open chronological/demo/index.html#R4.

Next main slide: 60. Public MRI contrast example.

Full discussion:
Research connection [7], Viola and Wells (1997): use mutual information to align images with different intensity relationships. The researcher uses a simpler histogram-MI teaching adaptation, not the original paper’s full estimator and optimizer. Compare recorded searches after same, inverted and nonlinear inverted shades. All 441 candidate offsets use the same 3,136 valid central samples. The table reports geometric error of the chosen answer, in pixels, allowing the three score rules to share a check quantity despite having different objective units. MSE and signed NCC fail under the displayed inversion; MI selects the known offset in this controlled run. That does not establish a universal winner. The shaded photograph is a simulated appearance change, not a genuine medical acquisition.

Expanded explanation and source context:
Mutual information measures how informative one paired value is about the other. The class begins with the existing counted-pair lesson. Here it uses a public photograph with a known generated shift. Same contrast keeps a normalized value v, inversion changes it to 1-v, and nonlinear inversion changes it to 1-(v raised to 0.7). These rules change brightness, while the known spatial movement remains separately controlled.

Viola and Wells established an alignment approach based on mutual information. This classroom experiment adapts the metric idea. It uses a thirty-two-bin histogram and an exhaustive bounded integer translation search. It does not reproduce the paper's Parzen density estimation, stochastic optimization, or full multimodal/three-dimensional examples. This adaptation must remain explicit.

Every candidate uses the same valid reference region, containing 3,136 paired values. The search tests 441 two-dimensional integer sampling offsets. A source sampling offset tells the software where to read a value from the moving picture. The applied correction has the opposite sign. The correct offset is (+6, -4), corresponding to the point correction (-6, +4).

The table reports the positional error of the offset selected by each objective, in pixels. These table entries share a geometric unit even though the underlying objectives have different units: MSE uses squared brightness, NCC has no units, and natural-log MI uses nats. The researcher compares each selected answer with the known shift. This controlled appearance remapping does not create genuinely acquired MRI or CT modalities, and a single result does not establish that MI always succeeds.

Published study: Paul Viola, William M. Wells III. Alignment by Maximization of Mutual Information (1997).
Primary source: https://doi.org/10.1023/A:1007958904918

What the paper contributes:
Alignment can be formulated by maximizing statistical dependence between model and image intensities; the paper uses nonparametric density estimation and stochastic optimization and reports MRI and vision experiments.

Evidence locations:
pp. 143-144, Sections 4-5, especially Eq. (13): Mutual-information alignment formulation.
pp. 145-146, Sections 5.1-5.2.1: Parzen-window density estimation and a local stochastic maximization procedure, unlike the class histogram grid search.
p. 147, Section 6.1 and Fig. 8: Original PD/T2 double-echo MRI example, synthetic nonlinear intensity change, and acknowledgement that normalized correlation could work for the relatively similar original MRI pair.
pp. 150-151, Sections 6.3-6.3.1, Figs. 12-14: A single-view relation can be insufficient; the paper develops a multiview construction.

Published limitation or scope boundary:
The paper's single-view model can fail when the aligned model and image lack a consistent relationship; it then develops a multiview construction. Its local optimization also requires an initialization and has a finite capture range in the reported examples.
Evidence location: p. 150, Section 6.3, Figs. 12–13; p. 151, Section 6.3.1

Classroom adaptation:
Use a 96 x 96 public photograph, a known (+6, -4)-pixel forward displacement, and three explicitly simulated intensity rules: v, 1-v, and 1-v^0.7. Compare MSE, signed NCC, and 32-bin histogram MI at all 441 integer sampling offsets in [-10,10]^2 on the same 3,136 source-valid fixed pixels. Convert the selected sampling offset to the opposite-sign point correction.

What this experiment does not reproduce:
The original EMMA Parzen-density stochastic-gradient optimizer
Original MRI subjects, head models, or view-based recognition experiments
A clinical validation or a real CT/MRI acquisition from the remapped photograph

Follow-up question for this class:
Which tested contrast changes preserve enough statistical dependence for the bounded MI search to select the known correction?

Supported conclusion:
Whether the tested metric and search recover the introduced shift under each controlled remapping.

Boundary on the conclusion:
That MI always works across modalities, that the original optimizer has been replicated, or that simulated contrast represents a genuine medical acquisition.

The classroom question does not carry a claim of novel or currently unsolved research.

Purpose of this experiment:
Check why equal brightness and statistical dependence are different registration objectives.

Recorded settings:
32-bin histogram MI; 441 integer (x,y) candidates; same, v->1-v, v->1-v^0.7; 96 px photo.

Interpretation of the measured rows:
MI recovered the known integer shift in all three appearances. Signed NCC and MSE chose wrong shifts after inversion.

Limits of this classroom run:
Teaching adaptation, not Viola/Wells Parzen estimation or optimizer; simulated contrasts are not acquired modalities; bounded translation only.

Read the condition first, name the measurement and its unit, and compare it with the known generated answer. Full raw measurements and figures are retained in the notebook and results files.

Numbered sources:
[7] Paul Viola and William M. Wells III (1997). Alignment by Maximization of Mutual Information. https://doi.org/10.1023/A:1007958904918

## Slide 60: Public MRI contrast example

Chronological slide 60 of 86. Part IV. Main route. Planned 0.94 minutes including the selected demonstration.

Purpose in ordinary words:
Separate the genuine input pictures from the artificially added movement and the achieved recovery.

Demonstration:
Inspect the supplied T1/PD images, the added (+9,-6) move, and the recorded (-9,+6) undo.

What to notice:
All three methods recover the added shift: error falls from about 10.817 to 0 pixels relative to native optima.

Interpretation:
This is added-movement recovery on two real MRI contrasts. It does not prove original anatomical alignment or MI superiority.

Matching combined-demo lesson: mri-achievement. Open chronological/demo/index.html#mri-achievement.

Next main slide: 61. What did the public MRI experiment achieve?.

Full discussion:
The public ITK example supplies genuine T1-weighted and proton-density MRI teaching images. Their different T1/proton-density MRI contrast is supplied by the public teaching pair, rather than generated by the researcher’s contrast-remapping operation. Original acquisition provenance is not established by the example files. The source, downloaded files, and checksums are recorded with the data.

The researcher deliberately displaces one image and tests whether the estimated correction recovers the pair's original supplied coordinate relationship. This provides a known answer for the added displacement. It does not establish that the original pair has perfect anatomical alignment. The acquisition metadata and independent anatomical ground truth are not established by the repository files used here.

Read the introduced and recovered shift and the residual perturbation error from the actual executed output. Inspect the before/after views as a complementary check. If asked whether this proves the method is clinically accurate, answer that it is an educational demonstration of recovering an introduced perturbation in a public pair. Clinical accuracy would require calibrated spatial units, anatomical reference data, broader validation, and a defined clinical task. The notebook preserves this distinction explicitly.

In this executed pair, MSE, signed NCC, and MI all recover the deliberately added displacement. This example does not show that MI uniquely succeeds. Recovery is measured relative to the native optimum of each metric.

Working array is 221 by 257 pixels. Introduced displacement magnitude is 10.817 pixels. MI perturbation recovery error is 0.000 pixels.

Sources:
[8] Registration Overview. https://simpleitk.readthedocs.io/en/latest/registrationOverview.html
[11] ITK ImageRegistration2.cxx: T1 and proton-density MRI registration example. https://raw.githubusercontent.com/InsightSoftwareConsortium/ITK/main/Examples/RegistrationITKv4/ImageRegistration2.cxx
[12] ITK LICENSE. https://raw.githubusercontent.com/InsightSoftwareConsortium/ITK/main/LICENSE

Numbered sources:
[8] SimpleITK contributors (2026). Registration Overview. https://simpleitk.readthedocs.io/en/latest/registrationOverview.html
[11] Insight Software Consortium / ITK contributors (2026). ITK ImageRegistration2.cxx: T1 and proton-density MRI registration example. https://raw.githubusercontent.com/InsightSoftwareConsortium/ITK/main/Examples/RegistrationITKv4/ImageRegistration2.cxx
[12] Insight Software Consortium / NumFOCUS (2026). ITK LICENSE. https://raw.githubusercontent.com/InsightSoftwareConsortium/ITK/main/LICENSE

## Slide 61: What did the public MRI experiment achieve?

Chronological slide 61 of 86. Part IV. Main route. Planned 1.11 minutes including the selected demonstration.

Purpose in ordinary words:
Separate the genuine input pictures from the artificially added movement and the achieved recovery.

Demonstration:
Inspect the supplied T1/PD images, the added (+9,-6) move, and the recorded (-9,+6) undo.

What to notice:
All three methods recover the added shift: error falls from about 10.817 to 0 pixels relative to native optima.

Interpretation:
This is added-movement recovery on two real MRI contrasts. It does not prove original anatomical alignment or MI superiority.

Matching combined-demo lesson: mri-achievement. Open chronological/demo/index.html#mri-achievement.

Next main slide: 62. Part V. When should we doubt the evidence?.

45-minute spoken route (one worked case; the longer discussion is for preparation):
These are two real MRI contrasts. We added a known move of nine right and six up. All three methods recovered the opposite undo. The added-movement error became zero. Brightness MSE stayed above zero because the contrasts still have different shades. This checks our added movement, not original anatomical truth.

Full discussion:
Purpose: state the achievement and its boundary before treating the MRI picture as evidence. MRI is magnetic resonance imaging. T1-weighted and proton-density images emphasize tissue properties differently within the same broad MRI modality. They are genuine public teaching images with different MRI contrasts, not a photograph whose shades the researcher inverted. Their original acquisition metadata and independent anatomical ground truth are not established by the supplied files.

The researcher first searches the supplied pair without the extra perturbation. That per-method best offset is called the native optimum: the method’s best answer for the supplied pair under its sampling mask, not a certified anatomical answer. In these recorded runs, native optimum is (0,0) for MSE, signed NCC and MI. The researcher then deliberately slides the T1 image by (+9,-6) pixels in (x,y) order. Without undoing this added movement, its displacement magnitude is sqrt(9 squared plus 6 squared), about 10.816654 pixels. That is the magnitude of the introduced movement, not a measurement of the original pair’s anatomical misalignment.

Each method returns the perturbed optimum (-9,+6). Subtract its native optimum (0,0) to get the incremental correction, also (-9,+6). That exactly cancels the added shift. The added-perturbation recovery error is therefore zero pixels for each method. All compare the same 27,756 foreground locations within the stated central sampling region. The achievement is recovery of a known artificial movement on a genuine MRI contrast pair. It shows that the controlled test can extend beyond algebraically recoloring one image. It does not demonstrate that MI alone succeeds, that native anatomy was perfectly aligned, that every MRI pair will work, or that clinical accuracy has been established. The supplied methods tied on this particular added-shift check.

The same-mask brightness scores were additionally checked with the original CPU functions: MSE is approximately 0.157896 before the added shift is undone and 0.127777 afterward. Signed NCC rises from approximately 0.154482 to 0.334569. MI rises from approximately 0.078739 to 0.752974 nats. Those after-correction values match the supplied native-pair values in the recorded construction. Brightness MSE remains nonzero because T1 and proton-density contrasts show different shades. This is compatible with zero recovery error for the known added movement: the two measurements ask different questions.

Numbered sources:
[8] SimpleITK contributors (2026). Registration Overview. https://simpleitk.readthedocs.io/en/latest/registrationOverview.html
[11] Insight Software Consortium / ITK contributors (2026). ITK ImageRegistration2.cxx: T1 and proton-density MRI registration example. https://raw.githubusercontent.com/InsightSoftwareConsortium/ITK/main/Examples/RegistrationITKv4/ImageRegistration2.cxx
[12] Insight Software Consortium / NumFOCUS (2026). ITK LICENSE. https://raw.githubusercontent.com/InsightSoftwareConsortium/ITK/main/LICENSE

## Slide 62: Part V. When should we doubt the evidence?

Chronological slide 62 of 86. Part V. Main route. Planned 0.3 minutes including the selected demonstration.

Purpose in ordinary words:
Recognize weak or misleading evidence and choose a sensible sequence of steps.

Demonstration:
Read the question before touching any controls. Imagine the familiar example.

What to notice:
A tiny scrap of a repeated pattern may fit in several places.

Interpretation:
A method can return a number even when its evidence cannot identify a unique correct position.

Matching combined-demo lesson: purpose-V. Open chronological/demo/index.html#purpose-V.

Next main slide: 65. A useful order for solving the problem.

Full discussion:
Begin with the familiar situation before naming the technical topic. A tiny scrap of a repeated pattern may fit in several places. Recognize weak or misleading evidence and choose a sensible sequence of steps. A method can return a number even when its evidence cannot identify a unique correct position. Explain that this is the purpose of failure cases and workflow. Ask the audience to predict what useful evidence would look like. The following slides explain the unfamiliar labels before the experiment. At the end of the part, return to the question: Do the compared pictures contain enough trustworthy common content?

## Slide 63: Compare the same real picture area

Chronological slide 63 of 86. Part V. Optional detail. Hidden during the normal forty-five-minute slideshow. Use for preparation or questions.

Next main slide: 65. A useful order for solving the problem.

Full discussion:
Say: When a picture slides right, empty space may appear at the left border. The computer often fills that space with zero. That zero is a storage choice, not an observed dark object. Comparing those invented border values can change a score unfairly.

The teaching experiment marks a central region that remains supported by original picture content for every candidate correction. Each tried move uses the same reference cells and the same count. Common area means that shared valid support, not simply whichever area happens to give the best score.

Ask: Would a test be fair if one move could hide half the difficult picture? Answer: It would answer a different question. This controlled scan keeps the compared region constant so the score changes can be interpreted more clearly.

The notebook and browser document the exact limits used. The rule does not solve every field-of-view problem in real data. Its purpose is to prevent padded borders from winning this small experiment. The technical expression for those real compared cells is valid overlap or valid support.

Source context:
[8] Registration Overview. https://simpleitk.readthedocs.io/en/latest/registrationOverview.html

Numbered sources:
[8] SimpleITK contributors (2026). Registration Overview. https://simpleitk.readthedocs.io/en/latest/registrationOverview.html

## Slide 64: When the evidence is not enough

Chronological slide 64 of 86. Part V. Optional detail. Hidden during the normal forty-five-minute slideshow. Use for preparation or questions.

Next main slide: 65. A useful order for solving the problem.

Full discussion:
A demonstration should also explain when its clues are insufficient. If a picture repeats the same stripe every few pixels, several candidate moves may compare equally well. If all brightness values are constant, signed NCC cannot be calculated by its usual formula. A count or objective value cannot create missing spatial evidence.

For the point model, a group of wrong matches can agree on a coherent wrong translation. A large sigma or a badly chosen threshold can weaken useful consensus. A translation-only model cannot correct rotation or deformation. These are different failure causes and should not all be described as random bad luck.

Ask: What should the researcher do when the best candidates tie? Answer: Report the ambiguity and inspect other evidence or a better-suited model. Do not turn the first returned index into a certainty claim.

The source scripts retain raw candidates, votes, and settings so the explanation can be checked. A visible failure with a clear reason is a useful learning result.

Source context:
[9] Image Similarity and Tissue Overlaps as Surrogates for Image Registration Accuracy: Widely Used but Unreliable. https://pmc.ncbi.nlm.nih.gov/articles/PMC3274625/

Numbered sources:
[9] Torsten Rohlfing (2012). Image Similarity and Tissue Overlaps as Surrogates for Image Registration Accuracy: Widely Used but Unreliable. https://pmc.ncbi.nlm.nih.gov/articles/PMC3274625/

## Slide 65: A useful order for solving the problem

Chronological slide 65 of 86. Part V. Main route. Planned 0.66 minutes including the selected demonstration.

Next main slide: 67. NMI calculation starts with uncertainty.

Full discussion:
First inspect the pictures. Are they showing the same scene or anatomy? Do they have shared content? Choose a movement model simple enough for the problem, such as a slide, a turn, or a uniform size change. Next choose evidence: distinctive point pairs or a suitable brightness comparison. Work from a reasonable starting position and inspect the shared valid region. Then estimate a movement. Finally check known positions that did not help fit the movement. If the evidence is weak, returning a number does not create missing information. Repeated textures, large missing regions, blur and an inappropriate motion model can make the problem ambiguous. The researcher saves settings, the known movement, the selected answer, the check points and the limits so that the experiment can be repeated.

Numbered sources:
[1] Richard Szeliski (2004). Image Alignment and Stitching: A Tutorial. https://www.microsoft.com/en-us/research/publication/image-alignment-and-stitching-a-tutorial/
[8] SimpleITK contributors (2026). Registration Overview. https://simpleitk.readthedocs.io/en/latest/registrationOverview.html
[9] Torsten Rohlfing (2012). Image Similarity and Tissue Overlaps as Surrogates for Image Registration Accuracy: Widely Used but Unreliable. https://pmc.ncbi.nlm.nih.gov/articles/PMC3274625/

## Slide 66: NMI adjusts an information score

Chronological slide 66 of 86. Part V. Optional detail. Hidden during the normal forty-five-minute slideshow. Use for preparation or questions.

Next main slide: 67. NMI calculation starts with uncertainty.

Full discussion:
Begin with a bag of labeled counters. If every counter has the same label, the next label is certain, so entropy is zero. If several labels are possible, there is uncertainty. A joint label describes the first and second image values together at one paired address. Joint entropy measures uncertainty in those pairs. This is the first introduction to normalized mutual information, abbreviated NMI. The Studholme definition used here adds the two individual entropies and divides by joint entropy. All quantities use the same natural-log convention, so the units cancel in the ratio. NMI is not a percentage and has no universal accuracy cutoff. If both images are constant, joint entropy is zero and division is undefined. Explain this before showing the crop table. The purpose of normalization is to address sensitivity to common image area, but it does not guarantee that every crop produces the same score. The follow-up paper by Cahill and colleagues limits blanket overlap-invariance claims. The six-crop experiment is a classroom adaptation rather than a replication of medical acquisition conditions.

Numbered sources:
[15] Colin Studholme, Derek L. G. Hill, David J. Hawkes (1999). An overlap invariant entropy measure of 3D medical image alignment. https://doi.org/10.1016/S0031-3203(98)00091-0
[16] Nathan D. Cahill, Julia A. Schnabel, J. Alison Noble, David J. Hawkes (2008). Revisiting overlap invariance in medical image alignment. https://doi.org/10.1109/CVPRW.2008.4562989

## Slide 67: NMI calculation starts with uncertainty

Chronological slide 67 of 86. Part V. Main route. Planned 1.11 minutes including the selected demonstration.

Purpose in ordinary words:
Understand what NMI divides and why changing common image area motivates it.

Demonstration:
Calculate the two individual entropies and joint entropy from the same four pairs. Compare useful, unhelpful and constant cases.

What to notice:
Useful: (0.6931+0.6931)/0.6931=2. Unhelpful: 1. Both constant: 0/0 is undefined.

Interpretation:
This NMI is a unitless uncertainty ratio, not a percentage. It addresses overlap sensitivity without guaranteeing invariance.

Matching combined-demo lesson: nmi-calculation. Open chronological/demo/index.html#nmi-calculation.

Next main slide: 68. NMI: the same numbers, a different calculation.

45-minute spoken route (one worked case; the longer discussion is for preparation):
Entropy measures uncertainty in labels. For two equally likely labels, add two terms minus one half times ln of one half: about 0.693 nats. Two predictable pair types have that same joint uncertainty. Four equally possible pair types have twice as much: about 1.386 nats.

Full discussion:
Purpose: calculate the uncertainty quantities instead of leaving H as an unexplained letter. Entropy is uncertainty in a label before seeing it. A bag containing only label zero has no uncertainty. A balanced bag with zero and one has two equally possible outcomes. H is just the short name for entropy. To calculate it, take each nonempty label’s fraction p, calculate -p times ln(p), and add those amounts. Natural logarithms give nats, the same information unit used in MI. The natural-log calculator gives ln(0.5)=-0.693147. Multiplying by -0.5 makes about +0.346574, and the two labels add to about 0.693147 nats. Empty groups add zero.

Joint entropy applies the same recipe to paired labels. In the same or reversed four-pair example, there are two equally frequent pair types. Their joint entropy is about 0.693147. In the independent four-pair example, all four pair types occur with fraction 0.25. Add four terms -0.25 ln(0.25) to obtain ln(4), about 1.386294. The individual-image entropies are still 0.693147 each. The pair has more remaining uncertainty in the unhelpful case.

As a check, MI can also be calculated as first entropy plus second entropy minus joint entropy. The informative case gives 0.693147+0.693147-0.693147=0.693147. The independent case gives 0.693147+0.693147-1.386294=0. These agree with the earlier weighted-clue calculation. The next slide uses these same quantities in the selected NMI ratio.

Numbered sources:
[15] Colin Studholme, Derek L. G. Hill, David J. Hawkes (1999). An overlap invariant entropy measure of 3D medical image alignment. https://doi.org/10.1016/S0031-3203(98)00091-0
[16] Nathan D. Cahill, Julia A. Schnabel, J. Alison Noble, David J. Hawkes (2008). Revisiting overlap invariance in medical image alignment. https://doi.org/10.1109/CVPRW.2008.4562989

## Slide 68: NMI: the same numbers, a different calculation

Chronological slide 68 of 86. Part V. Main route. Planned 1.16 minutes including the selected demonstration.

Purpose in ordinary words:
Understand what NMI divides and why changing common image area motivates it.

Demonstration:
Calculate the two individual entropies and joint entropy from the same four pairs. Compare useful, unhelpful and constant cases.

What to notice:
Useful: (0.6931+0.6931)/0.6931=2. Unhelpful: 1. Both constant: 0/0 is undefined.

Interpretation:
This NMI is a unitless uncertainty ratio, not a percentage. It addresses overlap sensitivity without guaranteeing invariance.

Matching combined-demo lesson: nmi-calculation. Open chronological/demo/index.html#nmi-calculation.

Next main slide: 70. Information scores as the crop shrinks.

45-minute spoken route (one worked case; the longer discussion is for preparation):
This NMI adds the two individual uncertainties and divides by paired uncertainty. Our useful clue gives two; unhelpful pairings give one. Both constant inputs give zero divided by zero, which is undefined. NMI studies sensitivity to common image area. These values are ratios, not percentages of alignment accuracy.

Full discussion:
NMI means normalized mutual information. This lesson uses the Studholme definition: NMI=(H(first)+H(second))/H(first,second). Read the numerator as the two individual uncertainties added and the denominator as the uncertainty in paired labels. This is a different formula from ordinary MI, which subtracts joint entropy. The same name NMI is used for other normalizations in other software; a number can be compared only when the definition and sampling protocol match.

Use the exact unrounded entropies in calculation. For the useful same or reversed clue, (ln2+ln2)/ln2=2. For the independent four-pair case, (ln2+ln2)/ln4=1. Both constant images have zero individual and joint entropies, yielding 0/0, which is undefined. A program must not print zero or perfect accuracy for that division. For this exact definition and a valid joint distribution with positive joint entropy, the ratio lies between one and two. That mathematical bound also holds for a coherent empirical histogram, apart from rounding. Sample choices can still mislead alignment while the number stays inside that bound. Other NMI definitions can use different scales. Neither bound is an accuracy percentage or universal registration pass mark.

Use case: moving one picture across another can change the area of real content shared by both. The brightness distribution and sample count can then change as well as the alignment. Studholme and colleagues [15] proposed a normalized information criterion to address sensitivity to overlap. The crop experiment compares ordinary MI and this NMI while the common window shrinks. The later primary follow-up [16] limits claims that normalization guarantees invariance to every overlap change. The class does not prove NMI always beats MI or validates medical accuracy. Inspect geometry and adequate shared content separately. The original 1999 full text was not available in the verified source set; the accessible primary follow-up supplies the stated formula and scope caution.

Numbered sources:
[15] Colin Studholme, Derek L. G. Hill, David J. Hawkes (1999). An overlap invariant entropy measure of 3D medical image alignment. https://doi.org/10.1016/S0031-3203(98)00091-0
[16] Nathan D. Cahill, Julia A. Schnabel, J. Alison Noble, David J. Hawkes (2008). Revisiting overlap invariance in medical image alignment. https://doi.org/10.1109/CVPRW.2008.4562989

## Slide 69: Common image area and information scores

Chronological slide 69 of 86. Part V. Optional detail. Hidden during the normal forty-five-minute slideshow. Use for preparation or questions.

Next main slide: 70. Information scores as the crop shrinks.

Full discussion:
Overlap means the content present in both compared images. A crop removes part of a picture from the comparison. As a registration candidate changes, the overlap or distribution of compared shades can change too. A score can therefore change for reasons beyond whether structures line up.

Studholme and colleagues proposed normalized mutual information to address sensitivity to changing overlap. Entropy describes uncertainty in the counted brightness values. Joint entropy describes uncertainty in the paired values. The version used here divides the sum of the two individual entropies by their joint entropy. Ordinary MI uses natural-log information units called nats. This NMI ratio has no units. Their numerical magnitudes should not be compared as if they were the same score scale.

The researcher evaluates three sampling offsets and six widths of a common valid crop. The crop height stays ninety-six pixels. A known eight-pixel displacement separates the correct offset from the two deliberately wrong ones. The experiment records the actual paired sample count for every measurement. It is a controlled crop-sensitivity adaptation, not a full reproduction of the paper's medical acquisition conditions or a guarantee of exact overlap invariance.

If both inputs are constant, the joint entropy is zero. Dividing by zero is undefined, so the code reports an absent value with an explanation. A later primary paper by Cahill and colleagues revisits overlap invariance; its evidence limits blanket claims. The follow-up asks how scores behave in this chosen construction. It does not claim that NMI solves every partial-overlap problem or always beats MI.

Published study: Colin Studholme, Derek L. G. Hill, David J. Hawkes. An overlap invariant entropy measure of 3D medical image alignment (1999).
Primary source: https://doi.org/10.1016/S0031-3203(98)00091-0

What the paper contributes:
The paper introduces normalized mutual information to reduce sensitivity to changing image overlap in the registration setting it studies. Its title is not a guarantee that every empirical histogram, crop, or image pair will be invariant.

Evidence locations:
Original publisher/Crossref record: Pattern Recognition 32(1), pp. 71-86, DOI 10.1016/S0031-3203(98)00091-0: Exact original paper identity, authors, venue, date and contribution topic.
Cahill et al. (2008), PDF p. 1, abstract and Section 1; p. 2, Eq. (4): Attributes NMI to Studholme et al. and states the formula (H(A)+H(B))/H(A,B).
Cahill et al. (2008), PDF pp. 1-3, Section 2, Figs. 1-2: Published disc/ring counterexample where ordinary NMI is not overlap invariant.
Cahill et al. (2008), PDF p. 2, Section 3; p. 7, Section 6: Modified invariance claims require common-background-statistics assumptions; the authors identify broader initialization tests and assumption checks as future work at that time.

Published limitation or scope boundary:
The later primary analysis by Cahill et al. supplies a counterexample to universal overlap invariance of ordinary NMI. Its modified measures obtain invariance only under stated background-statistics assumptions. This is a published follow-up finding, not a quotation attributed to the 1999 authors.
Evidence location: Cahill et al. (2008), Section 2 and Figs. 1-2; Section 3 assumptions; Section 6 conclusions

Classroom adaptation:
Use a 128-pixel public photograph with a known horizontal sampling offset of 8 pixels. Evaluate only three offsets (0, 8, and 16 pixels) at six crop widths (96, 72, 48, 24, 12, and 6 pixels), using real source content and a 32-bin histogram. Record the sample count and MI/NMI at each crop. This is a three-candidate comparison, not a full registration search.

What this experiment does not reproduce:
The original 3D medical images and complete registration protocol
Original scanner, patient, or clinical accuracy results
A theorem guaranteeing successful alignment under arbitrary crop or overlap

Follow-up question for this class:
As crop width shrinks, do MI and NMI still score the known 8-pixel sampling offset above the two tested wrong offsets?

Supported conclusion:
How the score ordering of these three tested offsets changes across the chosen crops and sample counts.

Boundary on the conclusion:
That NMI always outperforms MI, that normalization creates missing information, or that a bounded class run reproduces the original medical benchmark.

The classroom question does not carry a claim of novel or currently unsolved research.

Numbered sources:
[15] Colin Studholme, Derek L. G. Hill, David J. Hawkes (1999). An overlap invariant entropy measure of 3D medical image alignment. https://doi.org/10.1016/S0031-3203(98)00091-0

## Slide 70: Information scores as the crop shrinks

Chronological slide 70 of 86. Part V. Main route. Planned 1.43 minutes including the selected demonstration.

Purpose in ordinary words:
Examine how crop content and sample count affect MI and NMI [15,16].

Demonstration:
Read the entropy explanation, then select a recorded crop width and compare offsets.

What to notice:
Entropy means uncertainty in labels. This NMI is (H(first)+H(second))/H(pair), a unitless ratio. Both compared images being constant makes its denominator zero.

Interpretation:
Normalization does not guarantee unchanged scores for every overlap change. These are six controlled crops, not a broad medical benchmark.

Matching combined-demo lesson: R5. Open chronological/demo/index.html#R5.

Next main slide: 71. Part VI. How do we check the answer fairly?.

Full discussion:
The preceding entropy lesson defines every new term before this table or crop selector. Research connection [15], Studholme and colleagues (1999), and the later scope caution [16], Cahill and colleagues (2008). Select one of six recorded crop widths, all ninety-six pixels high. There are three tried offsets, including the known correct one. Cropping changes both common content and sample count. Ordinary MI uses nats. This NMI ratio is dimensionless, so compare each score only on its own scale. A correct same-contrast construction can produce NMI two here, but this is not two hundred percent accuracy or a universal fixed maximum for every NMI definition. Both constant images make the joint entropy zero, so this formula is undefined. The original 1999 full text was not available in the verified source set; metadata and formula context are supported through the accessible primary follow-up. State that access boundary if discussing original-paper details. The class investigates controlled crop sensitivity, not a novel gap or a replicated medical benchmark.

Expanded explanation and source context:
Overlap means the content present in both compared images. A crop removes part of a picture from the comparison. As a registration candidate changes, the overlap or distribution of compared shades can change too. A score can therefore change for reasons beyond whether structures line up.

Studholme and colleagues proposed normalized mutual information to address sensitivity to changing overlap. Entropy describes uncertainty in the counted brightness values. Joint entropy describes uncertainty in the paired values. The version used here divides the sum of the two individual entropies by their joint entropy. Ordinary MI uses natural-log information units called nats. This NMI ratio has no units. Their numerical magnitudes should not be compared as if they were the same score scale.

The researcher evaluates three sampling offsets and six widths of a common valid crop. The crop height stays ninety-six pixels. A known eight-pixel displacement separates the correct offset from the two deliberately wrong ones. The experiment records the actual paired sample count for every measurement. It is a controlled crop-sensitivity adaptation, not a full reproduction of the paper's medical acquisition conditions or a guarantee of exact overlap invariance.

If both inputs are constant, the joint entropy is zero. Dividing by zero is undefined, so the code reports an absent value with an explanation. A later primary paper by Cahill and colleagues revisits overlap invariance; its evidence limits blanket claims. The follow-up asks how scores behave in this chosen construction. It does not claim that NMI solves every partial-overlap problem or always beats MI.

Published study: Colin Studholme, Derek L. G. Hill, David J. Hawkes. An overlap invariant entropy measure of 3D medical image alignment (1999).
Primary source: https://doi.org/10.1016/S0031-3203(98)00091-0

What the paper contributes:
The paper introduces normalized mutual information to reduce sensitivity to changing image overlap in the registration setting it studies. Its title is not a guarantee that every empirical histogram, crop, or image pair will be invariant.

Evidence locations:
Original publisher/Crossref record: Pattern Recognition 32(1), pp. 71-86, DOI 10.1016/S0031-3203(98)00091-0: Exact original paper identity, authors, venue, date and contribution topic.
Cahill et al. (2008), PDF p. 1, abstract and Section 1; p. 2, Eq. (4): Attributes NMI to Studholme et al. and states the formula (H(A)+H(B))/H(A,B).
Cahill et al. (2008), PDF pp. 1-3, Section 2, Figs. 1-2: Published disc/ring counterexample where ordinary NMI is not overlap invariant.
Cahill et al. (2008), PDF p. 2, Section 3; p. 7, Section 6: Modified invariance claims require common-background-statistics assumptions; the authors identify broader initialization tests and assumption checks as future work at that time.

Published limitation or scope boundary:
The later primary analysis by Cahill et al. supplies a counterexample to universal overlap invariance of ordinary NMI. Its modified measures obtain invariance only under stated background-statistics assumptions. This is a published follow-up finding, not a quotation attributed to the 1999 authors.
Evidence location: Cahill et al. (2008), Section 2 and Figs. 1-2; Section 3 assumptions; Section 6 conclusions

Classroom adaptation:
Use a 128-pixel public photograph with a known horizontal sampling offset of 8 pixels. Evaluate only three offsets (0, 8, and 16 pixels) at six crop widths (96, 72, 48, 24, 12, and 6 pixels), using real source content and a 32-bin histogram. Record the sample count and MI/NMI at each crop. This is a three-candidate comparison, not a full registration search.

What this experiment does not reproduce:
The original 3D medical images and complete registration protocol
Original scanner, patient, or clinical accuracy results
A theorem guaranteeing successful alignment under arbitrary crop or overlap

Follow-up question for this class:
As crop width shrinks, do MI and NMI still score the known 8-pixel sampling offset above the two tested wrong offsets?

Supported conclusion:
How the score ordering of these three tested offsets changes across the chosen crops and sample counts.

Boundary on the conclusion:
That NMI always outperforms MI, that normalization creates missing information, or that a bounded class run reproduces the original medical benchmark.

The classroom question does not carry a claim of novel or currently unsolved research.

Purpose of this experiment:
Observe ordinary and normalized information scores while the compared field of view narrows.

Recorded settings:
128 px camera; widths 96,72,48,24,12,6; height 96; correct offset 8 and wrong offsets 0/16; natural logarithms.

Interpretation of the measured rows:
Exact aligned equal values keep NMI=2 here while MI changes with crop content; wrong alignments also change. No universal advantage follows.

Limits of this classroom run:
A perfect same-contrast relation is an easy special case, not a 3-D multimodal replication or proof of overlap invariance. Crop size and content change together.

Read the condition first, name the measurement and its unit, and compare it with the known generated answer. Full raw measurements and figures are retained in the notebook and results files.

Numbered sources:
[15] Colin Studholme, Derek L. G. Hill, David J. Hawkes (1999). An overlap invariant entropy measure of 3D medical image alignment. https://doi.org/10.1016/S0031-3203(98)00091-0

## Slide 71: Part VI. How do we check the answer fairly?

Chronological slide 71 of 86. Part VI. Main route. Planned 0.3 minutes including the selected demonstration.

Purpose in ordinary words:
Check the chosen movement using separate known positions and explain what the numbers support.

Demonstration:
Read the question before touching any controls. Imagine the familiar example.

What to notice:
Check a practice answer with a fresh question that did not help produce it.

Interpretation:
A good-looking match or a good similarity score alone cannot certify correct geometry.

Matching combined-demo lesson: purpose-VI. Open chronological/demo/index.html#purpose-VI.

Next main slide: 73. Independent point error: measure, then average.

Full discussion:
Begin with the familiar situation before naming the technical topic. Check a practice answer with a fresh question that did not help produce it. Check the chosen movement using separate known positions and explain what the numbers support. A good-looking match or a good similarity score alone cannot certify correct geometry. Explain that this is the purpose of evaluation and interpretation. Ask the audience to predict what useful evidence would look like. The following slides explain the unfamiliar labels before the experiment. At the end of the part, return to the question: Did the method recover the known positions, and is that error acceptable for the stated task?

## Slide 72: Check with points that did not vote

Chronological slide 72 of 86. Part VI. Optional detail. Hidden during the normal forty-five-minute slideshow. Use for preparation or questions.

Purpose in ordinary words:
Check movement recovery using an independent ruler.

Demonstration:
Compare fitted-pair agreement with the gaps at unused known check points.

What to notice:
The independent inverse check measures distances in fixed-image pixels. Those points did not vote or fit.

Interpretation:
An independent geometric check answers a different question from an image similarity score.

Matching combined-demo lesson: test. Open chronological/demo/index.html#test.

Next main slide: 73. Independent point error: measure, then average.

Full discussion:
Say: If we help a student practice the exact quiz answers and then grade the same answers, the result may look better than their ability to solve a new question. A similar issue occurs if we fit a transformation to points and judge it only using those same fitted points.

The teaching experiment creates six separate grid points that never vote and never enter the refit. The researcher applies the known forward move, then the estimated correction, and measures how far those points return from their starting positions. With a translation, this residual distance is the same at every point, but the separation between fitting and evaluation remains explicit.

For RANSAC voting, the algorithm compares corrected moving points to their claimed partners. For evaluation, the researcher uses known corresponding test coordinates. These are different comparisons. Do not call a low vote residual a clinical target-registration-error measurement.

Ask: What is the ideal geometric recovery error in this controlled setup? Answer: Zero pixels. That ideal concerns the known generated movement, not unknown anatomy or acquisition accuracy.

Source context:
[9] Image Similarity and Tissue Overlaps as Surrogates for Image Registration Accuracy: Widely Used but Unreliable. https://pmc.ncbi.nlm.nih.gov/articles/PMC3274625/

Numbered sources:
[9] Torsten Rohlfing (2012). Image Similarity and Tissue Overlaps as Surrogates for Image Registration Accuracy: Widely Used but Unreliable. https://pmc.ncbi.nlm.nih.gov/articles/PMC3274625/

## Slide 73: Independent point error: measure, then average

Chronological slide 73 of 86. Part VI. Main route. Planned 0.94 minutes including the selected demonstration.

Purpose in ordinary words:
See how each check-point distance is obtained before averaging.

Demonstration:
Use the same doubled dots and one supplied undo multiplier. Inspect the three returned positions.

What to notice:
Undo 0.55 gives gaps 1,2,3; mean distance is 2 fixed pixels. Undo 0.50 gives zero.

Interpretation:
These points did not fit or vote. Mean point distance differs from brightness RMSE and from root mean squared point distance.

Matching combined-demo lesson: independent-error. Open chronological/demo/index.html#independent-error.

Next main slide: 75. Is a number good or bad?.

45-minute spoken route (one worked case; the longer discussion is for preparation):
The same supplied undo returns three checking dots one, two and three pixels from home. Add their distances and divide by three: the mean error is two fixed pixels. These dots did not help fit the movement. This is mean position distance, not brightness RMSE.

Full discussion:
Purpose: calculate independent point error from one shared transformation, not from unexplained example distances. The fixed checking dots are (10,0),(20,0),(30,0). A known forward resize doubles their coordinates, giving (20,0),(40,0),(60,0). The supplied imperfect undo multiplier is 0.55 instead of the exact 0.50. It returns them to (11,0),(22,0),(33,0). All y values remain zero. Subtract each known target position to obtain horizontal gaps one, two and three pixels; the vertical gaps are zero. Each straight-line distance is the square root of horizontal gap squared plus vertical gap squared, so the distances remain one, two and three. Add and divide by three: mean independent point error is two fixed-image pixels.

These are unused checking dots. They did not fit the movement or support a RANSAC proposal. The supplied estimate is deliberately chosen to make the arithmetic clear; it is not a new measured algorithm result. The same one movement recipe acts on all three dots. A wrong scale can create different errors at different positions, unlike a pure translation error, whose displacement gap is the same everywhere.

Mean distance differs from root mean squared distance. The latter would be sqrt((1+4+9)/3), approximately 2.160 pixels. The table reports mean straight-line distance, not that RMS quantity and not image-brightness RMSE. If a check-point y gap were nonzero, include it before averaging the straight-line distances. Lower mean means the known positions return closer under the stated ruler. Zero at these points does not establish identity everywhere or clinical truth. Independence here is from the fit, not independent patient subjects. The researcher can know correct positions in this controlled experiment because the generating transformation is known.

Numbered sources:
[1] Richard Szeliski (2004). Image Alignment and Stitching: A Tutorial. https://www.microsoft.com/en-us/research/publication/image-alignment-and-stitching-a-tutorial/
[9] Torsten Rohlfing (2012). Image Similarity and Tissue Overlaps as Surrogates for Image Registration Accuracy: Widely Used but Unreliable. https://pmc.ncbi.nlm.nih.gov/articles/PMC3274625/
[13] Shinji Umeyama (1991). Least-Squares Estimation of Transformation Parameters Between Two Point Patterns. https://doi.org/10.1109/34.88573

## Slide 74: Read the saved result table

Chronological slide 74 of 86. Part VI. Optional detail. Hidden during the normal forty-five-minute slideshow. Use for preparation or questions.

Purpose in ordinary words:
Translate dense laboratory labels into the quantities already learned.

Demonstration:
Read offset, sample count, ROI, bins, error and runtime separately.

What to notice:
The full search grid and the one displayed curve count different things.

Interpretation:
A number becomes useful only after its quantity, unit and comparison are clear.

Matching combined-demo lesson: original-results. Open chronological/demo/index.html#original-results.

Next main slide: 75. Is a number good or bad?.

Full discussion:
Read this table one row at a time. Name what the row did before reading the number. The values are mean independent-point errors in pixels for the shared default synthetic translation case. Lower means less leftover position error. They are not percentages.

Before means leaving the moving coordinates unchanged. The all-pairs mean averages the correction suggested by every pair, including deliberately wrong ones. The RANSAC result first finds agreement and then averages the winning group's suggested corrections. The known inverse is the deliberately constructed ideal geometric comparator.

Read the measured values from the executed notebook and describe only this case. If the robust estimate has smaller error than the all-pairs mean, the explanation is supported for these generated pairs and settings. The result does not establish that RANSAC always wins or that the same threshold suits other resolutions.

Ask: Which points supplied the reported error? Answer: The independent points, not the voting correspondences. Also report sigma, the voting threshold, and the number of deliberately wrong pairs because these define the example.

The saved consensus walkthrough enumerates all twelve suggestions, using the first highest-vote proposal when counts tie. Report that teaching simplification when describing this table as the RANSAC idea.

Executed example:
Measured on six independent generated points: no correction 7.211103 pixels; all-pairs average 3.672847 pixels; consensus refit 0.174704 pixels. The selected correction is (-6.134515, 4.111477) pixels. The selected group has 8 votes from 12 pairs; 2 distinct groups tie for the highest count. Sigma is 0.8 pixels per coordinate, and the voting distance is 2 pixels. The ideal known correction is(-6,+4)pixels.

## Slide 75: Is a number good or bad?

Chronological slide 75 of 86. Part VI. Main route. Planned 0.94 minutes including the selected demonstration.

Purpose in ordinary words:
Interpret each row before deciding whether a number is good.

Demonstration:
Name the row condition, column quantity, unit, baseline, known answer and limit.

What to notice:
Smaller geometric error means closer known positions. More support is not a guarantee of smaller independent error.

Interpretation:
A classroom target of at most 2 pixels is a declared teaching criterion at the displayed resolution, not an industry or clinical standard.

Matching combined-demo lesson: table. Open chronological/demo/index.html#table.

Next main slide: 77. Equal image scores at different positions.

Full discussion:
Good or bad requires a stated quantity, unit, comparison and task. For this educational demonstration the researcher declared a target of mean independent error at most two pixels at the displayed working resolution. That is a classroom criterion, not an industry baseline, clinical threshold or universal standard. Compare unregistered positions, estimated correction and the known inverse under the same resolution and check points. Smaller known-point error is better for the stated geometric question. A score such as MSE, NCC or MI measures another question. Clinical acceptance would require an application-defined physical tolerance and anatomical truth. Pixel errors from different image sizes or different trials should not be ranked blindly.

Expanded explanation and source context:
Use this answer pattern: This number measures this quantity, in these units. Smaller or larger is preferred under this rule. Compared with this baseline, it changed by this amount. The conclusion applies to these tested conditions.

For geometric error, zero pixels is the mathematical ideal in the constructed problem. A classroom tolerance, if used, is chosen by the researcher for the displayed resolution. It is not automatically a medical or remote-sensing requirement. Two pixels can represent very different physical distances in different images.

For MSE, the value depends on the brightness scale and compared region. For signed NCC, plus one and minus one have different directional meanings. For MI,0.693 nats is special to our balanced two-value example and is not a real-image pass mark. A voting threshold is a fitting setting, not a general quality grade.

Ask: Can we say MI 0.8 means 80 percent correct? Answer: No. State the actual information unit and protocol, then check the geometry separately.

Source context:
[9] Image Similarity and Tissue Overlaps as Surrogates for Image Registration Accuracy: Widely Used but Unreliable. https://pmc.ncbi.nlm.nih.gov/articles/PMC3274625/

Numbered sources:
[9] Torsten Rohlfing (2012). Image Similarity and Tissue Overlaps as Surrogates for Image Registration Accuracy: Widely Used but Unreliable. https://pmc.ncbi.nlm.nih.gov/articles/PMC3274625/

## Slide 76: Image agreement and position accuracy

Chronological slide 76 of 86. Part VI. Optional detail. Hidden during the normal forty-five-minute slideshow. Use for preparation or questions.

Purpose in ordinary words:
Illustrate Rohlfing’s [9] warning about similarity as a stand-in for accuracy.

Demonstration:
Compare the known +5 sampling offset with the equal-score +13 offset.

What to notice:
The pattern repeats every 8 pixels. Both can have MSE 0 and NCC +1, while the wrong location has 8 pixels of independent error.

Interpretation:
This live stripe counterexample illustrates an evaluation principle. It does not reproduce the paper’s patient experiments.

Matching combined-demo lesson: R6. Open chronological/demo/index.html#R6.

Next main slide: 77. Equal image scores at different positions.

Full discussion:
A surrogate is an indirect stand-in for the quantity we actually care about. Image similarity is sometimes used as a stand-in for geometric accuracy. Rohlfing reports evidence that image similarity and tissue overlap can be unreliable surrogates for registration accuracy in the studied nonrigid medical registration settings.

The class illustrates the evaluation principle using repeating stripes. It does not reproduce the original paper's brain images, deformation algorithms, or clinical experiment. The stripe pattern repeats every eight pixels. The researcher creates a five-pixel forward shift. Reading the moving picture five pixels to the right recovers the intended positions. Reading thirteen pixels right produces the same shades because thirteen differs from five by one complete repeat.

Both appearances can therefore have MSE zero, signed NCC plus one, and the same mutual information. The independent geometric comparison distinguishes the intended five-pixel answer from the thirteen-pixel look-alike. The latter has an eight-pixel error. A pixel ruler requires known corresponding positions; in this construction the generating movement supplies them. Similarity alone cannot invent missing identity information in a repeated pattern.

The follow-up question is an intentionally simple illustration of a published caution. It does not establish the frequency of this problem in patients or satellite scenes and does not reproduce a clinical accuracy threshold. The researcher should explain what each score measures, point at the repeated structure, then show the independent position result. A score is evidence for its own comparison rule, not a universal quality grade.

Published study: Torsten Rohlfing. Image Similarity and Tissue Overlaps as Surrogates for Image Registration Accuracy: Widely Used but Unreliable (2012).
Primary source: https://doi.org/10.1109/TMI.2011.2163944

What the paper contributes:
The paper constructs highly inaccurate nonrigid mappings that perform well on widely used similarity and tissue-overlap surrogates, demonstrating that such scores alone can mislead evaluation.

Evidence locations:
Section II.A-B and Fig. 2: 18 modified IBSR T1-weighted MR images and the rank-based CURT construction.
Section III.A-E: Similarity, tissue overlap, localized-region overlap, inverse-consistency results, and summary.
Section IV.B, Limitations of This Study: CURT is limited to same-modality experiments; known-deformation tests quantify actual error but do not establish accuracy between independent acquired images.
Section IV.C, Recommendations and Caveats: Geometric distance measures and evaluation as independent as possible from fitting.

Published limitation or scope boundary:
Section IV.B explicitly limits CURT to same-modality registration and explains that tests with known deformations do not establish registration accuracy between independent acquired images. Section IV.C calls for independent spatial evidence. The class periodic-pattern example uses a different mechanism from CURT.
Evidence location: Section IV.B-C

Classroom adaptation:
Use periodic binary stripes with period 8 pixels and a known 5-pixel horizontal sampling offset. Compare the correct offset +5 with wrong lookalikes +13 and -3: their intensity arrays match, but independent point positions differ by one period. Periodic wrap is explicit.

What this experiment does not reproduce:
The original CURT algorithm
Original nonrigid brain-registration experiments or tissue-label benchmark
The precise quantitative results of the paper

Follow-up question for this class:
Can an excellent similarity score coexist with a clearly incorrect geometric displacement on a repeated pattern?

Supported conclusion:
That the selected appearance score cannot distinguish the tested repeated-pattern alignments, despite different coordinate error.

Boundary on the conclusion:
That every high similarity score is wrong, that all registration metrics are useless, or that the original clinical/nonrigid experiments were replicated.

The classroom question does not carry a claim of novel or currently unsolved research.

Numbered sources:
[9] Torsten Rohlfing (2012). Image Similarity and Tissue Overlaps as Surrogates for Image Registration Accuracy: Widely Used but Unreliable. https://pmc.ncbi.nlm.nih.gov/articles/PMC3274625/

## Slide 77: Equal image scores at different positions

Chronological slide 77 of 86. Part VI. Main route. Planned 1.76 minutes including the selected demonstration.

Purpose in ordinary words:
Illustrate Rohlfing’s [9] warning about similarity as a stand-in for accuracy.

Demonstration:
Compare the known +5 sampling offset with the equal-score +13 offset.

What to notice:
The pattern repeats every 8 pixels. Both can have MSE 0 and NCC +1, while the wrong location has 8 pixels of independent error.

Interpretation:
This live stripe counterexample illustrates an evaluation principle. It does not reproduce the paper’s patient experiments.

Matching combined-demo lesson: R6. Open chronological/demo/index.html#R6.

Next main slide: 78. Explain the lesson in plain words.

Full discussion:
Research connection [9], Rohlfing (2012), cautions against treating image similarity as an automatic stand-in for registration accuracy. The live stripe example illustrates the warning; it does not replicate patient experiments. The pattern repeats every eight pixels. The known generated displacement is plus five. Sampling at plus five recovers the intended location, but plus thirteen reads identical shades one repeat away. Both can have MSE zero, NCC plus one and MI about 0.693 nats. The independent known-position error is zero for the intended answer and eight pixels for the repeated look-alike. State the purpose before revealing the table: test whether a perfect similarity score uniquely proves the right place. It does not in this constructed example.

Expanded explanation and source context:
A surrogate is an indirect stand-in for the quantity we actually care about. Image similarity is sometimes used as a stand-in for geometric accuracy. Rohlfing reports evidence that image similarity and tissue overlap can be unreliable surrogates for registration accuracy in the studied nonrigid medical registration settings.

The class illustrates the evaluation principle using repeating stripes. It does not reproduce the original paper's brain images, deformation algorithms, or clinical experiment. The stripe pattern repeats every eight pixels. The researcher creates a five-pixel forward shift. Reading the moving picture five pixels to the right recovers the intended positions. Reading thirteen pixels right produces the same shades because thirteen differs from five by one complete repeat.

Both appearances can therefore have MSE zero, signed NCC plus one, and the same mutual information. The independent geometric comparison distinguishes the intended five-pixel answer from the thirteen-pixel look-alike. The latter has an eight-pixel error. A pixel ruler requires known corresponding positions; in this construction the generating movement supplies them. Similarity alone cannot invent missing identity information in a repeated pattern.

The follow-up question is an intentionally simple illustration of a published caution. It does not establish the frequency of this problem in patients or satellite scenes and does not reproduce a clinical accuracy threshold. The researcher should explain what each score measures, point at the repeated structure, then show the independent position result. A score is evidence for its own comparison rule, not a universal quality grade.

Published study: Torsten Rohlfing. Image Similarity and Tissue Overlaps as Surrogates for Image Registration Accuracy: Widely Used but Unreliable (2012).
Primary source: https://doi.org/10.1109/TMI.2011.2163944

What the paper contributes:
The paper constructs highly inaccurate nonrigid mappings that perform well on widely used similarity and tissue-overlap surrogates, demonstrating that such scores alone can mislead evaluation.

Evidence locations:
Section II.A-B and Fig. 2: 18 modified IBSR T1-weighted MR images and the rank-based CURT construction.
Section III.A-E: Similarity, tissue overlap, localized-region overlap, inverse-consistency results, and summary.
Section IV.B, Limitations of This Study: CURT is limited to same-modality experiments; known-deformation tests quantify actual error but do not establish accuracy between independent acquired images.
Section IV.C, Recommendations and Caveats: Geometric distance measures and evaluation as independent as possible from fitting.

Published limitation or scope boundary:
Section IV.B explicitly limits CURT to same-modality registration and explains that tests with known deformations do not establish registration accuracy between independent acquired images. Section IV.C calls for independent spatial evidence. The class periodic-pattern example uses a different mechanism from CURT.
Evidence location: Section IV.B-C

Classroom adaptation:
Use periodic binary stripes with period 8 pixels and a known 5-pixel horizontal sampling offset. Compare the correct offset +5 with wrong lookalikes +13 and -3: their intensity arrays match, but independent point positions differ by one period. Periodic wrap is explicit.

What this experiment does not reproduce:
The original CURT algorithm
Original nonrigid brain-registration experiments or tissue-label benchmark
The precise quantitative results of the paper

Follow-up question for this class:
Can an excellent similarity score coexist with a clearly incorrect geometric displacement on a repeated pattern?

Supported conclusion:
That the selected appearance score cannot distinguish the tested repeated-pattern alignments, despite different coordinate error.

Boundary on the conclusion:
That every high similarity score is wrong, that all registration metrics are useless, or that the original clinical/nonrigid experiments were replicated.

The classroom question does not carry a claim of novel or currently unsolved research.

Purpose of this experiment:
Show why a similarity score is not a substitute for an independent geometric answer key.

Recorded settings:
Synthetic periodic dark/bright stripes; period 8; generated shift 5; 41 offsets (-20..20), 2-bin MI.

Interpretation of the measured rows:
Offsets +5, +13 and -3 have identical perfect similarity, but the latter two each miss known physical positions by 8 px.

Limits of this classroom run:
Constructed 2-D counterexample illustrating Rohlfing's warning, not a reproduction of the 3-D clinical experiment or a universal frequency of failure.

Read the condition first, name the measurement and its unit, and compare it with the known generated answer. Full raw measurements and figures are retained in the notebook and results files.

Numbered sources:
[9] Torsten Rohlfing (2012). Image Similarity and Tissue Overlaps as Surrogates for Image Registration Accuracy: Widely Used but Unreliable. https://pmc.ncbi.nlm.nih.gov/articles/PMC3274625/

## Slide 78: Explain the lesson in plain words

Chronological slide 78 of 86. Part VI. Main route. Planned 0.4 minutes including the selected demonstration.

Purpose in ordinary words:
Answer the professor’s purpose, meaning and quality questions.

Demonstration:
State the question, what changed, what was measured, the known answer and the limit.

What to notice:
Explain why the measurement is relevant before reading its number.

Interpretation:
Registration finds spatial alignment. Fusion combines useful information after alignment.

Matching combined-demo lesson: review. Open chronological/demo/index.html#review.

Next main slide: 82. Registration prepares pictures for fusion.

Full discussion:
Invite the learner to explain five things without formulas. First, registration means lining up corresponding parts. Second, MSE averages squared brightness differences. Third, signed NCC compares a linear pattern of variation, including whether it goes in the same or opposite direction. Fourth, mutual information measures how helpful paired values are as clues. Fifth, RANSAC tries proposed models and looks for agreement despite some wrong pairs.

Then ask about sigma: it is a per-coordinate spread setting for simulated point measurement error, not a maximum displacement. Ask about a graph dot: it records the score for one tried correction, and the linked overlay shows that correction.

If any explanation still needs an unexplained technical word, return to its worked example. The aim is that the researcher can explain the purpose, measurement, and interpretation in ordinary language before introducing the formal abbreviation. The optional equations and original materials can then serve as a next step rather than a starting obstacle.

## Slide 79: Everything on the original laboratory screen

Chronological slide 79 of 86. Part VI. Optional detail. Hidden during the normal forty-five-minute slideshow. Use for preparation or questions.

Purpose in ordinary words:
Locate detailed controls after learning their meaning.

Demonstration:
Use the screen guide as a lookup for a control you want to revisit.

What to notice:
The combined course keeps all earlier labs inside this one HTML file.

Interpretation:
A tour is a reference aid. The chronological lessons supply the explanations.

Matching combined-demo lesson: screen-map. Open chronological/demo/index.html#screen-map.

Next main slide: 82. Registration prepares pictures for fusion.

Full discussion:
This is an optional lookup for the detailed laboratory. The combined demo embeds four detailed panels: picture transformations, generated-point fitting, translation search and contrast search. The earlier lessons explain their controls in the order needed. Read the local definition and name the quantity and unit before changing a control or interpreting a result. The new deck contains 86 slides, with 44 main slides. Optional details and references stay beside their topics. The normal slideshow skips optional slides. Use this lookup after learning the terms, then return to the relevant topic through the combined navigation. The earlier separate labs remain available as fallbacks. Their old decks have different slide numbers.

## Slide 80: A checklist for every unfamiliar label

Chronological slide 80 of 86. Part VI. Optional detail. Hidden during the normal forty-five-minute slideshow. Use for preparation or questions.

Purpose in ordinary words:
Give every unfamiliar term a plain meaning, example and unit.

Demonstration:
Choose a term and describe what it changes or measures.

What to notice:
Point-click sigma, blur sigma and brightness noise describe different quantities and units.

Interpretation:
A clear explanation names the measurement and what its evidence can support.

Matching combined-demo lesson: complete-review. Open chronological/demo/index.html#complete-review.

Next main slide: 82. Registration prepares pictures for fusion.

Full discussion:
Use the complete original-screen walkthrough and term catalogue as a lookup, not as a substitute for the worked lessons. Every control, score, and graph label is linked to a meaning, an example, its unit or role, and a common mistake. The detailed laboratory supplies the same help where the term appears.

Before touching a control, name what it changes: input geometry, pixel appearance, point measurements, a fitting rule, a display blend, or the search candidate. Before judging an output, name whether it measures brightness mismatch, descriptor disagreement, model agreement, independent geometry, valid area, or runtime.

Use the public-image ORB notebook to see actual detection and matching. Use the generated-point browser simulation to understand robust fitting. Use the known-inverse operation as a supplied-answer check. These are different learning activities and must remain labeled.

When returning to the original presentation, explain why each experiment is conducted, point at the measured comparison, and state the limits. If a term is still unclear, its worked example should be the next step; there is no need to pretend a formula or abbreviation is understood.

Source context:
[1] Image Alignment and Stitching: A Tutorial. https://www.microsoft.com/en-us/research/publication/image-alignment-and-stitching-a-tutorial/
[2] ORB (Oriented FAST and Rotated BRIEF). https://docs.opencv.org/4.13.0/d1/d89/tutorial_py_orb.html
[3] Random Sample Consensus: A Paradigm for Model Fitting with Applications to Image Analysis and Automated Cartography. https://www.sri.com/publication/artificial-intelligence-pubs/random-sample-consensus-a-paradigm-for-model-fitting-with-applications-to-image-analysis-and-automated-cartography/
[4] Camera Calibration and 3D Reconstruction: estimateAffinePartial2D. https://docs.opencv.org/4.13.0/d9/d0c/group__calib3d.html
[8] Registration Overview. https://simpleitk.readthedocs.io/en/latest/registrationOverview.html
[9] Image Similarity and Tissue Overlaps as Surrogates for Image Registration Accuracy: Widely Used but Unreliable. https://pmc.ncbi.nlm.nih.gov/articles/PMC3274625/

Numbered sources:
[1] Richard Szeliski (2004). Image Alignment and Stitching: A Tutorial. https://www.microsoft.com/en-us/research/publication/image-alignment-and-stitching-a-tutorial/
[2] OpenCV contributors (2026). ORB (Oriented FAST and Rotated BRIEF). https://docs.opencv.org/4.13.0/d1/d89/tutorial_py_orb.html
[3] Martin A. Fischler and Robert C. Bolles (1981). Random Sample Consensus: A Paradigm for Model Fitting with Applications to Image Analysis and Automated Cartography. https://www.sri.com/publication/artificial-intelligence-pubs/random-sample-consensus-a-paradigm-for-model-fitting-with-applications-to-image-analysis-and-automated-cartography/
[4] OpenCV contributors (2026). Camera Calibration and 3D Reconstruction: estimateAffinePartial2D. https://docs.opencv.org/4.13.0/d9/d0c/group__calib3d.html
[8] SimpleITK contributors (2026). Registration Overview. https://simpleitk.readthedocs.io/en/latest/registrationOverview.html
[9] Torsten Rohlfing (2012). Image Similarity and Tissue Overlaps as Surrogates for Image Registration Accuracy: Widely Used but Unreliable. https://pmc.ncbi.nlm.nih.gov/articles/PMC3274625/

## Slide 81: What these experiments support

Chronological slide 81 of 86. Part VI. Optional detail. Hidden during the normal forty-five-minute slideshow. Use for preparation or questions.

Purpose in ordinary words:
Give every unfamiliar term a plain meaning, example and unit.

Demonstration:
Choose a term and describe what it changes or measures.

What to notice:
Point-click sigma, blur sigma and brightness noise describe different quantities and units.

Interpretation:
A clear explanation names the measurement and what its evidence can support.

Matching combined-demo lesson: complete-review. Open chronological/demo/index.html#complete-review.

Next main slide: 82. Registration prepares pictures for fusion.

Full discussion:
The researcher uses controlled transformations to know the correct geometric answer before trying a method. Repeating that experiment shows behavior under the stated image, settings and perturbations. It does not establish performance for all satellite images or patients. Saved Python results back up live demonstrations. Browser generated-point fitting, actual OpenCV ORB output, and saved study selectors are different evidence types and retain their labels. Runtime belongs to the measured machine and implementation. Pixel distances depend on the image resolution; clinical interpretation needs calibrated physical units and a defined task. Research connections state the published contribution, documented limitations, the classroom follow-up question and the parts that are not reproduced. A classroom question is not automatically a novel unsolved research gap.

Numbered sources:
[1] Richard Szeliski (2004). Image Alignment and Stitching: A Tutorial. https://www.microsoft.com/en-us/research/publication/image-alignment-and-stitching-a-tutorial/
[9] Torsten Rohlfing (2012). Image Similarity and Tissue Overlaps as Surrogates for Image Registration Accuracy: Widely Used but Unreliable. https://pmc.ncbi.nlm.nih.gov/articles/PMC3274625/

## Slide 82: Registration prepares pictures for fusion

Chronological slide 82 of 86. Part VI. Main route. Planned 0.2 minutes including the selected demonstration.

Questions follow the main route. References and optional detail remain available.

Full discussion:
The researcher closes Parts I–VI here. Registration finds a spatial relationship. Fusion combines useful information from pictures after suitable alignment. For example, a fused display can combine complementary information, but poor registration can put it in the wrong location. The partner covers the remaining topics. Ask the audience to state which evidence supported each movement and which separate check established recovery of the known transformation.

Numbered sources:
[1] Richard Szeliski (2004). Image Alignment and Stitching: A Tutorial. https://www.microsoft.com/en-us/research/publication/image-alignment-and-stitching-a-tutorial/

## Slide 83: References

Chronological slide 83 of 86. Part References. Optional detail. Hidden during the normal forty-five-minute slideshow. Use for preparation or questions.

Questions follow the main route. References and optional detail remain available.

Full discussion:
{
  "id": 1,
  "authors": "Richard Szeliski",
  "year": 2004,
  "title": "Image Alignment and Stitching: A Tutorial",
  "publication": "Microsoft Research Technical Report MSR-TR-2004-92",
  "url": "https://www.microsoft.com/en-us/research/publication/image-alignment-and-stitching-a-tutorial/",
  "accessed": "2026-10-15",
  "supports": "Registration as geometric alignment; direct and feature approaches; registration precedes blending; motion and parallax limitations."
}

{
  "id": 2,
  "authors": "OpenCV contributors",
  "year": 2026,
  "title": "ORB (Oriented FAST and Rotated BRIEF)",
  "publication": "OpenCV 4.13.0 documentation",
  "url": "https://docs.opencv.org/4.13.0/d1/d89/tutorial_py_orb.html",
  "accessed": "2026-10-15",
  "original_paper": "E. Rublee, V. Rabaud, K. Konolige, and G. Bradski, ORB: An efficient alternative to SIFT or SURF, ICCV, pp. 2564–2571, 2011, doi:10.1109/ICCV.2011.6126544.",
  "supports": "ORB combines FAST detection with oriented binary descriptions; Hamming distance for default binary descriptors. Do not repeat the tutorial's outdated SIFT patent claim."
}

{
  "id": 3,
  "authors": "Martin A. Fischler and Robert C. Bolles",
  "year": 1981,
  "title": "Random Sample Consensus: A Paradigm for Model Fitting with Applications to Image Analysis and Automated Cartography",
  "publication": "Communications of the ACM, 24(6), pp. 381–395",
  "doi": "10.1145/358669.358692",
  "url": "https://www.sri.com/publication/artificial-intelligence-pubs/random-sample-consensus-a-paradigm-for-model-fitting-with-applications-to-image-analysis-and-automated-cartography/",
  "accessed": "2026-10-15",
  "supports": "Robust model fitting in measurements contaminated by gross errors. The institution page displays a 1980 page date but its publication citation is 1981."
}

{
  "id": 4,
  "authors": "OpenCV contributors",
  "year": 2026,
  "title": "Camera Calibration and 3D Reconstruction: estimateAffinePartial2D",
  "publication": "OpenCV 4.13.0 documentation",
  "url": "https://docs.opencv.org/4.13.0/d9/d0c/group__calib3d.html",
  "accessed": "2026-10-15",
  "supports": "Four-degree-of-freedom partial affine/similarity estimate; RANSAC reprojection threshold, confidence, iteration settings and inlier mask."
}

Numbered sources:
[1] Richard Szeliski (2004). Image Alignment and Stitching: A Tutorial. https://www.microsoft.com/en-us/research/publication/image-alignment-and-stitching-a-tutorial/
[2] OpenCV contributors (2026). ORB (Oriented FAST and Rotated BRIEF). https://docs.opencv.org/4.13.0/d1/d89/tutorial_py_orb.html
[3] Martin A. Fischler and Robert C. Bolles (1981). Random Sample Consensus: A Paradigm for Model Fitting with Applications to Image Analysis and Automated Cartography. https://www.sri.com/publication/artificial-intelligence-pubs/random-sample-consensus-a-paradigm-for-model-fitting-with-applications-to-image-analysis-and-automated-cartography/
[4] OpenCV contributors (2026). Camera Calibration and 3D Reconstruction: estimateAffinePartial2D. https://docs.opencv.org/4.13.0/d9/d0c/group__calib3d.html

## Slide 84: References, continued

Chronological slide 84 of 86. Part References. Optional detail. Hidden during the normal forty-five-minute slideshow. Use for preparation or questions.

Questions follow the main route. References and optional detail remain available.

Full discussion:
{
  "id": 5,
  "authors": "Manuel Guizar-Sicairos, Samuel T. Thurman, and James R. Fienup",
  "year": 2008,
  "title": "Efficient subpixel image registration algorithms",
  "publication": "Optics Letters, 33(2), pp. 156–158",
  "doi": "10.1364/OL.33.000156",
  "url": "https://doi.org/10.1364/OL.33.000156",
  "verified_full_text_url": "https://citeseerx.ist.psu.edu/document?doi=b5978b756bdcad061e3269eafaa69452a0c43e1b&repid=rep1&type=pdf",
  "accessed": "2026-10-15",
  "supports": "Efficient Fourier-domain translation estimation with local matrix-multiply DFT refinement. Numerical sampling resolution is not guaranteed registration accuracy."
}

{
  "id": 6,
  "authors": "scikit-image contributors",
  "year": 2026,
  "title": "skimage.registration: phase_cross_correlation",
  "publication": "scikit-image stable API documentation",
  "url": "https://scikit-image.org/docs/stable/api/skimage.registration.html",
  "example_url": "https://scikit-image.org/docs/stable/auto_examples/registration/plot_register_translation.html",
  "accessed": "2026-10-15",
  "supports": "Returned shift aligns moving to reference in array-axis order; upsample_factor; normalization and Fourier periodic ambiguity. Returned error is not geometric error in pixels."
}

{
  "id": 7,
  "authors": "Paul Viola and William M. Wells III",
  "year": 1997,
  "title": "Alignment by Maximization of Mutual Information",
  "publication": "International Journal of Computer Vision, 24(2), pp. 137–154",
  "doi": "10.1023/A:1007958904918",
  "url": "https://doi.org/10.1023/A:1007958904918",
  "verified_full_text_url": "https://cs.uwaterloo.ca/~mannr/cs886-w10/ViolaWells_IJCV.pdf",
  "accessed": "2026-10-15",
  "supports": "Statistical dependence can support alignment without equal image intensities; mutual information formulation and MRI alignment."
}

{
  "id": 8,
  "authors": "SimpleITK contributors",
  "year": 2026,
  "title": "Registration Overview",
  "publication": "SimpleITK documentation",
  "url": "https://simpleitk.readthedocs.io/en/latest/registrationOverview.html",
  "accessed": "2026-10-15",
  "supports": "Transform, metric, optimizer and interpolation; initialization; fixed-to-moving sampling convention; maximized metrics may be internally negated."
}

Numbered sources:
[5] Manuel Guizar-Sicairos, Samuel T. Thurman, and James R. Fienup (2008). Efficient subpixel image registration algorithms. https://doi.org/10.1364/OL.33.000156
[6] scikit-image contributors (2026). skimage.registration: phase_cross_correlation. https://scikit-image.org/docs/stable/api/skimage.registration.html
[7] Paul Viola and William M. Wells III (1997). Alignment by Maximization of Mutual Information. https://doi.org/10.1023/A:1007958904918
[8] SimpleITK contributors (2026). Registration Overview. https://simpleitk.readthedocs.io/en/latest/registrationOverview.html

## Slide 85: References, continued

Chronological slide 85 of 86. Part References. Optional detail. Hidden during the normal forty-five-minute slideshow. Use for preparation or questions.

Questions follow the main route. References and optional detail remain available.

Full discussion:
{
  "id": 9,
  "authors": "Torsten Rohlfing",
  "year": 2012,
  "title": "Image Similarity and Tissue Overlaps as Surrogates for Image Registration Accuracy: Widely Used but Unreliable",
  "publication": "IEEE Transactions on Medical Imaging, 31(2), pp. 153–163",
  "doi": "10.1109/TMI.2011.2163944",
  "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC3274625/",
  "accessed": "2026-10-15",
  "supports": "Primary experimental evidence that similarity/overlap alone can give misleading registration conclusions. Study concerns nonrigid registration; used here as a caution, not a measured result of this 2D study."
}

{
  "id": 10,
  "authors": "scikit-image contributors; image by Lav Varshney",
  "year": 2026,
  "title": "skimage.data.camera",
  "publication": "scikit-image stable data API documentation",
  "url": "https://scikit-image.org/docs/stable/api/skimage.data#skimage.data.camera",
  "accessed": "2026-10-15",
  "license": "CC0; no copyright restrictions, as stated by the scikit-image data documentation.",
  "supports": "512 × 512 grayscale source image; replacement since version 0.18; current photographer and CC0 dedication."
}

{
  "id": 11,
  "authors": "Insight Software Consortium / ITK contributors",
  "year": 2026,
  "title": "ITK ImageRegistration2.cxx: T1 and proton-density MRI registration example",
  "publication": "ITK Examples/RegistrationITKv4, source repository",
  "url": "https://raw.githubusercontent.com/InsightSoftwareConsortium/ITK/main/Examples/RegistrationITKv4/ImageRegistration2.cxx",
  "accessed": "2026-10-15",
  "supports": "Identifies BrainT1SliceBorder20.png as T1 MRI and BrainProtonDensitySliceBorder20.png as PD MRI, unit spacing, and describes intentionally shifted input. Does not establish original acquisition or clinical ground truth."
}

{
  "id": 12,
  "authors": "Insight Software Consortium / NumFOCUS",
  "year": 2026,
  "title": "ITK LICENSE",
  "publication": "ITK source repository",
  "url": "https://raw.githubusercontent.com/InsightSoftwareConsortium/ITK/main/LICENSE",
  "accessed": "2026-10-15",
  "license": "Apache License 2.0 (repository-level license).",
  "supports": "Repository distribution terms; retained attribution. No separate image-specific acquisition provenance was located."
}

Numbered sources:
[9] Torsten Rohlfing (2012). Image Similarity and Tissue Overlaps as Surrogates for Image Registration Accuracy: Widely Used but Unreliable. https://pmc.ncbi.nlm.nih.gov/articles/PMC3274625/
[10] scikit-image contributors; image by Lav Varshney (2026). skimage.data.camera. https://scikit-image.org/docs/stable/api/skimage.data#skimage.data.camera
[11] Insight Software Consortium / ITK contributors (2026). ITK ImageRegistration2.cxx: T1 and proton-density MRI registration example. https://raw.githubusercontent.com/InsightSoftwareConsortium/ITK/main/Examples/RegistrationITKv4/ImageRegistration2.cxx
[12] Insight Software Consortium / NumFOCUS (2026). ITK LICENSE. https://raw.githubusercontent.com/InsightSoftwareConsortium/ITK/main/LICENSE

## Slide 86: References, continued

Chronological slide 86 of 86. Part References. Optional detail. Hidden during the normal forty-five-minute slideshow. Use for preparation or questions.

Questions follow the main route. References and optional detail remain available.

Full discussion:
{
  "id": 13,
  "authors": "Shinji Umeyama",
  "year": 1991,
  "title": "Least-Squares Estimation of Transformation Parameters Between Two Point Patterns",
  "url": "https://doi.org/10.1109/34.88573",
  "doi": "10.1109/34.88573",
  "publication": "IEEE Transactions on Pattern Analysis and Machine Intelligence",
  "accessed": "2026-10-23"
}

{
  "id": 14,
  "authors": "Ethan Rublee, Vincent Rabaud, Kurt Konolige, Gary Bradski",
  "year": 2011,
  "title": "ORB: An efficient alternative to SIFT or SURF",
  "url": "https://doi.org/10.1109/ICCV.2011.6126544",
  "doi": "10.1109/ICCV.2011.6126544",
  "publication": "2011 International Conference on Computer Vision",
  "accessed": "2026-10-23"
}

{
  "id": 15,
  "authors": "Colin Studholme, Derek L. G. Hill, David J. Hawkes",
  "year": 1999,
  "title": "An overlap invariant entropy measure of 3D medical image alignment",
  "url": "https://doi.org/10.1016/S0031-3203(98)00091-0",
  "doi": "10.1016/S0031-3203(98)00091-0",
  "publication": "Pattern Recognition",
  "accessed": "2026-10-23"
}

{
  "id": 16,
  "authors": "Nathan D. Cahill, Julia A. Schnabel, J. Alison Noble, David J. Hawkes",
  "year": 2008,
  "title": "Revisiting overlap invariance in medical image alignment",
  "url": "https://doi.org/10.1109/CVPRW.2008.4562989",
  "doi": "10.1109/CVPRW.2008.4562989",
  "publication": "2008 IEEE Computer Society Conference on Computer Vision and Pattern Recognition Workshops",
  "accessed": "2026-10-23"
}

Numbered sources:
[13] Shinji Umeyama (1991). Least-Squares Estimation of Transformation Parameters Between Two Point Patterns. https://doi.org/10.1109/34.88573
[14] Ethan Rublee, Vincent Rabaud, Kurt Konolige, Gary Bradski (2011). ORB: An efficient alternative to SIFT or SURF. https://doi.org/10.1109/ICCV.2011.6126544
[15] Colin Studholme, Derek L. G. Hill, David J. Hawkes (1999). An overlap invariant entropy measure of 3D medical image alignment. https://doi.org/10.1016/S0031-3203(98)00091-0
[16] Nathan D. Cahill, Julia A. Schnabel, J. Alison Noble, David J. Hawkes (2008). Revisiting overlap invariance in medical image alignment. https://doi.org/10.1109/CVPRW.2008.4562989
