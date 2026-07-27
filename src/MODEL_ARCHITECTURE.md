# Text Pipeline and Transformer Architecture

## Task

Ten-class, single-label classification of expert-annotated CUAD contract clause passages.

## Leakage controls

- The vocabulary is fitted only on training passages.
- Validation and test tokens absent from the training vocabulary map to `<UNK>`.
- All passages from one contract remain in one split.
- The same vocabulary and encoded data are reused for the baseline and controlled experiment.

## Tokenization

The tokenizer lowercases text and separates:

- Alphabetic words, including simple apostrophe forms
- Numeric expressions
- Punctuation symbols

Legal terms, punctuation, and numbers are retained. Sequences are padded or truncated to 256 tokens.

## PyTorch data pipeline

- `CUADClauseDataset` returns token IDs, a Boolean attention mask, a numeric label, and an example ID.
- Batch size: 64
- Training DataLoader: shuffled with a seed-controlled `torch.Generator`
- Validation and test DataLoaders: deterministic, unshuffled
- `num_workers=0` for Colab portability and reproducibility
- Pinned memory is enabled when CUDA is available

## Baseline Transformer

- Token embeddings: learned
- Positional embeddings: learned
- Embedding dimension: 128
- Encoder layers: 2
- Attention heads: 4
- Feed-forward dimension: 256
- Activation: GELU
- Pooling: padding-mask-aware mean
- Output: linear ten-class classifier
- Baseline dropout: 0.10
- Experimental dropout: 0.30

The dropout probability is the only major change between configurations.

## Optimization design

- Loss: unweighted cross-entropy
- Optimizer: AdamW
- Learning rate: 0.0005
- Weight decay: 0.01
- Gradient clipping: 1.0
- Epochs: 15
- Primary checkpoint criterion: highest validation macro F1
- Tie-breaker: lower validation loss

The Phase 7 notebook includes a one-batch forward/backward check using a temporary model. That model is discarded so formal training starts from a fresh seed-controlled initialization.
