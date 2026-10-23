# Source verification and citation notes

The numbered entries in [references.json](../content/references.json) are shared by the slides, paper, and presenter notes. Sources were checked on October 15, 2026. Reference numbering is fixed. This file documents provenance and claim boundaries; it is not part of the spoken presentation.

| Reference | Primary evidence checked | Use in the materials |
|---|---|---|
| [1] | Researcher's institutional technical-report record | Broad feature/direct taxonomy, geometric models, and distinction between alignment and blending. |
| [2] | Official OpenCV ORB tutorial | FAST keypoints, orientation, binary descriptors, Hamming distance. Its historical SIFT patent statement is outdated and is deliberately not repeated. |
| [3] | Original authors' SRI publication record | RANSAC as robust fitting with gross errors. Cite the bibliographic year 1981; the web record also displays a different page date. |
| [4] | Official OpenCV calibration API | `estimateAffinePartial2D`, four degrees of freedom, RANSAC inlier mask and controls. A RANSAC fit threshold is an internal rule, not final accuracy. |
| [5] | Original 2008 paper full text | Local upsampled DFT translation refinement. No claim that a chosen upsampling factor guarantees that precision on arbitrary data. |
| [6] | Official scikit-image registration API and example | Shift is the correction applied to the moving image; array order is `(row, column)` or `(dy, dx)`. Returned normalized image error differs from geometric error. |
| [7] | Original 1997 journal article full text | MI captures statistical dependence without assuming equal intensities. The classroom implementation uses a simple histogram and bounded search; it is not a reproduction of the original optimizer. |
| [8] | Official SimpleITK registration overview | Registration components, initialization, transform direction, and internal metric sign conventions. SimpleITK is conceptual background, not a requirement for the lightweight experiments. |
| [9] | Full original research article in PubMed Central | Similarity and tissue overlap can be misleading surrogates. The published experiment is nonrigid; it is cited as methodological caution, not as a result of this study. |
| [10] | Official dataset API | Current `camera` image is CC0 by Lav Varshney, 512 × 512. Avoid using an old unverified camera image from another website. |
| [11] | Original ITK example source, especially its multimodality caption | Public T1/PD MRI teaching pair. Both are MRI contrasts, not a CT/MRI acquisition. Source describes an intentionally shifted PD image and unit spacing. |
| [12] | ITK root `LICENSE` | Apache 2.0 distribution terms at repository level. No image-specific acquisition metadata was independently verified. |

## Medical image terminology and limits

The ITK pair supports a real difference in MRI contrast. The materials call it a **public T1/PD MRI teaching pair** or **a genuine contrast-pair example**, rather than implying that the researcher acquired a clinical dataset. T1-weighted and proton-density-weighted images are different MRI contrasts within the same broad imaging modality. A stricter definition of multimodality reserves the word for different acquisition technologies, such as CT and MRI. Explain that distinction if asked.

The public source identifies the contrast types but does not establish original scanner, patient, date, or anatomical correspondence ground truth. Any reported recovery error for this pair concerns only the additional known displacement introduced by the researcher relative to the supplied pair. It cannot establish clinical accuracy. A preprocessing contrast inversion of one photograph is explicitly simulated and is kept distinct from this public pair.

## Licensing record

The current camera image has an explicit CC0 dedication. The ITK source and repository license establish repository distribution terms and source attribution, but no independent assertion about the original medical image acquisition license is made. The bundled provenance file retains actual download paths and checksums. Third-party data should retain this provenance when the package is copied.

## Threshold interpretation

The mean geometric error criterion of at most 2 pixels is a demonstration criterion selected for this package's displayed image resolution. It is not an industry, medical, satellite, or regulatory standard. No source is cited as establishing it. A deployment threshold would have to be linked to physical pixel size, target structures, downstream task, uncertainty, and a representative external validation set.

## Reference links

For exact titles, publication data, direct URLs, and verified full-text locations, use [references.json](../content/references.json). DOI links identify published papers; live documentation URLs identify implementation conventions. Package version numbers are recorded separately with the actual experimental results.
