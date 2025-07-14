# ============================== 0. Initialization ==============================

import gc

# Force garbage collection
gc.collect()

print("Start importation")
simulation_description = "Test avec eta petits et constants - H1P"
from import_inital_parms import initialize_simulation
model_data = initialize_simulation()

Nx, Ny, dx, dy, dt, Nt, Lx, Ly = model_data["spatial"]
V2_croiss, V1_croiss, k_V2_val, k_V1_norm, k_V2_max = model_data["vegetation"]
V1, V2, H1, H2, P, k_V1, k_V2, mask_V2, mask_V1 = model_data["initial_fields"]
a_H2, a_H1, h_V2H2, e_V1, e_V2, h_V1H1, h_V2H1, h_V1H2, mu_H2, mu_H1, epsi_AJ, chi_H2, chi_H1, a_PH2, a_PH1, h_PH1, h_PH2, mu_P, phi_P, h_P, chi_P, epsi_H1H2, gamma_H1H2, I_H1, I_H2 = model_data["animal_params"]
sigma_H2, sigma_P, alpha_H2H2, alpha_H1H1, alpha_PP, alpha_H2V1, alpha_H2V2, alpha_H1V2, alpha_H1V1, alpha_PH2, alpha_PH1 = model_data["diffusion_params"]
params = model_data["seasonal_functions"]

from Landscape_disturbances_mask import create_barrier_mask
import matplotlib.pyplot as plt

barrier_mask = create_barrier_mask((Nx, Ny), orientation='vertical', thickness=0, position='center')
# Put thickness to 0 to get ride of the barrier

print("End importation")

# ============================== 1. Save metadata ==============================

print("Start metadata")

from log_metadata import prepare_and_save_metadata
from log_metadata import save_metadata

 # Generate timestamp
from datetime import datetime
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")

print(timestamp)

metadata_path = prepare_and_save_metadata(
    V1, V2, H1, H2, P,
    alpha_H1V1, alpha_H1V2, alpha_H2V2, alpha_H2V1,
    alpha_H2H2, alpha_H1H1,
    sigma_H2, sigma_P,
    alpha_PH2, alpha_PH1,
    Nx, Ny, dx, dy, Nt, dt,
    simulation_description,
    save_metadata,
    timestamp
)

print("End metadata")

# ============================== 2. Create barrier mask ==============================

print("Start barrier")

from Landscape_disturbances_mask import create_barrier_mask
import matplotlib.pyplot as plt

barrier_mask = create_barrier_mask((Nx, Ny), orientation='vertical', thickness=0, position='center')
# Put thickness to 0 to get ride of the barrier

print("End barrier")

# ============================== 3. Run PDE ==============================
from scipy.integrate import solve_ivp
from PDE_solving import system_rhs
import numpy as np
from fct_flat_field import flatten_fields
from fct_flat_field import unflatten_fields
# from intermediate import log_intermediates
from diffusion_seasons import *
from memory_profiler import profile

# Prep initial state
y0 = flatten_fields(V1, V2, H1, H2, P)

print("y0 has NaNs?", np.any(np.isnan(y0)))
print("y0 has Infs?", np.any(np.isinf(y0)))
print("y0 min/max:", np.min(y0), np.max(y0))

t_span = (0, dt * Nt)
t_eval = np.linspace(*t_span, Nt)

# Bundle parameters
params = {
    'V1_croiss': V1_croiss, 'V2_croiss': V2_croiss,
    'k_V1_norm': k_V1_norm, 'k_V2_val': k_V2_val,
    'a_H1': a_H1, 'a_H2': a_H2,
    'h_V1H1': h_V1H1, 'h_V2H1': h_V2H1,
    'h_V1H2': h_V1H2, 'h_V2H2': h_V2H2,
    # 'rho_H1': rho_H1,
    'h_PH1': h_PH1, 'h_PH2': h_PH2,
    'a_PH1': a_PH1, 'a_PH2': a_PH2, 
    'chi_H1': chi_H1, 'chi_H2': chi_H2,
    'mu_H1': mu_H1, 'mu_H2': mu_H2, 
    'e_V1': e_V1, 'e_V2': e_V2,
    'epsi_AJ': epsi_AJ, 
    # 'sigma_H1': sigma_H1, 
    'sigma_H2': sigma_H2, 'sigma_P': sigma_P, 
    # 'eta_H1': eta_H1, 
    # 'eta_H2': eta_H2,
    # 'eta_P': eta_P, 
    'alpha_H1H1': alpha_H1H1, 'alpha_H2H2': alpha_H2H2, 'alpha_PP': alpha_PP,
    'alpha_H2V1': alpha_H2V1, 'alpha_H2V2': alpha_H2V2,
    'alpha_H1V1': alpha_H1V1, 'alpha_H1V2': alpha_H1V2,
    'alpha_PH1': alpha_PH1, 'alpha_PH2': alpha_PH2,
    'mu_P': mu_P, 'phi_P': phi_P, 'h_P': h_P,
    'chi_P': chi_P, 'epsi_H1H2': epsi_H1H2,
    'gamma_H1H2': gamma_H1H2,
    'eta_H1_fn': seasonal_eta_H1,
    'eta_H2_fn': seasonal_eta_H2,
    'eta_P_fn': seasonal_eta_P,
    'sigma_H1_fn': seasonal_sigma_H1,
    'rho_H1_fn': seasonal_rho_H1
}



# 4. Initialize logs BEFORE defining the function
# logged_data = {
#     "V1": [],
#     "V2": [],
#     "H1": [],
#     "H2": [],
#     "P": [],
#     "score_G_H1": [],
#     "Dm_eff_H1": [],
#     "score_G_H2": [],
#     "Dm_eff_H2": [],
#     "score_G_P": [],
#     "Dm_eff_P": [],
#     "k_H1": [],
#     "k_H2": [],
#     "safe_k_H1": [],
#     "safe_k_H2": [],
#     "safe_r_P": [],
#     "predation_H2": [],
#     "predation_H1": [],
#     "safe_k_V1": [],
#     "safe_k_V2": [],
#     "rho_H1": [],
#     'eta_H1': [],
#     'eta_H2': [],
#     'eta_P': [],
#     'flux_x_H1': [],
#     'flux_y_H1': [],
#     'flux_x_H2': [],
#     'flux_y_H2': [],
#     'flux_x_P': [],
#     'flux_y_P': []
# }

logged_data = {
}


# Save intermediate values on the disk rather than on the RAM! 
from intermediate import make_disk_logger
output_dir = "logs"  # or any directory you want
log_fn = make_disk_logger(output_dir)

print("Start solving PDE")

import time

start = time.time()
sol = solve_ivp(
    fun=lambda t, y: system_rhs(t, y, Nx, Ny, dx, dy, params, mask_V2, mask_V1, barrier_mask, log_fn=None),
    t_span=t_span,
    y0=y0,
    method='LSODA',
    t_eval=np.linspace(*t_span, 100)  # Fewer eval points
)


# =================================== Save the outputs

import os
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

# Base folder for all time series plots and data
base_output_dir = os.path.join("outputs", f"{timestamp}", "sol")
os.makedirs(base_output_dir, exist_ok=True)

# Save sol.t and sol.y inside the output directory
output_file = os.path.join(base_output_dir, "sol_output.npz")
np.savez_compressed(output_file, t=sol.t, y=sol.y)

print("Saved solution to:", output_file)
print("Simulation time:", time.time() - start)



