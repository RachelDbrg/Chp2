def diff_eq(H, V1, V2, P, dx, dy, sigma_H, eta_H, 
            alpha_HH, alpha_HV1, alpha_HV2, alpha_PH,
            barrier_mask=None, t=None):

    import numpy as np
    from scipy.ndimage import uniform_filter
    from compute_score_maps import compute_norm_score_patch

    # Evaluate time-dependent parameters if needed
    if callable(sigma_H):
        sigma_H = sigma_H(t)
        
    if callable(eta_H):
        eta_H = eta_H(t)


    omega_H = 2 * sigma_H

    score_G, normalized_score_G = compute_norm_score_patch(
        alpha_HH, H, alpha_HV1, V1, alpha_HV2, V2, alpha_PH, P
    )

    Dm_eff = np.exp(-omega_H * normalized_score_G) * eta_H

    if barrier_mask is not None:
        Dm_eff[barrier_mask] = 0

    # Pad for reflective boundary conditions
    H_padded = np.pad(H, pad_width=1, mode='edge')
    Dm_padded = np.pad(Dm_eff, pad_width=1, mode='edge')

    # Compute gradients
    dHdx = (H_padded[2:, 1:-1] - H_padded[1:-1, 1:-1]) / dx
    dHdy = (H_padded[1:-1, 2:] - H_padded[1:-1, 1:-1]) / dy

    flux_x = Dm_padded[1:-1,1:-1] * dHdx
    flux_y = Dm_padded[1:-1,1:-1] * dHdy

    # Reflective barrier sides: block flux across internal wall
    if barrier_mask is not None:
        edge_top = ~barrier_mask & np.roll(barrier_mask, 1, axis=0)
        edge_bottom = ~barrier_mask & np.roll(barrier_mask, -1, axis=0)
        edge_left = ~barrier_mask & np.roll(barrier_mask, 1, axis=1)
        edge_right = ~barrier_mask & np.roll(barrier_mask, -1, axis=1)

        dHdx[edge_top] = 0
        dHdx[edge_bottom] = 0
        dHdy[edge_left] = 0
        dHdy[edge_right] = 0

        flux_x[edge_top | edge_bottom] = 0
        flux_y[edge_left | edge_right] = 0

    # Flux divergence
    flux_x_padded = np.pad(flux_x, pad_width=1, mode='constant')
    flux_y_padded = np.pad(flux_y, pad_width=1, mode='constant')

    div_flux_x = (flux_x_padded[2:, 1:-1] - flux_x_padded[1:-1, 1:-1]) / dx
    div_flux_y = (flux_y_padded[1:-1, 2:] - flux_y_padded[1:-1, 1:-1]) / dy

    divergence = div_flux_x + div_flux_y
    divergence = uniform_filter(divergence, size=3)


    # Reflective padding 
    # Neumann boundary conditions 
    H_pad = np.pad(H, pad_width=1, mode='edge')

    laplacian_H = (
        H_pad[0:-2, 1:-1] +  # up
        H_pad[2:  , 1:-1] +  # down
        H_pad[1:-1, 0:-2] +  # left
        H_pad[1:-1, 2:  ] - 
        4 * H
    ) / (dx * dy)

    # # Optional: Laplacian (still respects Dm_eff)
    # laplacian_H = (
    #     np.roll(H, -1, axis=0) + np.roll(H, 1, axis=0) +
    #     np.roll(H, -1, axis=1) + np.roll(H, 1, axis=1) - 4 * H
    # ) / (dx * dy)

    diffusion_term = Dm_eff * laplacian_H

    return divergence, score_G, normalized_score_G, Dm_eff, diffusion_term