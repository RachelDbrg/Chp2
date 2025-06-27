# What is the code doing?

## Species and interactions modelled

2 types of vegetaiton: V1 and V2, where V1 is the lichen and V2 is the deciduous

2 species of herbivores: H1 are the caribou and H2 are the moose. 
Eventually, a 3rd herbivore should be integrated but will be invasive with an advection term simulating the northward shift

1 predator, maybe 2 if we integrate the cougar


# How are the parameters defined?
## Definition of initial parameters and structure

### Spatio-temporal settings
We define the structure of the landscape in terms of size, resolution of the discrete solving, and time steps in "spatial_parms.py"

### Species parameters
Everything related to the reaction term of the species (vegetation and animal) are defined in the script "parameters.py"

### Initial distribution
Based on th grid define, we define the initial distribution of species (should laterbe adjusted with GRF or something to account for spatial heterogeneity)
