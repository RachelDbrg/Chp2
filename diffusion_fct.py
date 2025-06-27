def compute_norm_score_patch(alpha_HH, H , alpha_HV1 ,V1 , alpha_HV2 ,V2 , alpha_PH, P):

    import numpy as np

    score_G = alpha_HH * H + alpha_HV1 * V1 + alpha_HV2 * V2 + alpha_PH * P

    score_G_min = np.min(score_G)
    score_G_max = np.max(score_G)
    normalized_score_G = (score_G - score_G_min) / (score_G_max - score_G_min + 1e-9)

    return score_G, normalized_score_G


def diff_eq(H, V1, V2, P, dx, dy, sigma_H, eta_H, 
            alpha_HH, alpha_HV1, alpha_HV2, alpha_PH):

    import numpy as np

    omega_H = 2 * sigma_H

    # Use the helper function to compute the G score and its normalized version
    score_G, normalized_score_G = compute_norm_score_patch(
        alpha_HH, H, alpha_HV1, V1, alpha_HV2, V2, alpha_PH, P
    )

    # Use normalized G score to compute effective diffusion
    # Dm_eff = np.exp(-omega_H * normalized_score_G) * eta_H


    # Idea provided by chatGPT to encourage movement toward favorable (high-score) areas.
    alpha = 5

    Dm_eff = eta_H * (1 + alpha * normalized_score_G)


    # Compute spatial gradients of H
    dHdx = (np.roll(H, -1, axis=0) - np.roll(H, 1, axis=0)) / (2 * dx)
    dHdy = (np.roll(H, -1, axis=1) - np.roll(H, 1, axis=1)) / (2 * dy)

    # Compute fluxes
    flux_x = Dm_eff * dHdx
    flux_y = Dm_eff * dHdy

    # Compute divergence of fluxes
    div_flux_x = (np.roll(flux_x, -1, axis=0) - np.roll(flux_x, 1, axis=0)) / (2 * dx)
    div_flux_y = (np.roll(flux_y, -1, axis=1) - np.roll(flux_y, 1, axis=1)) / (2 * dy)

    divergence = div_flux_x + div_flux_y

    return divergence, score_G, normalized_score_G, Dm_eff
