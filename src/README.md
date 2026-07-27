# Source and Protocol Documentation

This directory documents the reproducible implementation decisions behind the notebook:

- `prepare_cuad_classification.py` - builds the processed classification dataset.
- `MODEL_ARCHITECTURE.md` - tokenizer, data pipeline, and Transformer design.
- `TRAINING_PROTOCOL.md` - pilot, optimizer, checkpoint, and training rules.
- `CONTROLLED_EXPERIMENT.md` - equivalence controls and the one-variable dropout comparison.
- `EVALUATION_PROTOCOL.md` - frozen-checkpoint test evaluation and error-analysis rules.

The notebook contains the executable implementation; these files provide concise design and governance records for reviewers and future reuse.
