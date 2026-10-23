# Source images and derived classroom data

All images are bundled for offline use. No data download occurs when running the experiments or notebooks.

## Camera photograph

- File: `camera.png`, 512 × 512 pixels, grayscale.
- Provider: `skimage.data.camera()` in scikit-image 0.24.0.
- Photographer: Lav Varshney.
- Permission: official scikit-image documentation identifies the image as CC0, with no copyright restrictions.
- Primary documentation: <https://scikit-image.org/docs/stable/api/skimage.data#skimage.data.camera>.
- Experiment processing: area-resized to 384 × 384 for feature/phase tests and to 160 × 160 for exhaustive metric search. Derived PNGs and transformation/noise variants are saved alongside the source image.

## Public ITK MRI teaching pair

- Local `brain_pd.png` is `BrainProtonDensitySliceBorder20.png`: proton-density weighted MRI teaching image.
- Local `brain_t1.png` is `BrainT1SliceBorder20.png`: T1-weighted MRI teaching image.
- Each array has 221 columns × 257 rows. Both are MRI contrasts, not a CT/MRI pair.
- Retrieved October 16, 2026 from the Insight Software Consortium ITK repository. Source commit: `50c5b33430e98b91b53fbaae2dd94f0edb2a639a`.
- PD image: <https://raw.githubusercontent.com/InsightSoftwareConsortium/ITK/50c5b33430e98b91b53fbaae2dd94f0edb2a639a/Examples/Data/BrainProtonDensitySliceBorder20.png>.
- T1 image: <https://raw.githubusercontent.com/InsightSoftwareConsortium/ITK/50c5b33430e98b91b53fbaae2dd94f0edb2a639a/Examples/Data/BrainT1SliceBorder20.png>.
- Modality identification in primary example source: <https://raw.githubusercontent.com/InsightSoftwareConsortium/ITK/50c5b33430e98b91b53fbaae2dd94f0edb2a639a/Examples/RegistrationITKv4/ImageRegistration2.cxx>.
- Repository license: Apache License 2.0; its full text is bundled as `ITK_LICENSE.txt`. Repository-level license: <https://github.com/InsightSoftwareConsortium/ITK/blob/50c5b33430e98b91b53fbaae2dd94f0edb2a639a/LICENSE>.
- Image-specific original acquisition, patient metadata, physical pixel spacing, and independent anatomical ground truth have not been established from these repository files. The researcher treats them as a public teaching pair, not a clinical validation dataset.

The experiment introduces a known (+9, -6)-pixel displacement into the T1 image and measures recovery relative to each metric's native-pair optimum. The reported error therefore concerns the added perturbation. It does not establish native anatomical accuracy or patient-level performance.

## Derived images and checksums

`fixed_384.png`, `transform_moving.png`, `feature_moving.png`, `feature_registered.png`, `intensity_moving.png`, `intensity_registered.png`, and `simulated_contrast_*.png` are researcher-generated transformations of the source photograph. Contrast inversion is explicitly simulated; it is not another acquired modality. Files are normalized and quantized to 8-bit for display; calculations use floating-point arrays before export.

SHA-256 checksums, seed, operating system, package versions, coordinate convention, and evaluation policy are recorded in `../results/manifest.json`. The seed is 20261031. Runtime is hardware-specific.
