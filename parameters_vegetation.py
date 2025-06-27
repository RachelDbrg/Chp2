# %%

def initialize_veg_parms():

    import numpy as np

    # Parameters

    # Vegetation
    # Decidudous
    u_croiss = 30000
    k_U_val = 167010
    k_U_max = k_U_val

    # Lichen
    v_croiss = 0.06
    k_V_norm = 92870
    
    return u_croiss, v_croiss, k_U_val, k_V_norm, k_U_max



# %%
