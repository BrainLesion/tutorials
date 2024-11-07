from pathlib import Path
from typing import List, Optional
import matplotlib.pyplot as plt
import nibabel as nib


def visualize_data(files: List[Path], label: str, titles: Optional[List[str]] = None):
    """Visualize the MRI modalities

    Args:
        files (List[Path]): List of paths to the MRI modalities
        label (str): Label for the y-axis on the far left left, i.e. category of the passed images (e.g. input, output)
        titles (Optional[List[str]], optional): Title of images. Defaults to None.
    """
    _, axes = plt.subplots(1, len(files), figsize=(len(files) * 4, 10))

    for i, file in enumerate(files):
        modality_np = nib.load(file).get_fdata().transpose(2, 1, 0)
        axes[i].set_title(titles[i] if titles else file.name)
        axes[i].imshow(modality_np[modality_np.shape[0] // 2, :, :], cmap="gray")
    axes[0].set_ylabel(label)


def visualize_defacing(
    file: Path,
):
    """Visualize the defacing of the MRI modality

    Args:
        file (Path): Path to the MRI modality
    """

    modality_np = nib.load(file).get_fdata().transpose(2, 1, 0)
    plt.figure(figsize=(6, 6))
    plt.title(file.name)
    plt.imshow(modality_np[:, ::-1, 75], cmap="gray", origin="lower")
