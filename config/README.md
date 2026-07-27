# Configuration

`experiment_configuration.json` records the dataset, architecture, training, and controlled-comparison settings locked before formal model training. The notebook loads and validates this file so documented settings cannot silently diverge from the executed experiment.

The baseline uses dropout 0.10 and the experimental configuration uses dropout 0.30. All other major conditions remain fixed.
