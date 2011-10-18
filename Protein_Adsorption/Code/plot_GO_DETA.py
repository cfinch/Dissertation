from numpy import *
import matplotlib.pyplot as plt
import matplotlib
from Surface_Reaction_Tools.adsorption_fitting_tools import load_average_data
from Surface_Reaction_Tools.theoretical import Langmuir_kinetics_twolayer

# Setup
matplotlib.rc('font', size=10.0, family='serif')    # Set default font to 8pt
width = 5
colors = ['k', 'b']
dashes = [(None,None), (8,4), (2,2)]

# RSA with post-adsorption transition
#ka = 1.19e-8
#ks = 0.412
#kd = 2.33e-4
#area1 = 28.0
#area2 = 457
#ratio = sqrt(area2 / area1)

# Langmuir two layer
ka1 = 1.44e-7
ka2 = 1.26e-8
kd1 = 1.19e-3
kd2 = 3.42e-9
area = 363.0 # nm^2

expFileName = '/home/cfinch/cfinch/Microfluidics/Whispering Gallery Mode Sensor/Experimental Data Analysis/GO/Data/GO_DETA.h5'

NA = 6.022e23
molar_mass = 160e3      # g/mol
f = NA / molar_mass * 1e-9    # g/molecule

exp_C, exp_t, exp_mean, exp_std, labels = load_average_data(expFileName)
plt.figure(figsize=(width, width/1.618), facecolor='w')

max_time = 0
for i in range(len(exp_C)):
    if exp_t[i].max() > max_time:
        max_time = exp_t[i].max()

    theta1, theta2 = Langmuir_kinetics_twolayer(ka1, ka2, kd1, kd2,
                        exp_t[i], const_C=exp_C[i] * 1000)
#    theta1, theta2 = Van_Tassel_kinetics(ka, ks, kd, ratio, exp_t[i], 
#                        const_C=exp_C[i] * 1000)

    rho1 = theta1 / (f * area * 1e-14)
    rho2 = theta2 / (f * area * 1e-14)
    surface_density = rho1 + 2 * rho2
    plt.plot(exp_t[i], surface_density, color=colors[i], dashes=dashes[i], 
            label=r"$" + str(exp_C[i]) + "\, \mu g/ml$")
    plt.plot(exp_t[i], exp_mean[i], color=colors[i], ls='-')
    plt.plot(exp_t[i], exp_mean[i] + exp_std[i], color=colors[i], ls=':')
    plt.plot(exp_t[i], exp_mean[i] - exp_std[i], color=colors[i], ls=':')

plt.xlabel(r"$t(s)$")
plt.ylabel(r"$ng/cm^2$")
plt.axis([0.0, max_time, 0.0, 160.0])
plt.legend(loc='center right', handlelength=3)
plt.subplots_adjust(bottom=0.15)
plt.show()


