# Full Controlled Experiment Protocol

## Configurations

| Configuration | Dropout |
|---|---:|
| Baseline | 0.10 |
| Experimental | 0.30 |

Dropout is the only major difference.

## Equivalence controls

The notebook verifies matching parameter names, shapes, initial tensors, first shuffled batch IDs, encoded inputs, and labels before training. Temporary audit objects are then discarded.

## Shared conditions

- Same CUAD records and contract-grouped splits
- Same training-only vocabulary and tokenizer
- Same 256-token maximum
- Same Transformer dimensions
- Same seed: 42
- Same batch size: 64
- Same 15 epochs
- Same cross-entropy loss and AdamW optimizer
- Same learning rate: 0.0005
- Same weight decay: 0.01
- Same gradient clipping: 1.0
- No scheduler or early stopping
- Same checkpoint rule

## Checkpoint selection

Highest validation macro F1 wins. Lower validation loss breaks ties.

## Test control

The test split is not evaluated until both validation-selected checkpoints are frozen.
