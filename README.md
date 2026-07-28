# Capstone Project 4 - Deep Learning Systems

## Project title

**Transformer-Based Classification of Contract Clause Themes**

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/icmsol/capstone-project-4-deep-learning-systems/blob/main/deep_learning.ipynb)

## Project overview

This project implements and evaluates a custom PyTorch Transformer that classifies commercial-contract passages into ten clause themes. It uses expert-annotated passages derived from the Contract Understanding Atticus Dataset (CUAD) and compares two otherwise identical configurations in a controlled experiment: baseline dropout of 0.10 and experimental dropout of 0.30.

For ICM Solutions, the project demonstrates a semantic-intelligence capability that can support contract review, knowledge reuse, document-quality checks, and future grounded generative-AI workflows. It is a research prototype for human-assisted review, not legal advice or an autonomous contracting decision system.

## Business and capstone relevance

The first three capstone projects established reproducible data, statistical, and machine-learning workflows. This project extends the sequence into unstructured language by classifying contract clauses, creating a practical bridge to later grounded generation and agentic workflows. In an ICM context, a reviewed classifier could help route contract language to appropriate templates, prior findings, quality checks, or subject-matter reviewers.

## Dataset

- **Dataset:** Contract Understanding Atticus Dataset (CUAD) v1
- **Official project page:** https://www.atticusprojectai.org/cuad/
- **Archived release:** https://doi.org/10.5281/zenodo.4595826
- **Original corpus:** 510 commercial contracts, more than 13,000 expert-supervised labels, and 41 clause categories
- **Final experiment dataset:** 4,356 unique passages from 462 contracts across ten selected categories
- **Splits:** 3,486 training passages, 435 validation passages, and 435 test passages
- **Leakage control:** all passages from a source contract remain in one split

The processed dataset is stored at `data/processed/cuad_clause_classification.csv`. Source, license, adaptation, field definitions, and audit methods are documented under `data/`.

## Model and controlled experiment

The custom classifier uses learned token and positional embeddings, two Transformer encoder layers, four attention heads, a 256-unit feed-forward sublayer with GELU activation, padding-aware mean pooling, and a ten-class linear output. The training vocabulary contains 4,417 entries, the maximum sequence length is 256 tokens, and the model has 864,650 trainable parameters.

Exactly one major condition changes:

| Configuration | Dropout | Other conditions |
|---|---:|---|
| Baseline | 0.10 | Held constant |
| Experimental | 0.30 | Held constant |

Both configurations use the same processed records, vocabulary, initial parameter values, shuffled batch order, architecture dimensions, AdamW optimizer, learning rate, weight decay, gradient clipping, batch size, 15 epochs, and validation checkpoint rule.

## Final results

| Metric | Baseline 0.10 | Experimental 0.30 |
|---|---:|---:|
| Validation macro F1 | **0.8878** | 0.8842 |
| Validation accuracy | **0.9011** | 0.8966 |
| Test macro F1 | 0.8471 | **0.8530** |
| Test accuracy | 0.8690 | **0.8736** |
| Test weighted F1 | 0.8628 | **0.8689** |
| Test loss | **0.6410** | 0.7086 |

Validation selected the baseline, while the untouched test set modestly favored the experimental configuration by 0.0059 macro F1. Both models showed overfitting: training loss approached zero while validation loss increased after early epochs. The result supports a cautious conclusion that dropout 0.30 produced comparable performance with a small test advantage, not a definitive improvement.

## Key limitations

- CUAD contains commercial-contract language and may not represent public-sector contracting or ICM-specific documents.
- Only ten of the original 41 categories were modeled.
- The experiment used one random seed and one contract-grouped split.
- Eight test passages were truncated at 256 tokens.
- High-confidence errors show that model confidence is not equivalent to legal certainty.
- Outputs require human review and should not determine legal, procurement, or pursuit actions automatically.

## How to run

### Google Colab

1. Open `deep_learning.ipynb` using the Colab badge above.
2. Select **Runtime -> Change runtime type -> T4 GPU**.
3. Choose **Run all**.
4. The notebook loads the processed dataset from this public repository and runs top to bottom.
5. The final reproducibility cell creates `requirements.txt` using `python -m pip freeze > requirements.txt`.

### Local environment

Use the portable project dependency set for local execution:

```bash
git clone https://github.com/icmsol/capstone-project-4-deep-learning-systems.git
cd capstone-project-4-deep-learning-systems
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements_minimal.txt
jupyter lab deep_learning.ipynb
```

A CUDA-capable GPU is recommended for reproducing the recorded training runtime, although the notebook includes a CPU fallback. For local GPU execution, install the PyTorch build that matches the operating system, GPU driver, and CUDA environment.

### Dependency files

- `requirements.txt` is the exact 703-package Google Colab environment snapshot produced by the final T4 run using `python -m pip freeze`. It is retained for rubric compliance, auditability, and archival reproducibility. Because it includes Colab-, CUDA-, and hosted-runtime-specific packages, it is not intended as a universal local installation file.
- `requirements_minimal.txt` contains the portable project-relevant dependencies recommended for a new local environment.

## Repository structure

The fully executed repository-root `deep_learning.ipynb` is the sole authoritative submission notebook. The `notebooks/` directory is retained for organization and documentation without a conflicting duplicate copy.

```text
.
├── deep_learning.ipynb
├── Deep_Learning_Systems_Analysis_Report.pdf
├── module_summary.pdf
├── requirements.txt
├── requirements_minimal.txt
├── README.md
├── SUBMISSION_CHECKLIST.md
├── config/
│   ├── README.md
│   └── experiment_configuration.json
├── data/
│   ├── README.md
│   ├── DATASET_SOURCE.md
│   ├── DATA_DICTIONARY.md
│   ├── audit/
│   └── processed/cuad_clause_classification.csv
├── figures/
│   ├── README.md
│   └── final report figures
├── notebooks/
│   └── README.md
├── reports/
│   ├── README.md
│   ├── Deep_Learning_Systems_Analysis_Report.pdf
│   └── module_summary.pdf
└── src/
    ├── README.md
    ├── prepare_cuad_classification.py
    └── design and evaluation protocols
```

## Written analysis report

The completed report is provided under both filenames referenced by the project materials:

- `Deep_Learning_Systems_Analysis_Report.pdf`
- `module_summary.pdf`

The files contain identical content and cover the dataset, model architecture, controlled experiment, results, observed behavior, limitations, responsible use, future improvements, and APA-style references.

## License and attribution

Repository code and original project documentation are released under the MIT License. CUAD remains subject to its original dataset license and attribution requirements; see `data/DATASET_SOURCE.md` for details.
