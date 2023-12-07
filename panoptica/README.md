# Panoptica Tutorials

This folder contains several Jupyter notebooks to showcase different possible use cases of the [panoptica package](https://github.com/BrainLesion/panoptica).
The package allows to compute instance-wise segmentation quality metrics for 2D and 3D semantic- and instance segmentation maps by providing 3 core modules:

1. Instance Approximator: instance approximation algorithms in panoptic segmentation evaluation. Available now: connected components algorithm.
1. Instance Matcher: instance matching algorithm in panoptic segmentation evaluation, to align and compare predicted instances with reference instances.
1. Instance Evaluator: Evaluation of panoptic segmentation performance by evaluating matched instance pairs and calculating various metrics like true positives, Dice score, IoU, and ASSD for each instance.

![workflow_figure](https://github.com/BrainLesion/panoptica/blob/main/examples/figures/workflow.png)

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

## Citation

If you use panoptica in your research, please cite it to support the development!

Kofler, F., Möller, H., Buchner, J. A., de la Rosa, E., Ezhov, I., Rosier, M., Mekki, I., Shit, S., Negwer, M., Al-Maskari, R., Ertürk, A., Vinayahalingam, S., Isensee, F., Pati, S., Rueckert, D., Kirschke, J. S., Ehrlich, S. K., Reinke, A., Menze, B., Wiestler, B., & Piraud, M. (2023). _Panoptica -- instance-wise evaluation of 3D semantic and instance segmentation maps._ [arXiv preprint arXiv:2312.02608](https://arxiv.org/abs/2312.02608).

```
@misc{kofler2023panoptica,
      title={Panoptica -- instance-wise evaluation of 3D semantic and instance segmentation maps},
      author={Florian Kofler and Hendrik Möller and Josef A. Buchner and Ezequiel de la Rosa and Ivan Ezhov and Marcel Rosier and Isra Mekki and Suprosanna Shit and Moritz Negwer and Rami Al-Maskari and Ali Ertürk and Shankeeth Vinayahalingam and Fabian Isensee and Sarthak Pati and Daniel Rueckert and Jan S. Kirschke and Stefan K. Ehrlich and Annika Reinke and Bjoern Menze and Benedikt Wiestler and Marie Piraud},
      year={2023},
      eprint={2312.02608},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```
