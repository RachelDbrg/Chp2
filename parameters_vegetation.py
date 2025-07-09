# %%

def initialize_veg_parms():

    import numpy as np

    # Parameters

    # Vegetation
    # Decidudous
    V2_croiss = 30000
    # k_V2_val = 167010
    k_V2_val = 167010
    k_V2_max = k_V2_val

    # Lichen
    V1_croiss = 0.06
    k_V1_norm = 92870
    
    return V2_croiss, V1_croiss, k_V2_val, k_V1_norm, k_V2_max



# %%
