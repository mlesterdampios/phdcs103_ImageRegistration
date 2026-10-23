# Image Registration: A Step-by-Step Teaching Laboratory

**Mark Lester O. Dampios**  
PhDCS Student, Technological Institute of the Philippines - Manila  
PHDCS103 - Image Processing | Dr. Anna Liza Ramos  
Week 15: October 31, 2026 | Parts I–VI

The researcher demonstrates how two pictures can be lined up and how the answer can be checked fairly. Plain-English explanations, worked calculations and controlled experiments accompany the slides.

## Start here

1. Download [the latest PowerPoint](presentation/Dampios_Image_Registration_Chronological_Explained.pptx). It includes full speaker notes, numbered references and links to the matching demo lessons.
2. Open [demo/index.html](demo/index.html) locally in a modern browser. This single file contains the controls, images, calculations and saved results; it needs no server, Python or internet connection.
3. Read [the measurements guide](MEASUREMENTS_GUIDE.md) when a formula, graph, unit or result is unfamiliar.

On GitHub, an HTML link displays source rather than running the lesson. Download or clone the repository, then double-click `demo/index.html`. Keep `presentation/` and `demo/` beside one another so PowerPoint's relative demo links continue to work. Windows users can double-click `Open_Demo.cmd`.

The presentation contains **86 slides: 44 on the main route and 42 hidden optional slides**. The planned main route is approximately 45 minutes including demonstrations and switching, with questions afterward. This is a delivery plan rather than a measured rehearsal. The demo contains **45 ordered steps**: 32 retained activities, 7 worked measurement lessons and 6 purpose introductions.

## Folder guide

```text
presentation/    Latest explained PowerPoint and full presenter script
demo/            One standalone offline index.html
notebooks/       Executed notebook, offline HTML and bundled evidence
content/         Lesson plan, exact slide/demo map and numbered references
figures/         Current slide-number-free teaching figures
paper/           Adaptable Markdown research paper
docs/            Setup, editing, reproduction and provenance guidance
experiments/     Runnable CPU scripts, public inputs and recorded outputs
tools/           Repository verification and offline browser checks
```

## Study and reproduce

- [Executed notebook](notebooks/01_chronological_experiments.ipynb) and [offline reading copy](notebooks/01_chronological_experiments.html)
- [Presenter script](presentation/PRESENTER_SCRIPT.md) and [exact slide/demo map](content/SLIDE_DEMO_MAP.md)
- [Adaptable Markdown paper](paper/image_registration_study.md)
- [Python setup](docs/SETUP.md), [experiment commands](docs/EXPERIMENTS.md) and [editing guide](docs/EDITING.md)
- [Public-image provenance](experiments/data/PROVENANCE.md) and [third-party notices](THIRD_PARTY_NOTICES.md)

The notebook executes 22 short code cells against bundled evidence. The full ORB, registration and research experiments are separate scripts under `experiments/`. Running those scripts changes their saved outputs; it does not automatically regenerate the published slides or the standalone demo. Their original internal folder relationships are retained for reproducibility.

## Verify the downloaded files

From the repository root, run:

```sh
python tools/verify_repo.py
```

This uses Python's standard library and checks file hashes, the saved notebook, slide order, notes and relative demo links. It does not rerun the research pipelines. Optional browser testing is described in [setup](docs/SETUP.md).

For a distribution audit that also rejects local environments, Git metadata and temporary files, run `python tools/verify_repo.py --strict-pack` before packaging. Normal verification skips those local working directories. The included `.gitattributes` preserves file bytes across checkouts so line-ending conversion does not invalidate the recorded checksums.

## Scope and interpretation

The researcher uses controlled transformations with known answers, public photographs and a genuine public T1/proton-density MRI contrast pair. Simulated changes are labeled. Recovery of an artificially added MRI shift does not establish original anatomical alignment or clinical performance. A two-pixel teaching criterion is a declared classroom example, not an industry standard. Research connections are method-level reproductions or illustrations rather than replications of the papers' original benchmarks.

## Commit manually

This folder contains no Git history or configured remote. Create an empty GitHub repository, then use your preferred Git client or run these commands **inside this folder**:

```sh
git init
git add .
git commit -m "Add image registration presentation, demo and experiments"
```

Add your own remote when ready. [License status](LICENSE_NOTICE.md) distinguishes the researcher's materials from the bundled third-party images.
