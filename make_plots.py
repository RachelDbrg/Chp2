# ============================= Load and plot the outputs
import numpy as np
import matplotlib.pyplot as plt
from fct_flat_field import unflatten_fields  # You already have this

# Load the saved solution
data = np.load("sol_output.npz")
t = data['t']         # shape: (N_times,)
y = data['y']         # shape: (5 * Nx * Ny, N_times)

Nx, Ny = 100, 100  # Example; use your real values
n = Nx * Ny


H1_avg = []

for i in range(len(t)):
    state_flat = y[:, i]
    
    # Unflatten fields
    V1, V2, H1, H2, P = unflatten_fields(state_flat, Nx, Ny, 5)
    
    # Compute mean H1
    H1_avg.append(H1.mean())

H1_avg = np.array(H1_avg)


plt.figure(figsize=(8, 4))
plt.plot(t, H1_avg, label='Average H1')
plt.xlabel("Time")
plt.ylabel("Average H1")
plt.title("H1 vs Time")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

