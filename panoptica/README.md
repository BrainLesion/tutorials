# Panoptica Tutorials

This folder contains several Jupyter notebooks to showcase different possible use cases of the [panoptica package](https://github.com/BrainLesion/panoptica).
The package allows to compute instance-wise segmentation quality metrics for 2D and 3D semantic- and instance segmentation maps by providing 3 core modules:

1. Instance Approximator: instance approximation algorithms in panoptic segmentation evaluation. Available now: connected components algorithm.
1. Instance Matcher: instance matching algorithm in panoptic segmentation evaluation, to align and compare predicted instances with reference instances.
1. Panoptic Evaluator: Evaluation of panoptic segmentation performance by evaluating matched instance pairs and calculating various metrics like true positives, Dice score, IoU, and ASSD for each instance.

## Use Cases

### Semantic Segmentation Input

<img src="https://github.com/BrainLesion/panoptica/blob/main/examples/figures/semantic.png?raw=true" alt="semantic_figure" height="300"/>

Although for many biomedical segmentation problems, an instance-wise evaluation is highly relevant and desirable, they are still addressed as semantic segmentation problems due to lack of appropriate instance labels.

Modules [1-3] can be used to obtain panoptic metrics of matched instances based on a semantic segmentation input.

[Jupyter Notebook Example](https://github.com/BrainLesion/tutorials/tree/main/panoptica/example_spine_semantic.ipynb)

### Unmatched Instances Input

<img src="https://github.com/BrainLesion/panoptica/blob/main/examples/figures/unmatched_instance.png?raw=true" alt="unmatched_instance_figure" height="300"/>

It is a common issue that instance segementation outputs have good segmentations with mismatched labels.

For this case modules [2-3] can be utilized to match the instances and report panoptic metrics.

[Jupyter Notebook Example](https://github.com/BrainLesion/tutorials/tree/main/panoptica/example_spine_unmatched_instance.ipynb)

### Matched Instances Input

<img src="https://github.com/BrainLesion/panoptica/blob/main/examples/figures/matched_instance.png?raw=true" alt="matched_instance_figure" height="300"/>

Ideally the input data already provides matched instances.

In this case module 3 can be used to directly report panoptic metrics without requiring any internal preprocessing.

[Jupyter Notebook Example](https://github.com/BrainLesion/tutorials/tree/main/panoptica/example_spine_matched_instance.ipynb)
