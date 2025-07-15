import numpy as np
import os
from import_inital_parms import initialize_simulation
from spatial_parms import initialize_spatial_parms


model_data = initialize_simulation()
sigma_H2, sigma_P, alpha_H2H2, alpha_H1H1, alpha_PP, alpha_H2V1, alpha_H2V2, alpha_H1V2, alpha_H1V1, alpha_PH2, alpha_PH1 = model_data["diffusion_params"]
Nx, Ny, dx, dy, dt, Nt, Lx, Ly = model_data["spatial"]

def load_solution(output_dir, timestamp, Nx, Ny):
    # Path to the saved .npz file
    npz_path = os.path.join(output_dir, f"{timestamp}", "sol", "sol_output.npz")

    # Load the data
    data = np.load(npz_path)
    t = data["t"]
    y = data["y"]

    # print("sol.t shape:", t.shape)
    # print("sol.y shape:", y.shape)


    # Number of spatial points
    N = Nx * Ny

    N = y.shape[0] // 5
    # Nx = Ny = int(np.sqrt(N))  # Only if you know it’s a square grid


    # Convert to NumPy array (if needed)
    y_array = np.array(y)

    # Reshape each species
    V1_over_time = y_array[0*N : 1*N, :].reshape(Nx, Ny, -1)
    V2_over_time = y_array[1*N : 2*N, :].reshape(Nx, Ny, -1)
    H1_over_time = y_array[2*N : 3*N, :].reshape(Nx, Ny, -1)
    H2_over_time = y_array[3*N : 4*N, :].reshape(Nx, Ny, -1)
    P_over_time  = y_array[4*N : 5*N, :].reshape(Nx, Ny, -1)
    # barrier_mask_over_time  = y_array[5*N : 6*N, :].reshape(Nx, Ny, -1)
    # kV1_over_time  = y_array[6*N : 7*N, :].reshape(Nx, Ny, -1)
    # kV2_over_time  = y_array[7*N : 8*N, :].reshape(Nx, Ny, -1)


    # return t, V1_over_time, V2_over_time, H1_over_time, H2_over_time, P_over_time, barrier_mask_over_time, kV1_over_time, kV2_over_time
    return t, V1_over_time, V2_over_time, H1_over_time, H2_over_time, P_over_time




# Example usage
if __name__ == "__main__":
    # Nx, Ny = 100, 100  # Replace with actual values
    timestamp = "2025-07-15_15-40"   # Use the actual timestamp used during save
    output_dir = "outputs"

    # t, V1, V2, H1, H2, P, barrier_mask, k_V1, k_V2 = load_solution(output_dir, timestamp, Nx, Ny)
    t, V1, V2, H1, H2, P = load_solution(output_dir, timestamp, Nx, Ny)


    # print("Time steps:", t.shape)
    # print("Deciduous shape:", H1.shape)


species_data = {
    "H1": H1,
    "H2": H2,
    "V1": V1,
    "V2": V2,
    "P":  P,
    # "barrier_mask":  barrier_mask,
    # "k_V1":  k_V1,
    # "k_V2":  k_V2
}

species_params = {
    "H1": {"alpha_V1": alpha_H1V1, "alpha_V2": alpha_H1V2, "eta": 0, "color": "orange"},
    "H2": {"alpha_V1": alpha_H2V1, "alpha_V2": alpha_H2V2, "eta": 0, "color": "purple"},
    "V1": {"alpha_V1": 0.0, "alpha_V2": 0.0, "eta": 0.0, "color": "blue"},
    "V2": {"alpha_V1": 0.0, "alpha_V2": 0.0, "eta": 0.0, "color": "green"},
    "P":  {"alpha_V1": alpha_PH1,  "alpha_V2": alpha_PH2,  "eta": 0, "color": "red"},
}

# print("Time axis shape:", t.shape)
# print("H1 shape:", H1.shape)



# ===================================== 1. Sum of the densities through time =====================================
import os
import matplotlib.pyplot as plt
import numpy as np

# Base folder for time series plots
base_output_dir = os.path.join("outputs", f"{timestamp}", "global_time_series")
os.makedirs(base_output_dir, exist_ok=True)

for species_name, species_field in species_data.items():
    if species_name not in species_params:
        continue  # skip if no params defined

    # Sum over spatial grid
    species_sum = np.sum(species_field, axis=(0, 1))

    # Retrieve plotting parameters
    params = species_params[species_name]
    alpha_V1 = params["alpha_V1"]
    alpha_V2 = params["alpha_V2"]
    eta = params["eta"]
    color = params["color"]

    # Create filename
    filename = f"{species_name}_alphaV1_{alpha_V1:.2f}_alphaV2_{alpha_V2:.2f}_eta_{eta:.2f}.png"
    filepath = os.path.join(base_output_dir, filename)

    # Plot and save figure
    plt.figure()
    plt.plot(t, species_sum, label=species_name, color=color)
    plt.xlabel("Time")
    plt.ylabel("Total Value (Sum over Grid)")
    plt.title(f"{species_name} Dynamics Over Time")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig(filepath)
    plt.close()


# ===================================== 2. Mean of the densities through time =====================================
import os
import matplotlib.pyplot as plt
import numpy as np

# Base folder for time series plots
base_output_dir = os.path.join("outputs", f"{timestamp}", "mean_time_series")
os.makedirs(base_output_dir, exist_ok=True)

for species_name, species_field in species_data.items():
    if species_name not in species_params:
        continue  # skip if no params defined

    # Sum over spatial grid
    species_sum = np.mean(species_field, axis=(0, 1))

    # Retrieve plotting parameters
    params = species_params[species_name]
    alpha_V1 = params["alpha_V1"]
    alpha_V2 = params["alpha_V2"]
    eta = params["eta"]
    color = params["color"]

    # Create filename
    filename = f"{species_name}_alphaV1_{alpha_V1:.2f}_alphaV2_{alpha_V2:.2f}_eta_{eta:.2f}.png"
    filepath = os.path.join(base_output_dir, filename)

    # Plot and save figure
    plt.figure()
    plt.plot(t, species_sum, label=species_name, color=color)
    plt.xlabel("Time")
    plt.ylabel("Total Value (Sum over Grid)")
    plt.title(f"{species_name} Dynamics Over Time")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig(filepath)
    plt.close()


# ===================================== 3. Final spatial state =====================================
from plot_distribution import plot_species_distribution
import os
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

# Base folder for time series plots
base_output_dir = os.path.join("outputs", f"{timestamp}", "final_distribution")
os.makedirs(base_output_dir, exist_ok=True)

max_t_idx = V2.shape[2] - 1
t_idx = max_t_idx

V1_t = V1[:, :, t_idx]
V2_t = V2[:, :, t_idx]
H1_t = H1[:, :, t_idx]
H2_t = H2[:, :, t_idx]
P_t  = P[:, :, t_idx]
# barrier_mask_t  = barrier_mask[:, :, t_idx]
# k_V2  = k_V2[:, :, t_idx]
# k_V1  = k_V1[:, :, t_idx]


species_fields = {
    "Deciduous": V2_t,
    "Lichen": V1_t,
    "Caribou": H1_t,
    "Moose": H2_t,
    "Predator": P_t,
    # "Barrier": barrier_mask,
    # "k_V2": k_V2,
    # "k_V1": k_V1
}


for species_name, field in species_fields.items():
    if np.any(field != 0):
        filename = os.path.join(base_output_dir, f"{species_name}.png")
        plot_species_distribution(field, Lx, Ly, species_name=species_name, save_path=filename, time_label= t_idx)


# ===================================== 4. Frames and GIF through time =====================================

import os
import matplotlib.pyplot as plt
import imageio.v2 as imageio
import numpy as np

def save_frame(field, title, t_idx, t_eval, Lx, Ly, filename):
    plt.imshow(field[:, :, t_idx], cmap='viridis', extent=[0, Lx, 0, Ly], origin='lower')
    plt.colorbar()
    plt.title(f"{title} at time t={t_eval[t_idx]:.2f}")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()

def generate_frames_and_gif(species_name, field, alpha_V1, alpha_V2, t_eval, Lx, Ly, timestamp, total_frames=50):
    # Skip if empty field
    if not np.any(field):
        print(f"⏭️ Skipping {species_name}: initial distribution is all zeros.")
        return

    output_dir = os.path.join("outputs", f"{timestamp}", f"frames_{species_name}")
    os.makedirs(output_dir, exist_ok=True)

    step = max(1, field.shape[2] // total_frames)
    selected_indices = list(range(0, field.shape[2], step))[:total_frames]

    for i, t_idx in enumerate(selected_indices):
        fname = os.path.join(output_dir, f"{species_name}_{i:04d}.png")
        save_frame(field, species_name, t_idx, t_eval, Lx, Ly, fname)

    # Make GIF
    gif_dir = os.path.join("outputs", f"{timestamp}", "GIF")
    os.makedirs(gif_dir, exist_ok=True)

    images = [imageio.imread(os.path.join(output_dir, f"{species_name}_{i:04d}.png")) for i in range(len(selected_indices))]
    gif_path = os.path.join(gif_dir, f"{species_name}.gif")
    imageio.mimsave(gif_path, images, duration=0.2)

    print(f"✅ Saved GIF for {species_name} to {gif_path}")


species_data = {
    "H1": H1,
    "H2": H2,
    "P":  P
}

species_params = {
    "H1": {"alpha_V1": alpha_H1V1, "alpha_V2": alpha_H1V2},
    "H2": {"alpha_V1": alpha_H2V1, "alpha_V2": alpha_H2V2},
    "P":  {"alpha_V1": alpha_PH1,  "alpha_V2": alpha_PH2}
}


for species_name, field in species_data.items():
    params = species_params[species_name]
    generate_frames_and_gif(species_name, field, params["alpha_V1"], params["alpha_V2"], t, Lx, Ly, timestamp)
