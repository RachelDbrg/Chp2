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
