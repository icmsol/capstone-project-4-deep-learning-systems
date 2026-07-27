# Training and Checkpoint Protocol

## Purpose

This protocol governs the pilot and full controlled experiment for the CUAD clause-theme Transformer.

## Common training conditions

- Random seed: 42
- Batch size: 64
- Loss: unweighted cross-entropy
- Optimizer: AdamW
- Learning rate: 0.0005
- Weight decay: 0.01
- Gradient clipping: 1.0
- Scheduler: none
- Early stopping: disabled
- Full epochs per configuration: 15
- Device: CUDA when available, with CPU fallback

## Controlled comparison

- Baseline dropout: 0.10
- Experimental dropout: 0.30
- Dropout probability is the only major difference.
- Both runs recreate the model from the same global seed.
- Both runs recreate the training DataLoader from the same generator seed.
- Vocabulary, encoded records, batches, architecture dimensions, optimizer, learning rate, epochs, metrics, and checkpoint rule remain identical.

## Checkpoint rule

The selected checkpoint is the epoch with the highest validation macro F1. If two epochs have macro F1 values equal within numerical tolerance, the lower validation loss wins.

The test set is not used for checkpoint selection or pilot assessment.

## Pilot

The pilot runs the baseline configuration for three epochs to validate mechanics, runtime, memory, and learning behavior. Pilot weights are discarded and never used as final baseline weights.

Readiness gates:

1. Numeric history remains finite.
2. Training loss decreases.
3. The best checkpoint restores correctly.
4. Validation macro F1 exceeds a training-majority reference.
5. Peak GPU memory remains below 12 GB on a T4.

## Full experiment

Each formal configuration runs all 15 epochs. No early stopping is used. Complete histories and the best validation-selected checkpoint are retained for direct comparison and final test evaluation.
