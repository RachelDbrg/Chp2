def system_rhs(t, y, Nx, Ny, dx, dy, params, mask_V2, mask_V1, barrier_mask, log_fn=None):

    import numpy as np
    from reaction import reaction_eq_prey_mono
    from reaction import reaction_eq_prey_mix
    from reaction import reaction_eq_deciduous
    from reaction import reaction_eq_lichen
    from reaction import reaction_eq_predator
    from diffusion_fct import diff_eq
    from fct_flat_field import flatten_fields
    from fct_flat_field import unflatten_fields
    from dynamics_carrying_capacities import dynamics_carrying_capacity


    # V1, V2, H1, H2, P, barrier_mask, k_V1, k_V2 = unflatten_fields(y, Nx, Ny, 8)
    V1, V2, H1, H2, P = unflatten_fields(y, Nx, Ny, 5)

    k_H1, k_H2, safe_k_H1, safe_k_H2 = dynamics_carrying_capacity(V1, V2, params['gamma_H1H2'])

    # print("k_H1_final shape:", np.shape(k_H1))
    # print("k_H2_final shape:", np.shape(k_H2))


    # Initialise array with the proper dimensions but filled with 0
    zero_field = np.zeros((Nx, Ny))


    # Test of optimization: run the functions (season dependant, reaction and diffusion) ONLY if the species is present

    # H1
    if np.any(H1 > 0):
        rho_val = params['rho_H1_fn'](t)
        eta_H1_val = params['eta_H1_fn'](t)

        # Reaction
        R_H1, predation_H1 = reaction_eq_prey_mix(V1 = V1, 
                                              V2 = V2, 
                                              P = P, 
                                              a_H1 = params['a_H1'],
                                            mu_H1 = params['mu_H1'], 
                                            rho_H1 = rho_val,
                                            h_V1H1 = params['h_V1H1'], 
                                            h_V2H1 = params['h_V2H1'],
                                            e_V1 = params['e_V1'], 
                                            e_V2 = params['e_V2'],
                                            epsi_AJ = params['epsi_AJ'],
                                            k_H1 = safe_k_H1,
                                            chi_H1 = params['chi_H1'], 
                                            h_PH1 = params['h_PH1'],
                                            a_PH1 = params['a_PH1'],
                                            H1 = H1,
                                            H2 = H2, 
                                            h_PH2 = params['h_PH2'], 
                                            a_PH2 = params['a_PH2'],
                                            t=t)
        

        # Diffusion
        D_H1, score_G_H1, norm_score_G_H1, Dm_eff_H1, diffusion_term_H1, flux_x_H1, flux_y_H1 = diff_eq(
        H1, V1, V2, P, dx, dy,
        sigma_H=params['sigma_H1_fn'],  # function of t
        eta_H=eta_H1_val,      # function of t
        alpha_HH=params['alpha_H1H1'],
        alpha_HV1=params['alpha_H1V1'],
        alpha_HV2=params['alpha_H1V2'],
        alpha_PH=params['alpha_PH1'],
        barrier_mask=None,
        t=t
    )

    else:
        # rho_val = 0
        # eta_H1_val = 0
        # R_H1 = 0
        # predation_H1 = 0
        # diffusion_term_H1 = 0

        rho_val = 0
        eta_H1_val = 0
        R_H1 = zero_field
        predation_H1 = zero_field
        diffusion_term_H1 = zero_field
        score_G_H1 = zero_field
        Dm_eff_H1 = zero_field
        flux_x_H1 = zero_field
        flux_y_H1 = zero_field


    # H2
    if np.any(H2 > 0):
        eta_H2_val = params['eta_H2_fn'](t)

        # Reaction
        R_H2, r_H, predation_H2 = reaction_eq_prey_mono(params['a_H2'], params['h_V2H2'], V2,
                                    params['chi_H2'], params['epsi_AJ'], params['e_V2'],
                                    params['mu_H2'], safe_k_H2,
                                    params['a_PH2'], P, H2,
                                    params['h_PH1'], params['a_PH1'], H1, params['h_PH2'])


        # Diffusion
        D_H2, score_G_H2, norm_score_G_H2, Dm_eff_H2, diffusion_term_H2, flux_x_H2, flux_y_H2 = diff_eq(
        H2, V1, V2, P, dx, dy,
        sigma_H=params["sigma_H2"], 
        eta_H=eta_H2_val,      # function of t
        alpha_HH=params['alpha_H2H2'],
        alpha_HV1=params['alpha_H2V1'],
        alpha_HV2=params['alpha_H2V2'],
        alpha_PH=params['alpha_PH2'],
        barrier_mask=None,
        t=t
        )


    else:
        eta_H2_val = 0
        # R_H2 = 0
        # predation_H2 = 0
        # diffusion_term_H2 = 0
        # score_G_H2 = 0
        # Dm_eff_H2 = 0
        # flux_x_H2 = 0
        # flux_y_H2 = 0

        eta_H2_val = 0
        R_H2 = zero_field
        predation_H2 = zero_field
        diffusion_term_H2 = zero_field
        score_G_H2 = zero_field
        Dm_eff_H2 = zero_field
        flux_x_H2 = zero_field
        flux_y_H2 = zero_field


    # P
    if np.any(P > 0):
        eta_P_val = params['eta_P_fn'](t)

        # Reaction
        R_P, safe_r_P = reaction_eq_predator(P, H1, H2,
                               params['a_PH1'], params['a_PH2'],
                               params['h_PH1'], params['h_PH2'],
                               params['phi_P'], params['h_P'],
                               params['chi_P'], params['epsi_H1H2'], params['mu_P'])
        
        # Diffusion
        D_P, score_G_P, norm_score_G_P, Dm_eff_P, diffusion_term_P, flux_x_P, flux_y_P = diff_eq(
        P, H1, H2, 0, dx, dy,
        sigma_H=params["sigma_P"],  
        eta_H=eta_P_val,      # function of t
        alpha_HH=params['alpha_PP'],
        alpha_HV1=params['alpha_PH1'],
        alpha_HV2=params['alpha_PH2'],
        alpha_PH=0,
        barrier_mask=None,
        t=t
        )


    else:
        # eta_P_val = 0
        # R_P = 0
        # safe_r_P = 0
        # diffusion_term_P = 0
        # score_G_P = 0
        # Dm_eff_P = 0
        # flux_x_P = 0
        # flux_y_P = 0


        # shape = (Nx, Ny)
        eta_P_val = 0
        R_P = zero_field
        safe_r_P  = zero_field
        diffusion_term_P = zero_field
        score_G_P = zero_field
        Dm_eff_P = zero_field
        flux_x_P = zero_field
        flux_y_P = zero_field



    # Compute reactions
    R_V1, safe_k_V1 = reaction_eq_lichen(v0 = params['V1_croiss'],
                                         V1 = V1, V2 = V2, 
                                         k_V1 = params['k_V1_norm'], 
                                         rho_H1=rho_val,  # function of t
                                         a_H1 = params['a_H1'],
                                         h_V1H1 = params['h_V1H1'], 
                                         h_V2H1 = params['h_V2H1'],
                                         H1 =H1, 
                                         t=t)
 
    

    R_V2, safe_k_V2 = reaction_eq_deciduous(u0 =params['V2_croiss'], 
                                            V1 = V1, 
                                            V2 = V2, 
                                            k_V2 = params['k_V2_val'],
                                            H1 = H1,
                                            H2 = H2, 
                                            rho_H1=rho_val,  # function of t
                                            a_H1=params['a_H1'],
                                            h_V1H1=params['h_V1H1'], 
                                            h_V2H1 = params['h_V2H1'],
                                            a_H2 = params['a_H2'], 
                                            h_V1H2 = params['h_V1H2'],
                                            h_V2H2 = params['h_V2H2'],
                                            t=t)





    # Compute diffusion
    ## H1
    # D_H1, score_G_H1, norm_score_G_H1, Dm_eff_H1, diffusion_term_H1 = diff_eq(H1, V1, V2, P, dx, dy, params["sigma_H1"], params["eta_H1"],
    # params["alpha_H1H1"], params["alpha_H1V1"], params["alpha_H1V2"], params["alpha_PH1"], barrier_mask=None)


    
    ## H2
    # D_H2, score_G_H2, norm_score_G_H2, Dm_eff_H2, diffusion_term_H2 = diff_eq(H2, V1, V2, P, dx, dy, params["sigma_H2"], params["eta_H2"],
    # params["alpha_H2H2"], params["alpha_H2V1"], params["alpha_H2V2"], params["alpha_PH2"], barrier_mask=None)


    ## P
    # D_P, score_G_P, norm_score_G_P, Dm_eff_P, diffusion_term_P = diff_eq(P, H1, H2, 0, dx, dy, params["sigma_P"], params["eta_P"],
    # params["alpha_PP"], params["alpha_PH1"], params["alpha_PH2"], 0, barrier_mask=None)



    if mask_V2 is not None:
        # R_V2 = np.where(mask_V2, R_V2, 0)
        R_V2[~mask_V2] = 0
        # V2 = np.where(mask_V2, V2, 0)
        V2[~mask_V2] = 0

    if mask_V1 is not None:
        # R_V1 = np.where(mask_V1, R_V1, 0)
        R_V1[~mask_V1] = 0
        # V1 = np.where(mask_V1, V1, 0)
        V1[~mask_V1] = 0


    # Log if requested
    if log_fn:
        log_fn(
            t,
            V1 = V1,
            V2 = V2,
            H1 = H1,
            H2 = H2,
            P = P,
            score_G_H1=score_G_H1,
            Dm_eff_H1=Dm_eff_H1,
            score_G_H2=score_G_H2,
            Dm_eff_H2=Dm_eff_H2,
            score_G_P=score_G_P,
            Dm_eff_P=Dm_eff_P,
            k_H1=k_H1,
            k_H2=k_H2,
            safe_k_H1=safe_k_H1,
            safe_k_H2=safe_k_H2,
            safe_r_P = safe_r_P,
            predation_H2 = predation_H2,
            predation_H1 = predation_H1,
            safe_k_V1 = safe_k_V1,
            safe_k_V2 = safe_k_V2,
            rho_H1 = rho_val,
            eta_H1 = eta_H1_val,
            eta_H2 = eta_H2_val,
            eta_P = eta_P_val,
            flux_x_H1 = flux_x_H1,
            flux_y_H1 = flux_y_H1,
            flux_x_H2 = flux_x_H2,
            flux_y_H2 = flux_y_H2,
            flux_x_P = flux_x_P,
            flux_y_P = flux_y_P
    )




    # Apply the barrier mask directly to densities (to prevent "ghost" flow across the barrier)
    if barrier_mask is not None:
        V2[barrier_mask] = 0
        H2[barrier_mask] = 0
        V1[barrier_mask] = 0
        H1[barrier_mask] = 0
        P[barrier_mask] = 0
        R_V2[barrier_mask] = 0  # Optional: Stop any growth across the barrier
        R_H2[barrier_mask] = 0  # Optional: Stop predation or growth too
        R_V1[barrier_mask] = 0  # Optional: Stop any growth across the barrier
        R_H1[barrier_mask] = 0  # Optional: Stop predation or growth too
        R_P[barrier_mask] = 0  # Optional: Stop predation or growth too
        diffusion_term_H1[barrier_mask] = 0
        diffusion_term_H2[barrier_mask] = 0
        diffusion_term_P[barrier_mask] = 0
        

    # Calculate full derivatives
    dV1dt = R_V1
    dV2dt = R_V2
    dH1dt = diffusion_term_H1 + R_H1
    dH2dt = diffusion_term_H2 + R_H2
    dPdt  = diffusion_term_P + R_P

    dH2dt[barrier_mask] = 0  
    dV2dt[barrier_mask] = 0 
    dH1dt[barrier_mask] = 0  
    dV1dt[barrier_mask] = 0 
    dPdt[barrier_mask] = 0 

    return flatten_fields(dV1dt, dV2dt, dH1dt, dH2dt, dPdt) 