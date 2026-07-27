# Dataset Source and Attribution

## Dataset

This project uses the **Contract Understanding Atticus Dataset (CUAD) v1**, an expert-annotated corpus for legal contract review.

- Official dataset overview: https://www.atticusprojectai.org/cuad/
- Archived release: https://zenodo.org/records/4595826
- DOI: https://doi.org/10.5281/zenodo.4595826
- Official GitHub repository: https://github.com/TheAtticusProject/cuad
- Associated paper: *CUAD: An Expert-Annotated NLP Dataset for Legal Contract Review* (NeurIPS 2021)
- Dataset license: Creative Commons Attribution 4.0 International (CC BY 4.0)

The official CUAD v1 release contains 510 commercial contracts and more than 13,000 expert-supervised annotations across 41 clause categories.

## Source file used

The reproducible preparation workflow starts from:

`CUAD_v1/master_clauses.csv`

The master file contains one source-contract row and paired context/answer columns for each CUAD category. The project extracts the expert-annotated answer passages and preserves the source contract identifier and category.

## Capstone adaptation

CUAD was designed primarily for identifying legally significant passages within complete contracts. This capstone transparently adapts the expert-annotated passages into a ten-class, single-label text-classification task.

The model receives a passage that has already been identified as relevant and predicts its clause theme. It does not locate every relevant provision in a complete contract, provide legal advice, determine contract acceptability, or replace professional review.

## ICM Solutions relevance

The experiment demonstrates a document-theme classification capability that could later support ICM Solutions knowledge-management and quality-review workflows. With authorized domain-specific data and human validation, a future system could classify passages from contracts, work authorizations, RFPs, statements of work, IV&V deliverables, test plans, and project-management artifacts before retrieving related checklists, standards, examples, or reusable language.

The CUAD-trained academic model is not assumed to generalize directly to California public-sector documents or confidential ICM/client content.

## Repository data

The repository includes the processed project-specific classification table and documented access to the original source. It does not redistribute the complete CUAD archive.

CUAD attribution and license terms apply independently from the MIT license used for this project's original code.
