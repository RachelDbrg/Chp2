def compute_norm_score_patch(alpha_HH, H , alpha_HV1 ,V1 , alpha_HV2 , V2 , alpha_PH, P):

    import numpy as np
   
    score_G = alpha_HH * H + alpha_HV1 * V1 + alpha_HV2 * V2 + alpha_PH * P

    score_G_min = np.min(score_G)
    score_G_max = np.max(score_G)
    normalized_score_G = (score_G - score_G_min) / (score_G_max - score_G_min + 1e-9)

    return score_G, normalized_score_G


def generate_score_map_plots(V1, V2, H1, H2, P,
                             alpha_H2H2, alpha_H2V1, alpha_H2V2, alpha_PH2,
                             alpha_H1H1, alpha_H1V1, alpha_H1V2,
                             alpha_PP, alpha_PH1,
                             timestamp, compute_score_patch_fn):
    import os
    import numpy as np
    import matplotlib.pyplot as plt

    # Create output folder
    score_dir = os.path.join("outputs", timestamp, "score_maps")
    os.makedirs(score_dir, exist_ok=True)

    # Compute score maps
    score_G_H2, norm_score_G_H2 = compute_score_patch_fn(alpha_H2H2, H2, alpha_H2V1, V1, alpha_H2V2, V2, alpha_PH2, P)
    score_G_H1, norm_score_G_H1 = compute_score_patch_fn(alpha_H1H1, H1, alpha_H1V1, V1, alpha_H1V2, V2, alpha_PH2, P)
    score_G_P, norm_score_G_P   = compute_score_patch_fn(alpha_PP, P, alpha_PH1, H1, alpha_PH2, H2, 0, 0)

    # Bundle fields and colormaps
    fields_to_plot = {
        "V1_distribution": V1,
        "V2_distribution": V2,
        "H1_distribution": H1,
        "H2_distribution": H2,
        "G_H2_raw": score_G_H2,
        "G_H1_raw": score_G_H1,
        "G_P_raw": score_G_P,
        "G_H2_normalized": norm_score_G_H2,
        "G_H1_normalized": norm_score_G_H1,
        "G_P_normalized": norm_score_G_P
    }

    colormaps = {
        "V1_distribution": "viridis",
        "V2_distribution": "viridis",
        "H1_distribution": "viridis",
        "H2_distribution": "viridis",
        "G_H2_raw": "viridis",
        "G_H1_raw": "viridis",
        "G_P_raw": "viridis",
        "G_H2_normalized": "plasma",
        "G_H1_normalized": "plasma",
        "G_P_normalized": "plasma"
    }

    # Plot each field
    for name, field in fields_to_plot.items():
        cmap = colormaps.get(name, "viridis")
        plt.figure()
        plt.imshow(field, origin="lower", cmap=cmap)
        plt.colorbar(label="Score")
        plt.title(name.replace("_", " "))
        plt.savefig(os.path.join(score_dir, f"{name}.png"), bbox_inches="tight", dpi=300)
        plt.close()
