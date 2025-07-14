def initialize_spatial_parms():
    
    import numpy as np
   
    
 # Grid and time setup
    Nx, Ny = 30, 30    # Number of grid cells in the x- and y-direction
    Lx, Ly = 100, 100   # Physical length of the domain in the x- and y-direction (e.g., meters, kilometers)
    dx, dy = Lx/Nx, Ly/Ny # Spatial resolution (grid cell size)
    dt = 0.01      # time step size (in years)
    T = 100.0      # total simulation time (in years)
    Nt = int(T / dt)  # number of time steps

    return Nx, Ny, dx, dy, dt, Nt, Lx, Ly