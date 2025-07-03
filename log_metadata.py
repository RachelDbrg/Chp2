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
