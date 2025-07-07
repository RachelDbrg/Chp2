# The diffusion parameters should be time dependant, as species H1 is likely 
# to chose V1 in winter and more V2 in summer 

# What should change?
## Sigma: the sensitivity of species to high quality patches 

def seasonal_eta_H1(t):
    import numpy as np

    # Example: sinusoidal variation over a year (assuming t in years)
    return 0.05 + 0.02 * np.sin(2 * np.pi * t)

def seasonal_sigma_H1(t):
    import numpy as np
    
    return 0.5 + 0.1 * np.cos(2 * np.pi * t)

# You can do the same for other parameters
