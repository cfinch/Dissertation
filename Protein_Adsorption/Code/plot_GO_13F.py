from numpy import *
import matplotlib.pyplot as plt
import matplotlib
from Surface_Reaction_Tools.adsorption_fitting_tools import load_average_data
from Surface_Reaction_Tools.theoretical import Langmuir_transition_kinetics

# Setup
matplotlib.rc('font', size=10.0, family='serif')    # Set default font
width = 5
colors = ['k', 'b']
dashes = [(None,None), (8,4), (2,2)]

# Langmuir with post-adsorption transition
ka = 5.957e-8
ks = 1.143e-2
kd = 6.744e-5
area1 = 209.0
area2 = 291.0
ratio = area2 / area1
theta_max = 1.0

expFileName = '/home/cfinch/cfinch/Microfluidics/Whispering Gallery Mode Sensor/Experimental Data Analysis/GO/Data/GO_13F.h5'

NA = 6.022e23
molar_mass = 160e3      # g/mol
f = NA / molar_mass * 1e-9    # g/molecule

exp_C, exp_t, exp_mean, exp_std, labels = load_average_data(expFileName)
plt.figure(figsize=(width, width/1.618), facecolor='w')
max_time = 0
for i in range(len(exp_C)):
    if exp_t[i].max() > max_time:
        max_time = exp_t[i].max()

    theta1, theta2 = Langmuir_transition_kinetics(ka, ks, kd, ratio, exp_t[i], 
                        const_C=exp_C[i] * 1000, blocking_fn_args=theta_max)

    rho1 = theta1 / (f * area1 * 1e-14)
    rho2 = theta2 / (f * area2 * 1e-14)
    surface_density = rho1 + rho2

    plt.plot(exp_t[i], surface_density, color=colors[i], dashes=dashes[i], 
            label=r"$" + str(exp_C[i]) + "\, \mu g/ml$")
    plt.plot(exp_t[i], exp_mean[i], color=colors[i], ls='-')
    plt.plot(exp_t[i], exp_mean[i] + exp_std[i], color=colors[i], ls=':')
    plt.plot(exp_t[i], exp_mean[i] - exp_std[i], color=colors[i], ls=':')

plt.xlabel(r"$t(s)$")
plt.ylabel(r"$ng/cm^2$")
plt.axis([0.0, max_time, 0.0, 160.0])
plt.legend(loc='upper right', handlelength=3)
plt.subplots_adjust(bottom=0.15)
plt.show()


