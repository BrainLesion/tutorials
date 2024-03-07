import os
import matplotlib.pyplot as plt
import nibabel as nib
from pathlib import Path

    
def visualize_data2(t1c, t1, t2, flair, height_p = 0.5):    #
    """Visualize the MRI modalities. This function is different from "visualize_data" in the following ways:
    	a) it expects the four file paths directly (no naming convention required)
    	b) it does not take a slice index but a percentage height (e.g. 0.5 = 50% = middle slice) as imputs may have different dimensions

    Args:
    	height_p (float, optional): the percentage of slicing height. 0.5 means 50% means exactly in the middle of the cuboid
        slice_index (int, optional): Slice to be visualized (first index in data of shape (155, 240, 240)). Defaults to 75.
    """
    _, axes = plt.subplots(1, 4, figsize=(12, 10))

    for i, (mod, modality_file) in enumerate([("t1",t1), ("t1c",t1c), ("t2",t2), ("flair",flair)]):
    
        data = nib.load(modality_file).get_fdata()
         # Get the middle slice along the specified axis
        slice_index = int(data.shape[2] * height_p)  # show slice that is exactly in the middle
        slice_data = data[:, ::-1, slice_index].T
        
        axes[i].set_title(mod)
        axes[i].imshow(slice_data, cmap="gray")
        axes[i].axis("off")

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

def visualize_segmentation(modality_file: str, segmentation_file: str, slice_p = 0.5):
    """Visualize the MRI modality and the segmentation

    Args:
        modality_file (str): Path to the desired modality file
        segmentation_file (str): Path to the segmentation file
    """
    modality_np = nib.load(modality_file).get_fdata().transpose(2, 1, 0)
    seg_np = nib.load(segmentation_file).get_fdata().transpose(2, 1, 0)
    _, ax = plt.subplots(1, 2, figsize=(8, 4))

    slice_index = int(modality_np.shape[0] * slice_p)  # You can choose any slice here
    ax[0].imshow(modality_np[slice_index, :, :], cmap="gray")
    ax[1].imshow(modality_np[slice_index, :, :], cmap="gray")
    ax[1].imshow(seg_np[slice_index, :, :], cmap="plasma", alpha=0.5)
    for ax in ax:
        ax.axis("off")
    plt.tight_layout()
    

