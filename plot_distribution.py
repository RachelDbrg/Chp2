# Function that plots the densities of species at defined time steps

def plot_species_distribution(field, Lx, Ly, species_name="", save_path=None, time_label=None):
    import matplotlib.pyplot as plt

    plt.figure()
    plt.imshow(field, extent=[0, Lx, 0, Ly], origin="lower", cmap="viridis")
    
    if time_label is not None:
        plt.title(f"{species_name} Distribution at t = {time_label}")
    else:
        plt.title(f"{species_name} Distribution")
    
    plt.xlabel("x")
    plt.ylabel("y")
    plt.colorbar()

    if save_path:
        if time_label:
            save_path = save_path.replace(".png", f"_t{time_label}.png")
        plt.savefig(save_path, bbox_inches="tight", dpi=300)
    else:
        plt.show()

    plt.close()


def plot_initial_species_distribution(V1, V2, H1, H2, P,
                                      k_V1, k_V2, barrier_mask,
                                      Lx, Ly, timestamp,
                                      plot_species_distribution_fn):
    import os
    import numpy as np

    # Create output folder for initial distribution plots
    plot_dir = os.path.join("outputs", timestamp, "initial_distribution")
    os.makedirs(plot_dir, exist_ok=True)

    t_idx = 0  # Time label for initial snapshot

    # Extract individual fields
    species_fields = {
        "Deciduous": V2,
        "Lichen": V1,
        "Caribou": H1,
        "Moose": H2,
        "Predator": P,
        "Barrier": barrier_mask,
        "k_V2": k_V2,
        "k_V1": k_V1
    }

    # Plot non-zero fields
    for species_name, field in species_fields.items():
        if np.any(field != 0):
            filename = os.path.join(plot_dir, f"{species_name}.png")
            plot_species_distribution_fn(
                field,
                Lx, Ly,
                species_name=species_name,
                save_path=filename,
                time_label=t_idx
            )
