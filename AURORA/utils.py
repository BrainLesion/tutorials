import matplotlib.pyplot as plt
import nibabel as nib


def visualize_results(t1_file: str, segmentation_file: str):
    t1_np = nib.load(t1_file).get_fdata().transpose(2, 1, 0)
    seg_np = nib.load(segmentation_file).get_fdata().transpose(2, 1, 0)
    _, ax = plt.subplots(1, 2, figsize=(8, 4))

    slice_index = t1_np.shape[0] // 2  # You can choose any slice here
    ax[0].imshow(t1_np[slice_index, :, :], cmap="gray")
    ax[1].imshow(t1_np[slice_index, :, :], cmap="gray")
    ax[1].imshow(seg_np[slice_index, :, :], cmap="plasma", alpha=0.3)
    for ax in ax:
        ax.axis("off")
    plt.tight_layout()
