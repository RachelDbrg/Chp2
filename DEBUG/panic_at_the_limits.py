import numpy as np
import matplotlib.pyplot as plt

def check_total_mass_over_time(logged_data, species="H1"):
    """Plot total mass (sum) of a species over time."""
    if species not in logged_data:
        raise ValueError(f"{species} not in logged_data")
    data = logged_data[species]
    times = [t for t, _ in data]
    masses = [np.sum(field) for _, field in data]
    
    plt.plot(times, masses)
    plt.title(f"Total mass of {species} over time")
    plt.xlabel("Time")
    plt.ylabel(f"Σ{species}")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def inspect_boundary_cells(H, label="H1"):
    """Print min/max values on edges of a grid."""
    top, bottom = H[0, :], H[-1, :]
    left, right = H[:, 0], H[:, -1]
    
    print(f"[{label}] Top row: min={top.min():.2f}, max={top.max():.2f}")
    print(f"[{label}] Bottom row: min={bottom.min():.2f}, max={bottom.max():.2f}")
    print(f"[{label}] Left col: min={left.min():.2f}, max={left.max():.2f}")
    print(f"[{label}] Right col: min={right.min():.2f}, max={right.max():.2f}")

def detect_flux_leakage(flux_x, flux_y, label="H1"):
    """Check flux values at domain boundaries."""
    print(f"[{label}] Flux X (left/right): {flux_x[:, 0].mean():.3e}, {flux_x[:, -1].mean():.3e}")
    print(f"[{label}] Flux Y (top/bottom): {flux_y[0, :].mean():.3e}, {flux_y[-1, :].mean():.3e}")
