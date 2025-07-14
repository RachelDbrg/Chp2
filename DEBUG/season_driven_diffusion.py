
# What should change?

## Eta: Area prospected per year: should strongly decrease in winter
## We could suppose lesser movement during calving 
# Voir  Pdf FergusonElkiecariboumovement2004
def seasonal_eta_H1(t):
    import numpy as np
    return 170 + 110 * np.sin(2 * np.pi * t)
    # return 100


## Sigma: the sensitivity of species to high quality patches
def seasonal_sigma_H1(t):
    import numpy as np
    
    return 0.5 + 0.1 * np.cos(2 * np.pi * t)
    # return 0.5


## Rho: part of V1 in the diet of H1
## Higher V1 proportion during the winter and more mixed with higher proportion of V2 during summer
# Based on Thompson et al., 2015
# Part of the H1 in V1 diet: 0.46 during summer to more than 0.7 during winter 

def seasonal_rho_H1(t):
    import numpy as np
    
    min_val = 0.46
    max_val = 0.7
    mean = (min_val + max_val) / 2
    amplitude = (max_val - min_val) / 2
    period = 1  # Period is 1 year because t is in years
    
    return mean + amplitude * np.sin(2 * np.pi * t / period)

    
    # You can do the same for other parameters


import numpy as np

import matplotlib.pyplot as plt

# Time vector: one year, in fractions (e.g. 0 = Jan, 0.25 = Apr, etc.)
t_vals = np.linspace(0, 365, 1000)

# Evaluate functions
eta_vals = [seasonal_eta_H1(t) for t in t_vals]
sigma_vals = [seasonal_sigma_H1(t) for t in t_vals]
rho_vals = [seasonal_rho_H1(t) for t in t_vals]

print(rho_vals)

# Plot
plt.figure(figsize=(10, 5))
# plt.plot(t_vals, eta_vals, label='η_H1 (movement rate)', color='blue')
# plt.plot(t_vals, sigma_vals, label='σ_H1 (patch sensitivity)', color='green')
plt.plot(t_vals, rho_vals, label='part of V1 in the diet', color='red')
plt.axhline(0, color='gray', linestyle='--', linewidth=0.5)
plt.title("Seasonal Variation of η_H1 and σ_H1")
plt.xlabel("Time (fraction of year)")
plt.ylabel("Parameter value")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


# Eta varying across seasons based on data from Diego
def seasonal_eta_H1(t):
    import numpy as np

    # Target values (km²)
    calving = 8254
    sumfall = 11939
    winter = 9361

    # Approximate mean and amplitude
    A = (calving + sumfall + winter) / 3           # Mean value
    B = (sumfall - calving) / 2                    # Amplitude

    # Peak should occur at t = 1/3 → shift sine so sin(2πt - φ) peaks there
    # sin(x) peaks at π/2, so we solve: 2π(1/3) - φ = π/2 ⇒ φ = 2π/3 - π/2
    phi = 2 * np.pi / 3 - np.pi / 2

    return A + B * np.sin(2 * np.pi * t - phi)


# times = [0, 1/3, 2/3]
# labels = ["Calving", "Sumfall", "Winter"]
# for t, label in zip(times, labels):
#     print(f"{label} (t={t:.2f}): η_H1 = {seasonal_eta_H1(t):.2f}")



def seasonal_eta_H2(t):
    import numpy as np

    # Target values (km²)
    calving = 2475
    sumfall = 5478
    winter = 2514

    # Approximate mean and amplitude
    A = (calving + sumfall + winter) / 3           # Mean value
    B = (sumfall - calving) / 2                    # Amplitude

    # Peak should occur at t = 1/3 → shift sine so sin(2πt - φ) peaks there
    # sin(x) peaks at π/2, so we solve: 2π(1/3) - φ = π/2 ⇒ φ = 2π/3 - π/2
    phi = 2 * np.pi / 3 - np.pi / 2

    return A + B * np.sin(2 * np.pi * t - phi)


# times = [0, 1/3, 2/3]
# labels = ["Calving", "Sumfall", "Winter"]
# for t, label in zip(times, labels):
#     print(f"{label} (t={t:.2f}): η_H1 = {seasonal_eta_H2(t):.2f}")


