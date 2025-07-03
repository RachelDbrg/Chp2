def compute_norm_score_patch(alpha_HH, H , alpha_HV1 ,V1 , alpha_HV2 , V2 , alpha_PH, P):

    import numpy as np
   
    score_G = alpha_HH * H + alpha_HV1 * V1 + alpha_HV2 * V2 + alpha_PH * P

    score_G_min = np.min(score_G)
    score_G_max = np.max(score_G)
    normalized_score_G = (score_G - score_G_min) / (score_G_max - score_G_min + 1e-9)

    return score_G, normalized_score_G
