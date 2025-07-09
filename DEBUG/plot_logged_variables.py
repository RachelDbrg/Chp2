import numpy as np
import matplotlib.pyplot as plt
import os
import pickle

# === CONFIGURATION ===
# Load your logged_data dictionary from a saved file
# Replace this with your actual path if needed
LOG_FILE = "DEBUG/logged_data.pkl"

# Choose which variable to visualize
VARIABLE = "eta_H1"  # e.g., "Dm_eff_P", "score_G_H1", etc.

# Plot settings
PLOT_TYPE = "max"  # Options: "mean", "max", "center", "heatmap"
FRAME_INTERVAL = 100  # For heatmap animation: plot every Nth frame

# === LOAD LOGGED DATA ===
if not os.path.exists(LOG_FILE):
    raise FileNotFoundError(f"Could not find {LOG_FILE}. Make sure you saved logged_data.")

with open(LOG_FILE, "rb") as f:
    logged_data = pickle.load(f)

if VARIABLE not in logged_data:
    raise ValueError(f"{VARIABLE} not found in logged_data. Available keys: {list(logged_data.keys())}")

# === EXTRACT TIME SERIES ===
entries = logged_data[VARIABLE]

print(f"{VARIABLE} has {len(entries)} entries")

# Handle (time, field) tuples
times = [entry[0] for entry in entries]
values = [entry[1] for entry in entries]

# Determine if values are scalar or 2D fields
is_field = isinstance(values[0], np.ndarray) and values[0].ndim == 2

if not is_field:
    # Simple scalar time series
    plt.figure(figsize=(8, 5))
    plt.plot(times, values, label=VARIABLE)
    plt.xlabel("Time")
    plt.ylabel(VARIABLE)
    plt.title(f"{VARIABLE} Over Time")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

else:
    if PLOT_TYPE == "mean":
        spatial_means = [np.mean(v) for v in values]
        plt.plot(times, spatial_means)
        plt.title(f"Mean {VARIABLE} Over Time")
        plt.xlabel("Time")
        plt.ylabel(f"Mean {VARIABLE}")
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    elif PLOT_TYPE == "max":
        spatial_max = [np.max(v) for v in values]
        plt.plot(times, spatial_max)
        plt.title(f"Max {VARIABLE} Over Time")
        plt.xlabel("Time")
        plt.ylabel(f"Max {VARIABLE}")
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    elif PLOT_TYPE == "center":
        center_vals = [v[v.shape[0] // 2, v.shape[1] // 2] for v in values]
        plt.plot(times, center_vals)
        plt.title(f"{VARIABLE} at Center Cell Over Time")
        plt.xlabel("Time")
        plt.ylabel(f"{VARIABLE} (center)")
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    elif PLOT_TYPE == "heatmap":
        for i in range(0, len(times), FRAME_INTERVAL):
            plt.figure(figsize=(6, 5))
            plt.imshow(values[i].T, origin="lower", cmap="viridis")
            plt.colorbar(label=VARIABLE)
            plt.title(f"{VARIABLE} at t = {times[i]:.2f}")
            plt.tight_layout()
            plt.show()
    else:
        raise ValueError(f"Unknown PLOT_TYPE: {PLOT_TYPE}")
