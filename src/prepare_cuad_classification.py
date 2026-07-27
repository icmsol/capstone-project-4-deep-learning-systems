#!/usr/bin/env python3
"""Prepare the CUAD multiclass clause-classification dataset used in Capstone Project 4."""

from __future__ import annotations

import argparse
import ast
import hashlib
import re
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.model_selection import StratifiedGroupKFold

NON_THEME_LABELS = [
    "Document Name",
    "Parties",
    "Agreement Date",
    "Effective Date",
    "Expiration Date",
]
RANDOM_SEED = 42


def parse_list_cell(value: object) -> list[str]:
    if pd.isna(value):
        return []
    text = str(value).strip()
    if not text:
        return []
    try:
        parsed = ast.literal_eval(text)
    except (ValueError, SyntaxError):
        parsed = [text]
    if isinstance(parsed, list):
        return [str(item).strip() for item in parsed if str(item).strip()]
    if isinstance(parsed, str):
        return [parsed.strip()] if parsed.strip() else []
    return [str(parsed).strip()]


def main(source_csv: Path, output_csv: Path) -> None:
    source = pd.read_csv(source_csv)
    context_columns = [
        column
        for column in source.columns
        if column != "Filename" and "Answer" not in column
    ]

    rows: list[dict[str, object]] = []
    for source_row, row in source.iterrows():
        contract_id = str(row["Filename"]).strip()
        for category in context_columns:
            for item_index, clause_text in enumerate(parse_list_cell(row[category])):
                normalized = re.sub(r"\s+", " ", clause_text).strip().lower()
                rows.append(
                    {
                        "contract_id": contract_id,
                        "category": category,
                        "clause_text": clause_text,
                        "normalized_text": normalized,
                        "source_row": int(source_row),
                        "item_index": int(item_index),
                    }
                )

    records = pd.DataFrame(rows)
    records["word_count"] = records["clause_text"].str.split().str.len().astype(int)
    records["char_count"] = records["clause_text"].str.len().astype(int)

    category_counts = records.groupby("normalized_text")["category"].nunique()
    ambiguous_texts = set(category_counts[category_counts > 1].index)

    clean = (
        records.sort_values(
            ["category", "normalized_text", "contract_id", "source_row", "item_index"]
        )
        .drop_duplicates(["category", "normalized_text"], keep="first")
    )
    clean = clean[~clean["normalized_text"].isin(ambiguous_texts)].copy()

    eligible = (
        clean[~clean["category"].isin(NON_THEME_LABELS)]
        .groupby("category")
        .agg(
            clean_unique_passages=("normalized_text", "nunique"),
            distinct_contracts=("contract_id", "nunique"),
        )
        .reset_index()
    )
    selected_categories = (
        eligible[eligible["distinct_contracts"] >= 100]
        .sort_values(
            ["clean_unique_passages", "category"],
            ascending=[False, True],
        )
        .head(10)["category"]
        .tolist()
    )

    model_data = (
        clean[clean["category"].isin(selected_categories)]
        .sort_values(["contract_id", "category", "normalized_text"])
        .reset_index(drop=True)
    )

    splitter = StratifiedGroupKFold(
        n_splits=10,
        shuffle=True,
        random_state=RANDOM_SEED,
    )
    folds = np.empty(len(model_data), dtype=np.int64)
    for fold_id, (_, holdout_indices) in enumerate(
        splitter.split(
            model_data,
            y=model_data["category"],
            groups=model_data["contract_id"],
        )
    ):
        folds[holdout_indices] = fold_id

    model_data["fold"] = folds
    model_data["split"] = model_data["fold"].map(
        {**{fold: "train" for fold in range(8)}, 8: "validation", 9: "test"}
    )
    label_map = {category: label for label, category in enumerate(selected_categories)}
    model_data["label_id"] = model_data["category"].map(label_map).astype(int)
    model_data["normalized_text_sha256"] = model_data["normalized_text"].map(
        lambda text: hashlib.sha256(text.encode("utf-8")).hexdigest()
    )
    model_data["example_id"] = [
        f"cuad_{index:05d}" for index in range(1, len(model_data) + 1)
    ]

    output_columns = [
        "example_id",
        "contract_id",
        "category",
        "label_id",
        "clause_text",
        "normalized_text_sha256",
        "word_count",
        "char_count",
        "fold",
        "split",
    ]
    output_csv.parent.mkdir(parents=True, exist_ok=True)
    model_data[output_columns].to_csv(output_csv, index=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("source_csv", type=Path)
    parser.add_argument("output_csv", type=Path)
    args = parser.parse_args()
    main(args.source_csv, args.output_csv)
