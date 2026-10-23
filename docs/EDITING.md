# Editing and keeping references aligned

The native PowerPoint remains directly editable, with full speaker notes and hidden optional slides preserved. The HTML is a self-contained application containing embedded styles, source documents, images and evidence. Keep an original copy before editing either artifact.

The current lesson plan and [slide/demo map](../content/SLIDE_DEMO_MAP.md) document all 86 slide numbers and 45 ordered browser steps. The main route has 44 visible slides. PowerPoint hyperlinks point to `../demo/index.html#lesson-id`; moving the two sibling directories together preserves these links.

If slide order changes, update the lesson plan, slide map, slide notes and hyperlinks, the demo's embedded plan and visible labels, and the notebook's section references together. `tools/verify_repo.py` catches structural mismatches; it cannot judge whether an explanation is clear or a changed experiment is scientifically appropriate.

This curated pack includes the numerical experiment scripts, current lesson metadata and finished editable artifacts. Historical decks, historical demo sources and native-PowerPoint assembly scripts are omitted. Those builders depended on earlier presentation editions. The current PPTX is the editable presentation source in this repository; the pack does not claim to rebuild it from JSON alone.

`content/lesson_plan.json`, the demo and recorded notebook evidence retain historical source identifiers and original workspace-relative provenance strings. Their current runtime links already use the sibling `presentation/` and `demo/` directories. [repository_paths.json](../content/repository_paths.json) explicitly maps the original workspace paths to this curated tree. Those provenance strings do not request that omitted historical decks be opened.

The [paper](../paper/image_registration_study.md) has repository-relative artifact links. Its numerical results, research interpretations and current slide numbering are retained. Add a license for original materials only after the repository owner chooses one; third-party notices remain separate.
