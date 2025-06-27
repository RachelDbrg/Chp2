def flatten_fields(*fields):
    return np.concatenate([f.flatten() for f in fields])

def unflatten_fields(y, Nx, Ny, num_fields):
    split = np.split(y, num_fields)
    return [s.reshape((Nx, Ny)) for s in split]


def system_rhs(t, y, Nx, Ny, dx, dy, params, mask_V2):
    # Unpack state
    V2, H2, P = unflatten_fields(y, Nx, Ny, 3)
    V1, H1 = params['V1'], params['H1']

    # Compute reactions
    R_V2, _ = reaction_eq_deciduous(params['u_croiss'], V1, V2, params['k_U_val'],
                                    H1, H2, params['rho_H1'], params['a_H1'],
                                    params['h_V1H1'], params['h_V2H1'],
                                    params['a_H2'], params['h_V1H2'],
                                    params['h_V2H2'])

    R_H2, _ = reaction_eq_prey_mono(params['a_H2'], params['h_V2H2'], V2,
                                    params['chi_H2'], params['epsi_AJ'], params['e_V2'],
                                    params['mu_H2'], params['k_H2'],
                                    params['a_PH2'], P, H2,
                                    params['h_PH1'], params['a_PH1'], H1, params['h_PH2'])

    R_P = reaction_eq_predator(P, H1, H2,
                               params['a_PH1'], params['a_PH2'],
                               params['h_PH1'], params['h_PH2'],
                               params['phi_P'], params['h_P'],
                               params['chi_P'], params['epsi_H1H2'], params['mu_P'])

    if mask_V2 is not None:
        R_V2 = np.where(mask_V2, R_V2, 0)
        V2 = np.where(mask_V2, V2, 0)

    # Calculate full derivatives
    dV2dt = R_V2
    dH2dt = R_H2 #+ Lm
    dPdt  = R_P

    return flatten_fields(dV2dt, dH2dt, dPdt)
