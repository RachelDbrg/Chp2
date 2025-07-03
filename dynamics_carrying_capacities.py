def dynamics_carrying_capacity(k_V2, k_V1):

    # We want to make the carrying capacity of consumers dependant on the 
    # abundance of their resource

    # V2
    ## H2
    k_H2_V2 = 4 * 10**(-6) * k_V2 - 0.0618

    ## H1
    k_H1_V2 = alpha_NM * k_H2_V2

    # V1
    k_H1_V1 = 9 * 10**(-7) * k_V1 - 0.0094
    k_H2_V1 = 0

    # Compute total carrying capacities, accounting for the mixed diet
    k_H1 = k_H1_V1 + k_H1_V2
    k_H2 = k_H2_V1 + k_H2_V2


    return