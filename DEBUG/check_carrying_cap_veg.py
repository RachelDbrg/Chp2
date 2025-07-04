## Script to test that the carrying capacities of herbivores is linked with vegetation abundance

import matplotlib.pyplot as plt

def plot_V1_and_kH1(V1, k_H1, Lx, Ly, time_label=None, save_path=None):
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # Plot V1
    im1 = axes[0].imshow(V1, extent=[0, Lx, 0, Ly], origin="lower", cmap="Greens")
    axes[0].set_title(f"Lichen (V1) at t = {time_label}" if time_label else "Lichen (V1)")
    axes[0].set_xlabel("x")
    axes[0].set_ylabel("y")
    fig.colorbar(im1, ax=axes[0])

    # Plot k_H1
    if np.isscalar(k_H1):
        k_H1 = np.full_like(V1, k_H1)  # broadcast scalar to 2D
    elif k_H1.ndim == 1:
        k_H1 = k_H1.reshape(V1.shape)  # reshape if needed

    im2 = axes[1].imshow(k_H1, extent=[0, Lx, 0, Ly], origin="lower", cmap="Blues")
    axes[1].set_title(f"Carrying Capacity (k_H1) at t = {time_label}" if time_label else "k_H1")
    axes[1].set_xlabel("x")
    axes[1].set_ylabel("y")
    fig.colorbar(im2, ax=axes[1])

    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches="tight")
    else:
        plt.show()

    plt.close()
