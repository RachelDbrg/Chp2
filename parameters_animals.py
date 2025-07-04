# %%

def initialize_animal_parms(k_U_val, k_V_norm, k_U_max):

    import numpy as np

      
    # Prey
    ## ------------------ Weights
    w_H2 = 400
    w_H1 = 100
    
    ## ------------------ Carrying capacities: A CHANGER
    # k_H2 = 0.6
    # k_H1 = 0.6 #A CHANGER

    ## ------------------ Handling times
    h_V2H1 = 8.81e-4
    h_V1H2 = 0
    h_V2H2 = 0.000034
    h_V1H1 = 8.81e-4

    ## ------------------ Prospecting area
    a_H1 = 0.05
    a_H2 = 0.05

    ## ------------------ Energy provided by the vegetation
    e_V2 = 20083
    e_V1 = 11.8e3
    
    ## ------------------ Basal energy needs
    mu_H2 = 70 * w_H2**0.75 * 365 * 1.7 * 4.184
    mu_H1 = 70 * w_H1**0.75 * 365 * 1.7 * 4.184 

    ## ------------------ Proportion of V1 in the H1 diet 
    rho_H1 = 0.6
    
    ## ------------------ Conversion rates
    epsi_AJ = 0.08
    epsi_H1H2 = w_H1 / w_H2

    ## ------------------ Target growth rates
    target_growth_rate_H2 = 0.39
    target_growth_rate_H1 = 0.26

    ## ------------------ Conversion of energy into new individuals
    chi_H2 = target_growth_rate_H2 / (epsi_AJ) * ((a_H2 * k_U_val * e_V2)/(1 + a_H2 * h_V2H2 * k_U_val) - mu_H2)**-1
    denom_supp_NRJ_H1 = 1 + (rho_H1 * a_H1 * h_V1H1 * k_V_norm) + ((1 - rho_H1) * a_H1 * h_V2H1 * k_U_val)
    chi_H1 = target_growth_rate_H1 / (epsi_AJ) * ((((rho_H1 * a_H1 * e_V1 * k_V_norm + (1 - rho_H1) * a_H1 * e_V2 * k_U_max)/(denom_supp_NRJ_H1))) - mu_H1)**-1

    ## ------------------ Intake ratio between prey
    I_H1 = 0.45 * (w_H1 **0.71)
    I_H2 = 0.45 * (w_H2 **0.71)
    gamma_H1H2 = I_H1 / I_H2

    # Predator
    ###  ------------------ Basal energy needs
    mu_P = 0 # set to 0 to avoind redundancy with chi_P

    ## ------------------ Natural mortality ------------------
    phi_P = 30

    ### ------------------ Hunting of the predator ------------------
    h_P = 0

    ### ------------------ Conversion of energy into new individuals ------------------
    chi_P = 0.64/6.93


    ### ------------------ Traveling distances and detection -----------------------
    daily_dist_P = (8.4+10.92)/2 #(km/day), mean value from Serrouya 2020
    annual_dist_P = daily_dist_P * 365.25 #(km/year)
    detection_buffer_P = 0.2 #(km), from Serrouya et al., 2015 (in Serrouya 2020)
    


    ### ---------------------------- Attack success --------------------------------
    attack_success_NA_P = 0.43 # Serrouya2020
    attack_success_MA_P = 0.064 # Serrouya2020
    attack_success_MJ_P = 0.196 # Wikenros 2009

    ratio_attack_success_AJ_P = attack_success_MJ_P / attack_success_MA_P

    ### --------------- Spatial overlap between predator and prey ------------------
    overlap_N_P = 0.125 #serrouya2020
    overlap_M_P = 0.29 #* t_U #serrouya2020

    ### ------------------------- Foraging efficiency ------------------------------
    a_PH2 = (annual_dist_P * detection_buffer_P * attack_success_MA_P * overlap_M_P) #* t_U
    a_PH1 = (annual_dist_P * detection_buffer_P * attack_success_NA_P * overlap_N_P) #* q_N


    ### ------------------------- Handling time ------------------------------------
    # Adults
    h_PH1 = 0.144 #* t_U # from Lake, (year.predator)/prey
    h_PH2 = h_PH1 * epsi_H1H2 

 
    return rho_H1, a_H2, a_H1, h_V2H2, e_V1, e_V2, h_V1H1, h_V2H1, h_V1H2, mu_H2, \
    mu_H1, epsi_AJ, chi_H2, chi_H1, a_PH2, a_PH1, h_PH1, h_PH2, mu_P, phi_P, h_P, chi_P, epsi_H1H2, gamma_H1H2, I_H1, I_H2



# %%
