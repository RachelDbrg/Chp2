import os
import json

def save_metadata(species, params, grid, sim_settings, timestamp, notes=""):
       
    metadata = {
        "timestamp": timestamp,
        "species": species,
        "parameters": params,
        "grid": grid,
        "simulation": sim_settings,
        "notes": notes
    }

    # Create timestamped subfolder
    config_dir = os.path.join("outputs", timestamp, "configs")
    os.makedirs(config_dir, exist_ok=True)

    filename = f"run_{species}.json"
    filepath = os.path.join(config_dir, filename)

    with open(filepath, "w") as f:
        json.dump(metadata, f, indent=2)
    
    return filepath


def prepare_and_save_metadata(V1, V2, H1, H2, P,
                               alpha_H1V1, alpha_H1V2, alpha_H2V2, alpha_H2V1,
                               alpha_H2H2, alpha_H1H1,
                               sigma_H2, sigma_P,
                               alpha_PH2, alpha_PH1,
                               Nx, Ny, dx, dy, Lx, Ly, Nt, dt,
                               simulation_description,
                               save_metadata_fn, timestamp
                               ):
    from datetime import datetime
    import numpy as np

    # Generate timestamp
    # timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")

    # Duration of the simulations
    t_span = (0, dt * Nt)

    # Detect which species are present
    species = {"V1": V1, "V2": V2, "H1": H1, "H2": H2, "P": P}
    active_species = [name for name, field in species.items() if np.any(field != 0)]

    # Bundle tracked parameters
    params = {
        "alpha_H1V1": alpha_H1V1,
        "alpha_H1V2": alpha_H1V2,
        "alpha_H2V2": alpha_H2V2,
        "alpha_H2V1": alpha_H2V1,
        "alpha_H2H2": alpha_H2H2,
        "alpha_H1H1": alpha_H1H1,
        "sigma_H2": sigma_H2,
        "sigma_P": sigma_P,
        "alpha_PH2": alpha_PH2,
        "alpha_PH1": alpha_PH1
    }

    grid = {"Nx - nbe of cells x axis": Nx, "Ny - nbe of cells y axis": Ny, 
            "Lx - Physical length of the domain (km) ":Lx, "Ly - Physical length of the domain (km)":Ly, 
            "dx - resolution of x axis (km/cell)": dx, "dy - resolution of y axis (km/cell)": dy}
    sim_settings = {"Nt - ": Nt, "t_span": list(t_span), "solver": "LSODA"}
    notes = simulation_description

    # Save and return path
    return save_metadata_fn(active_species, params, grid, sim_settings, timestamp, notes)


