# Structured Corpus

The files in this directory provide the machine-readable L1-L4 corpus of 313 unique systems used by the survey.

- `agentic_visual_generation_corpus.csv` and `.json` contain one row per unique system.
- `landscape_summary.json` contains the counts used for the temporal, modality, and mechanism analyses.
- `../scripts/build_structured_corpus.py` regenerates every file from the taxonomy tables in `README.md`, which remain the canonical human-reviewed source.

## Annotation fields

Identity, date, level, capability path, modalities, primary mechanism, and official links are parsed directly from the reviewed catalog. `closed_loop` records whether the capability path includes L3, while `cross_task_persistence` records primary L4 placement. The seven mechanism indicators are reproducible tags derived from catalog section placement, taxonomy paths, paper titles, and primary-mechanism annotations. They support aggregate analysis and should not be interpreted as exhaustive architectural descriptions.

Four normalized descriptors support comparison across heterogeneous papers. `controller_type` distinguishes a default language or multimodal controller, a multi-role controller, and a unified multimodal policy using conservative title and mechanism cues. `visual_executor` maps reviewed modality tags to the artifact-producing executor. `feedback` records the causal feedback boundary implied by the assigned level. `evaluation_type` states the minimum level-appropriate evaluation target. These normalized fields are generated interpretations, not substitutes for the original paper's implementation details.

Modality annotations are multi-label. Consequently, a system can contribute to more than one row of a modality-by-level table. L0 supporting components and evaluation-only resources are excluded from these files.
