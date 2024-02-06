import os
import matplotlib.pyplot as plt
import nibabel as nib

DATA_FOLDER = "data"


def visualize_data(data_folder: str = DATA_FOLDER, slice_index: int = 75):
    """Visualize the MRI modalities for a given slice index

    Args:
        data_folder (str, optional): Path to the folder containing the t1, t1c, t2 & flair file. Defaults to DATA_FOLDER.
        slice_index (int, optional): Slice to be visualized (first index in data of shape (155, 240, 240)). Defaults to 75.
    """
    _, axes = plt.subplots(1, 4, figsize=(12, 10))

    modalities = ["t1", "t1c", "t2", "flair"]
    for i, mod in enumerate(modalities):
        modality_file = os.path.join(data_folder, f"{mod}.nii.gz")
        modality_np = nib.load(modality_file).get_fdata().transpose(2, 1, 0)
        axes[i].set_title(mod)
        axes[i].imshow(modality_np[slice_index, :, :], cmap="gray")
        axes[i].axis("off")


def visualize_segmentation(modality_file: str, segmentation_file: str):
    modality_np = nib.load(modality_file).get_fdata().transpose(2, 1, 0)
    seg_np = nib.load(segmentation_file).get_fdata().transpose(2, 1, 0)
    _, ax = plt.subplots(1, 2, figsize=(8, 4))

    slice_index = modality_np.shape[0] // 2  # You can choose any slice here
    ax[0].imshow(modality_np[slice_index, :, :], cmap="gray")
    ax[1].imshow(modality_np[slice_index, :, :], cmap="gray")
    ax[1].imshow(seg_np[slice_index, :, :], cmap="plasma", alpha=0.3)
    for ax in ax:
        ax.axis("off")
    plt.tight_layout()
