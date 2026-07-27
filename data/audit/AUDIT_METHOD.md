# CUAD Structural Audit and Classification Adaptation

## Purpose

This audit documents how the official CUAD v1 annotations were transformed into a reproducible, single-label, ten-class clause-theme classification dataset.

## Source dimensions

- Source contracts: 510
- Source columns in `master_clauses.csv`: 83
- Clause categories: 41
- Raw annotated clause passages extracted: 13,101

## Cleaning rules

1. Preserve the original expert-annotated passage for model input.
2. Normalize whitespace and letter case only for duplicate and conflict detection.
3. Within a category, retain one deterministic representative of identical normalized text.
4. Remove every identical normalized passage assigned to more than one category because this capstone uses a single-label output.
5. Exclude blank or unparsable passages.
6. Do not remove legal wording, punctuation, numbers, or contract-specific language from `clause_text`.

## Duplicate and conflict audit

- Normalized text values appearing more than once: 1,336
- Rows in any duplicate group: 3,393
- Normalized text values assigned to multiple categories: 1,063
- Rows affected by multiple-category conflicts: 2,344
- Clean unique passages remaining across all 41 categories: 9,981

## Category-selection rule

1. Exclude the metadata-oriented labels `Document Name`, `Parties`, `Agreement Date`, `Effective Date`, and `Expiration Date`.
2. Require at least 100 distinct source contracts after cleaning.
3. Rank eligible categories by clean unique passage count.
4. Break count ties alphabetically.
5. Retain the ten highest-ranked categories.

This rule was fixed before any model training or validation/test evaluation.

## Final dataset

- Passages: 4,356
- Source contracts: 462
- Classes: 10
- Training: 3,486 passages from 368 contracts
- Validation: 435 passages from 48 contracts
- Test: 435 passages from 46 contracts

## Split method

The preparation script uses contract-grouped stratification. All passages from a source contract remain in one partition, which reduces leakage from repeated or stylistically similar language within the same contract.

## Length profile

- Mean word count: approximately 55
- Median word count: 43
- 95th percentile: 136
- Maximum: 704
- Passages above the preliminary 256-word proxy: 36, or approximately 0.83%

The final model uses a maximum length of 256 tokens. Exact tokenizer-based truncation will be measured after the training-only vocabulary is created.

## Reproducibility

The complete transformation is implemented in:

`src/prepare_cuad_classification.py`

The formal configuration is stored in:

`config/experiment_configuration.json`

Audit outputs are stored in:

- `data/audit/cuad_data_audit_summary.json`
- `data/audit/cuad_selected_category_audit.csv`
- `data/audit/cuad_split_distribution.csv`
