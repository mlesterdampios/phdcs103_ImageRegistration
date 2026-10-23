# Public photograph and derived experiment images

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
