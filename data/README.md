# Data

This directory contains the processed CUAD clause-classification dataset and the documentation required to reproduce and audit its construction.

## Contents

- `processed/cuad_clause_classification.csv` - 4,356 clean, single-label passages across ten categories.
- `DATASET_SOURCE.md` - official source, archived release, attribution, license, and task adaptation.
- `DATA_DICTIONARY.md` - field definitions for the processed dataset.
- `audit/AUDIT_METHOD.md` - duplicate, conflict, category-selection, and contract-grouped splitting controls.
- `audit/cuad_data_audit_summary.json` - source and processed-record counts.
- `audit/cuad_selected_category_audit.csv` - selected category evidence.
- `audit/cuad_split_distribution.csv` - split distribution evidence.

The final split is grouped by source contract to prevent clauses from the same contract appearing in more than one partition. The dataset is loaded directly from the public repository by `deep_learning.ipynb`.
