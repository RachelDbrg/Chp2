# Diffusion parameters
def initialize_diffusion_parms():

   sigma_H2 = 1
   sigma_H1 = 1
   sigma_P = 1

   eta_H2 = 0
   eta_H1 = 0
   eta_P = 0

   alpha_H2H2 = 0
   alpha_H1H1 = 0
   alpha_PP = 0

   alpha_H2V1 = 0
   alpha_H2V2 = 1
   alpha_H1V2 = 0
   alpha_H1V1 = 1

   alpha_PH2 = 10
   alpha_PH1 = 1

   return sigma_H1, sigma_H2, sigma_P, eta_H1, eta_H2, eta_P, alpha_H2H2, alpha_H1H1, alpha_PP, alpha_H2V1, alpha_H2V2, alpha_H1V2, alpha_H1V1, alpha_PH2, alpha_PH1