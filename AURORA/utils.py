import matplotlib.pyplot as plt
import nibabel as nib


def visualize_results(modality_file: str, segmentation_file: str):
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
