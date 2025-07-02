# Diffusion parameters
def initialize_diffusion_parms():

   sigma_H2 = 1
   sigma_H1 = 1

   eta_H2 = 10
   eta_H1 = 10

   alpha_H2H2 = 0
   alpha_H1H1 = 0

   alpha_H2V1 = 0
   alpha_H2V2 = 1
   alpha_H1V2 = 0
   alpha_H1V1 = 1

   alpha_PH2 = 0
   alpha_PH1 = 0

   return sigma_H1, sigma_H2, eta_H1, eta_H2, alpha_H2H2, alpha_H1H1, alpha_H2V1, alpha_H2V2, alpha_H1V2, alpha_H1V1, alpha_PH2, alpha_PH1