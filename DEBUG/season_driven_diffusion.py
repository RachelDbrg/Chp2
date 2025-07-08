
# What should change?

## Eta: Area prospected per year: should strongly decrease in winter
## We could suppose lesser movement during calving 
# Voir  Pdf FergusonElkiecariboumovement2004
def seasonal_eta_H1(t):
    import numpy as np
    return 170 + 110 * np.sin(2 * np.pi * t)



## Sigma: the sensitivity of species to high quality patches
def seasonal_sigma_H1(t):
    import numpy as np
    
    return 0.5 + 0.1 * np.cos(2 * np.pi * t)

# You can do the same for other parameters


import numpy as np

import matplotlib.pyplot as plt

# Time vector: one year, in fractions (e.g. 0 = Jan, 0.25 = Apr, etc.)
t_vals = np.linspace(0, 1, 365)

# Evaluate functions
eta_vals = [seasonal_eta_H1(t) for t in t_vals]
sigma_vals = [seasonal_sigma_H1(t) for t in t_vals]

# Plot
plt.figure(figsize=(10, 5))
plt.plot(t_vals, eta_vals, label='η_H1 (movement rate)', color='blue')
plt.plot(t_vals, sigma_vals, label='σ_H1 (patch sensitivity)', color='green')
plt.axhline(0, color='gray', linestyle='--', linewidth=0.5)
plt.title("Seasonal Variation of η_H1 and σ_H1")
plt.xlabel("Time (fraction of year)")
plt.ylabel("Parameter value")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

