def initial_sp_distribution(Nx, Ny):

    import numpy as np

    # Initialize fields
    V1 = np.zeros((Nx, Ny))
    V2 = np.zeros((Nx, Ny))
    H1 = np.zeros((Nx, Ny))
    H2 = np.zeros((Nx, Ny))
    P = np.zeros((Nx, Ny))
    k_V1 = np.zeros((Nx, Ny))
    k_V2 = np.zeros((Nx, Ny))

    # Localisation of the V2 vegetation
    V2_loc_x_min = 2
    V2_loc_x_max = 3
    V2_loc_y_min = 8
    V2_loc_y_max = 9


    # Localisation of the V1 vegetation, AROUND the V2 spot 
    # V1_loc_x_min = V2_loc_x_min + 4
    # V1_loc_x_max = V2_loc_x_max + 4
    # V1_loc_y_min = V2_loc_y_min - 4
    # V1_loc_y_max = V2_loc_y_max - 4


    V1_loc_x_min = 8
    V1_loc_x_max = 9
    V1_loc_y_min = 2
    V1_loc_y_max = 3


    # Create the mask inside your initialize() function:
    mask_V2 = np.zeros((Nx, Ny), dtype=bool)
    mask_V2[V2_loc_x_min:V2_loc_x_max, V2_loc_y_min:V2_loc_y_max] = True

    mask_V1 = np.zeros((Nx, Ny), dtype=bool)
    mask_V1[V1_loc_x_min:V1_loc_x_max, V1_loc_y_min:V1_loc_y_max] = True
    
    # V2[Nx // 3:2*Nx // 3, Ny // 3:2*Ny // 3] = 1*10^5  # Center of the grid
    V2[V2_loc_x_min:V2_loc_x_max, V2_loc_y_min:V2_loc_y_max] = 1*10**5  # Center of the grid
    # V1[1:Nx, 1:Ny] = 0  # Center of the grid
    V1[V1_loc_x_min:V1_loc_x_max, V1_loc_y_min:V1_loc_y_max] = 1*10**5 

    # Localisation of the H2 herbivore
    H2_loc_x_min = 2
    H2_loc_x_max = 3
    H2_loc_y_min = 2
    H2_loc_y_max = 3

    H1_loc_x_min = 8
    H1_loc_x_max = 9
    H1_loc_y_min = 8
    H1_loc_y_max = 9

    # H1_loc_x_min = V1_loc_x_min - 1
    # H1_loc_x_max = V1_loc_x_max - 1
    # H1_loc_y_min = V1_loc_y_min
    # H1_loc_y_max = V1_loc_y_max

    
    H1[H1_loc_x_min:H1_loc_x_max, H1_loc_y_min:H1_loc_y_max] = 0.1
    H2[H2_loc_x_min:H2_loc_x_max, H2_loc_y_min:H2_loc_y_max] = 0.1

    P[Nx//2, Nx//2] = 0
    
    k_V2[V2_loc_x_min:V2_loc_x_max, V2_loc_y_min:V2_loc_y_max] = 167010
    k_V1[V1_loc_x_min:V1_loc_x_max, V1_loc_y_min:V1_loc_y_max]= 92870


    # Test and put every vegetation to 0
    # k_V1 = np.zeros((Nx, Ny))
    # k_V2 = np.zeros((Nx, Ny))
    # V1 = np.zeros((Nx, Ny))
    # V2 = np.zeros((Nx, Ny))



    return V1, V2, H1, H2, P, k_V1, k_V2, mask_V2, mask_V1


def plot_species_distribution(species_data, Lx, Ly, species_name='Species'):

    import matplotlib.pyplot as plt

    """
    Plots the distribution of a given species on a 2D grid.
    
    Parameters:
    - species_data: 2D array (e.g., U, V, M, N) representing the species distribution.
    - Lx: float, length of the grid in the X direction.
    - Ly: float, length of the grid in the Y direction.
    - species_name: str, name of the species for the plot title and colorbar label.
    """
    plt.figure(figsize=(6, 5))
    plt.imshow(species_data, origin='lower', extent=[0, Lx, 0, Ly], cmap='Greens')
    plt.colorbar(label=f'{species_name} Density')
    plt.title(f'Initial Distribution of {species_name}')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.tight_layout()
    plt.show()