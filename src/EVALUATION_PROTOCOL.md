# Final Evaluation Protocol

## Frozen checkpoints
Both models are selected using validation macro F1 before final test evaluation.

## Test use
The same untouched 435-record test split is evaluated once for each frozen checkpoint. Test results are not used to tune the model.

## Metrics
Aggregate metrics: loss, accuracy, macro precision, macro recall, macro F1, and weighted F1.

Class-level evidence: precision, recall, F1, support, count confusion matrices, normalized confusion matrices, and frequent confusion pairs.

Behavioral evidence: representative correct predictions, high-confidence errors, truncation-related cases, and model disagreements.

## Interpretation boundary
Small differences are interpreted cautiously because the project uses one test split and one random seed, without confidence intervals or repeated-seed significance testing.
