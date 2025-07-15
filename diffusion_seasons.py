# The diffusion parameters should be time dependant, as species H1 is likely 
# to chose V1 in winter and more V2 in summer 

# What should change?
## Sigma: the sensitivity of species to high quality patches should be stronger in winter than in summer?


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
    # return 10


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
    # return 10


def seasonal_eta_P(t):
    import numpy as np

    # Target values (km²)
    calving = 2327
    sumfall = 1735
    winter = 2905

    # Approximate mean and amplitude
    A = (calving + sumfall + winter) / 3           # Mean value
    B = (sumfall - calving) / 2                    # Amplitude

    # Peak should occur at t = 1/3 → shift sine so sin(2πt - φ) peaks there
    # sin(x) peaks at π/2, so we solve: 2π(1/3) - φ = π/2 ⇒ φ = 2π/3 - π/2
    phi = 2 * np.pi / 3 - np.pi / 2

    return A + B * np.sin(2 * np.pi * t - phi)
    # return 10



def seasonal_sigma_H1(t):
    import numpy as np
    
    # return 0.5 + 0.1 * np.cos(2 * np.pi * t)
    return 0.5


def seasonal_rho_H1(t):
    import numpy as np

    min_val = 0.46
    max_val = 0.7
    mean = (min_val + max_val) / 2
    amplitude = (max_val - min_val) / 2
    period = 1

    # print(f"[DEBUG] seasonal_rho_H1 called with t={t} (type: {type(t)})")

    return mean + amplitude * np.sin(2 * np.pi * t / period)
