# Processed CUAD Classification Dataset — Data Dictionary

File: `data/processed/cuad_clause_classification.csv`

| Field | Type | Description |
|---|---|---|
| `example_id` | string | Deterministic project-specific identifier for one retained clause passage. |
| `contract_id` | string | Identifier or filename of the source CUAD contract. Used as the grouping key for leakage-resistant splitting. |
| `category` | string | Human-readable CUAD clause-theme label used as the classification target. |
| `label_id` | integer | Zero-based numeric encoding of `category`, ranging from 0 through 9. |
| `clause_text` | string | Original expert-annotated clause passage retained for model input. |
| `normalized_text_sha256` | string | SHA-256 hash of normalized text used for duplicate and conflicting-label controls. It is not a model feature. |
| `word_count` | integer | Preliminary whitespace-delimited word count used for structural and length analysis. |
| `char_count` | integer | Character count of the retained original passage. |
| `fold` | integer | Contract-grouped fold assignment from the reproducible split procedure. |
| `split` | string | Final partition: `train`, `validation`, or `test`. |

## Target categories

| Label ID | Category |
|---:|---|
| 0 | Audit Rights |
| 1 | Anti-Assignment |
| 2 | Insurance |
| 3 | Cap On Liability |
| 4 | Governing Law |
| 5 | Revenue/Profit Sharing |
| 6 | Minimum Commitment |
| 7 | Post-Termination Services |
| 8 | License Grant |
| 9 | Ip Ownership Assignment |

## Modeling controls

- `contract_id`, `example_id`, hashes, counts, folds, and split names are never used as predictive inputs.
- Vocabulary construction uses only the training split.
- Validation data selects checkpoints.
- Test data remains untouched until both model configurations are frozen.
- All passages from one contract remain in one split.
