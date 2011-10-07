#!/usr/bin/env python
from numpy import *
from matplotlib import pyplot as plt
from Surface_Reaction_Tools.adsorption_fitting_tools import Fit_Langmuir

NA = 6.022e23

### Setup ###
fit_GO = Fit_Langmuir()
fit_GO.molecular_weight = 160e3        # Daltons (GO)

fit_GO.experimentalFileName = "/home/cfinch/cfinch/Microfluidics/Whispering Gallery Mode Sensor/Experimental Data Analysis/GO/Data/GO_13F.h5"
fit_GO.plot_title = "GO on 13F"

fit_GO.constant_concentration = True

fit_GO.start_conc = 0
fit_GO.end_conc = 2

#Initial parameters:
#ka = 5.000e-08 cm^3/ng/s
#kd = 1.000e-04 1/s
#A = 1.200e-12 cm^2
#Initial SSE: 34.9998144777
#Final parameters:
#ka = 7.197e-08 cm^3/ng/s
#kd = 1.168e-04 1/s
#A = 1.351e-12 cm^2
#Final SSE: 2.44576226523

# Initial parameters
fit_GO.ka = 5e-8
fit_GO.kd = 1e-4
fit_GO.area = 1.2e-12
fit_GO.theta_max = 0.547

fit_GO.f = NA/(fit_GO.molecular_weight*1e9)   # molecules/ng

fit_GO.load_experimental_data()
fit_GO.concentrations = fit_GO.concentrations*1000    # ug/ml to ng/cm^2

if not fit_GO.constant_concentration:
    fit_GO.load_CFD_concentrations()
#    fit_GO.plot_CFD_concentrations()

fit_GO.model_parameters = (fit_GO.concentrations, fit_GO.mean_surf_conc, fit_GO.times)

fit_GO.initial_parameters = [fit_GO.ka, fit_GO.kd, fit_GO.area, fit_GO.theta_max]

def f_ieqcons(a, b, c, d):
    return zeros(4)

fit_GO.f_ieqcons = f_ieqcons

fit_GO.bounds = []
#fit_GO.bounds = [(0.0,1.0), (0.0, 1.0), (0.0, 1.0), (0.0, 1001)]

print("Initial parameters:")
fit_GO.print_parameters(fit_GO.initial_parameters)

#fit_GO.plot()
plt.show()

#fit_GO.fit_adsorption_kinetics()
fit_GO.fit_adsorption_kinetics_slsqp()

print("Initial SSE: {0}".format(fit_GO.initial_sse))
print("Final parameters:")
fit_GO.print_parameters(fit_GO.fitted_parameters)
print("Final SSE: {0}".format(fit_GO.final_sse))

fit_GO.plot()

plt.show()

