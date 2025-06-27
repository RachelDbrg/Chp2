def reaction_eq_lichen(v0, V1, V2, k_V, rho_H1, a_H1, h_V1H1, h_V2H1, H1):

    reaction_V1 = v0 * V1 * (1 - V1 / k_V) - ((rho_H1 * a_H1 * V1)/(1 + (rho_H1 * a_H1 * h_V1H1 * V1) + (( 1 - rho_H1) * a_H1 * h_V2H1 * V2))) * H1

    return reaction_V1


def reaction_eq_deciduous(u0, V1, V2, k_V2, H1, H2, rho_H1, a_H1, h_V1H1, h_V2H1,a_H2, h_V1H2, h_V2H2):

    import numpy as np

    safe_k_V2 = np.where(k_V2 < 1e-6, 1e-6, k_V2)

    reaction_V2 = u0 * (1 - V2 / safe_k_V2) - ((a_H2 * V2)/(1 + a_H2 * h_V2H2 * V2) * H2) - ((( 1 - rho_H1) * a_H1 * V2)/(1 + (rho_H1 * a_H1 * h_V1H1 * V1) + (( 1 - rho_H1) * a_H1 * h_V2H1 * V2))) * H1
    
    return reaction_V2, safe_k_V2


def reaction_eq_prey_mix(V1, V2, P, a_H1, mu_H1, rho_H1, h_V1H1, h_V2H1, e_V1, e_V2, epsi_AJ, k_H1, chi_H1,
                         h_PH1, a_PH1, H1, H2, h_PH2, a_PH2):


    denom_H = 1 + (rho_H1 * a_H1 * h_V1H1 * V1) + ((1 - rho_H1) * a_H1 * h_V2H1 * V2)
    r_H = (chi_H1 * epsi_AJ * (((rho_H1 * a_H1 * e_V1 * V1 + (1 - rho_H1) * a_H1 * e_V2 * V2)/denom_H) - mu_H1))
    phi_H = r_H / k_H1
    denom_predator = 1 + h_PH1 * a_PH1 * H1 + h_PH2 * a_PH2 * H2
    predation_H1 = (a_PH1 * P * H1)/denom_predator
    
    # reaction_H = r_H - phi_H * H1**2 + predation_H
    reaction_H = r_H * H1 - phi_H * H1**2 + predation_H1

    return reaction_H

def reaction_eq_prey_mono(a_H2, h_V2H2, V2, chi_H2, epsi_AJ, e_V2, mu_H2, k_H, a_PH2, P, H2, h_PH1, a_PH1, H1, h_PH2):

    denom_H2 = (1 + a_H2 * h_V2H2 * V2)
    r_H = (chi_H2 * epsi_AJ * ((a_H2 * e_V2 * V2)/(denom_H2) - mu_H2))
    phi_H = r_H / k_H
    denom_predator = 1 + h_PH1 * a_PH1 * H1 + h_PH2 * a_PH2 * H2
    predation_H2 = (a_PH2 * P * H2)/denom_predator

    reaction_H = r_H * H2 - phi_H * H2**2 + predation_H2

    return reaction_H, r_H

def reaction_eq_predator(P, H1, H2, a_PH1, a_PH2, h_PH1, h_PH2, phi_P, h_P, chi_P, epsi_H1H2, mu_P) :


    denom_predator = 1 + h_PH1 * a_PH1 * H1 + h_PH2 * a_PH2 * H2

    intake_predator = (chi_P * ((a_PH1 * H1 + epsi_H1H2 * a_PH2 * H2) / (denom_predator)) - mu_P)

    reaction_P = P * (intake_predator - phi_P * P - h_P)

    
    return reaction_P