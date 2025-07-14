def initialize_simulation():
    import matplotlib.pyplot as plt
    import numpy as np
    from spatial_parms import initialize_spatial_parms
    from parameters_animals import initialize_animal_parms
    from parameters_vegetation import initialize_veg_parms
    from initial_distribution import initial_sp_distribution
    from Diffusion_parameters import initialize_diffusion_parms
    from diffusion_seasons import (
        seasonal_eta_H1,
        seasonal_eta_H2,
        seasonal_eta_P,
        seasonal_sigma_H1,
        seasonal_rho_H1
    )

    # Spatial and time parameters
    Nx, Ny, dx, dy, dt, Nt, Lx, Ly = initialize_spatial_parms()

    # Vegetation parameters
    V2_croiss, V1_croiss, k_V2_val, k_V1_norm, k_V2_max = initialize_veg_parms()

    # Initial state distributions
    V1, V2, H1, H2, P, k_V1, k_V2, mask_V2, mask_V1 = initial_sp_distribution(Nx, Ny, k_V1_norm, k_V2_max)

    # Animal parameters
    a_H2, a_H1, h_V2H2, e_V1, e_V2, h_V1H1, h_V2H1, h_V1H2, mu_H2, mu_H1, epsi_AJ, chi_H2, chi_H1, \
    a_PH2, a_PH1, h_PH1, h_PH2, mu_P, phi_P, h_P, chi_P, epsi_H1H2, gamma_H1H2, I_H1, I_H2 = \
        initialize_animal_parms(k_V2_max, k_V1_norm, k_V2_max)

    # Diffusion-related parameters (seasonal or static)
    sigma_H2, sigma_P, alpha_H2H2, alpha_H1H1, alpha_PP, alpha_H2V1, alpha_H2V2, \
    alpha_H1V2, alpha_H1V1, alpha_PH2, alpha_PH1 = initialize_diffusion_parms()

    # Bundle all outputs into a dictionary
    return {
        "spatial": (Nx, Ny, dx, dy, dt, Nt, Lx, Ly),
        "vegetation": (V2_croiss, V1_croiss, k_V2_val, k_V1_norm, k_V2_max),
        "initial_fields": (V1, V2, H1, H2, P, k_V1, k_V2, mask_V2, mask_V1),
        "animal_params": (a_H2, a_H1, h_V2H2, e_V1, e_V2, h_V1H1, h_V2H1, h_V1H2, mu_H2, mu_H1,
                          epsi_AJ, chi_H2, chi_H1, a_PH2, a_PH1, h_PH1, h_PH2, mu_P, phi_P, h_P,
                          chi_P, epsi_H1H2, gamma_H1H2, I_H1, I_H2),
        "diffusion_params": (sigma_H2, sigma_P, alpha_H2H2, alpha_H1H1, alpha_PP, alpha_H2V1,
                             alpha_H2V2, alpha_H1V2, alpha_H1V1, alpha_PH2, alpha_PH1),
        "seasonal_functions": {
            "eta_H1_fn": seasonal_eta_H1,
            "eta_H2_fn": seasonal_eta_H2,
            "eta_P_fn": seasonal_eta_P,
            "sigma_H1_fn": seasonal_sigma_H1,
            "rho_H1_fn": seasonal_rho_H1
        }
    }
