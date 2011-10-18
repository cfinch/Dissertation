from numpy import *
import matplotlib.pyplot as plt
import matplotlib
from Surface_Reaction_Tools.adsorption_fitting_tools import load_average_data
from Surface_Reaction_Tools.theoretical import RSA_kinetics

# Setup
matplotlib.rc('font', size=10.0, family='serif')    # Set default font to 8pt
width = 5
colors = ['k', 'b']
dashes = [(None,None), (8,4), (2,2)]

# RSA
ka = 2.18e-8
kd = 2.55e-4
area = 482.0

expFileName = '/home/cfinch/cfinch/Microfluidics/Whispering Gallery Mode Sensor/Experimental Data Analysis/GO/Data/GO_PEG.h5'

NA = 6.022e23
molar_mass = 160e3      # g/mol
f = NA / molar_mass * 1e-9    # g/molecule

exp_C, exp_t, exp_mean, exp_std, labels = load_average_data(expFileName)
plt.figure(figsize=(width, width/1.618), facecolor='w')

max_time = 0
for i in range(1,len(exp_C)):
    if exp_t[i].max() > max_time:
        max_time = exp_t[i].max()

    theta = RSA_kinetics(ka, kd, exp_t[i], 
                        const_C=exp_C[i] * 1000)

    surface_density = theta / (f * area * 1e-14)
    plt.plot(exp_t[i], surface_density, color=colors[i], dashes=dashes[i], 
            label=r"$" + str(exp_C[i]) + "\, \mu g/ml$")
    plt.plot(exp_t[i], exp_mean[i], color=colors[i], ls='-')
    plt.plot(exp_t[i], exp_mean[i] + exp_std[i], color=colors[i], ls=':')
    plt.plot(exp_t[i], exp_mean[i] - exp_std[i], color=colors[i], ls=':')

plt.xlabel(r"$t(s)$")
plt.ylabel(r"$ng/cm^2$")
plt.axis([0.0, max_time, 0.0, 60.0])
plt.legend(loc='upper right', handlelength=3)
plt.subplots_adjust(bottom=0.15)
plt.show()


