# Diffusion parameters
def initialize_diffusion_parms():

   # Sensitivity of species for high G scores
   # Serves as a weighting factor. Default to 0.5 so omega = 1
   sigma_H2 = 0.5
   # sigma_H1 = 0.5
   sigma_P = 0.5

   # Average movement of species, area prospected per year (km2/year)
   # Defines how much the diffusion term will increase based on the G score, defines the rate of the movement
   # based on the quality of the patch

   # eta_H2 = 0.05
   # eta_H1 = 0.05
   # eta_P = 65

   # Intra-specific diffusion term: should be <0
   alpha_H2H2 = 0 
   alpha_H1H1 = 0
   alpha_PP = 0

   # Inter-specific diffusion term: should be >0 if less diffusion expected in high resource areas
   alpha_H2V1 = 0
   alpha_H2V2 = 1
   alpha_H1V2 = 1
   alpha_H1V1 = 1

   # Diffusion of the predator that should decrease with the density of the prey 
   alpha_PH2 = 1
   alpha_PH1 = 1

   # return sigma_H1, sigma_H2, sigma_P, eta_H1, eta_H2, eta_P, alpha_H2H2, alpha_H1H1, alpha_PP, alpha_H2V1, alpha_H2V2, alpha_H1V2, alpha_H1V1, alpha_PH2, alpha_PH1
   # return sigma_H2, sigma_P, eta_H2, eta_P, alpha_H2H2, alpha_H1H1, alpha_PP, alpha_H2V1, alpha_H2V2, alpha_H1V2, alpha_H1V1, alpha_PH2, alpha_PH1
   return sigma_H2, sigma_P, alpha_H2H2, alpha_H1H1, alpha_PP, alpha_H2V1, alpha_H2V2, alpha_H1V2, alpha_H1V1, alpha_PH2, alpha_PH1