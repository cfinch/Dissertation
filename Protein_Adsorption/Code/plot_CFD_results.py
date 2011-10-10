#!/usr/bin/env python
"""Plot the results of CFD transient simulations of transport near the 
resonator surface with a simple irreversible Langmuir adsorbing boundary
condition.
"""

from numpy import *
import matplotlib as mpl
mpl.rc('font', family='serif', size='10')
from matplotlib import pyplot as plt
from Surface_Reaction_Tools.data_utilities import read_ACE_surf_conc, \
        read_ACE_reaction_rate, read_ACE_near_surface_concentration
from Surface_Reaction_Tools.adsorption_fitting_tools import load_average_data

# Setup
width = 5.0
dashes = [(None,None), (8,4), (2,2)]
target_fraction = 0.99

baseNames = ['/home/cfinch/cfinch/Microfluidics/Whispering Gallery Mode Sensor/CFD/GO/Results/GO_DETA_10ugml_adsorption_RESONATORSENSINGAREA',
        '/home/cfinch/cfinch/Microfluidics/Whispering Gallery Mode Sensor/CFD/GO/Results/GO_DETA_100ugml_adsorption_RESONATORSENSINGAREA']
expFileName = '/home/cfinch/cfinch/Microfluidics/Whispering Gallery Mode Sensor/Experimental Data Analysis/GO/Data/GO_DETA.h5'

molar_mass = 160e3
f = molar_mass * 1e5

exp_C, exp_t, exp_mean, std, labels = load_average_data(expFileName)

plt.figure(facecolor='white', figsize=(width, width/1.618))
plt.subplots_adjust(left=0.15, top=0.88, right=0.97, bottom=0.18)

plt.figure(facecolor='white', figsize=(width, width/1.618))
plt.subplots_adjust(left=0.15, top=0.88, right=0.97, bottom=0.18)

for i in range(len(exp_C)):
    # Near-surface concentration
    fileName = baseNames[i] + '_Near_Surf_Conc.DAT'
    t, c = read_ACE_near_surface_concentration(fileName)
    plt.figure(1)
#    plt.title('Near-Surface Concentration')
    plt.plot(t, c * 1000 * molar_mass, color='k', dashes=dashes[i], 
            label=r"$" + str(exp_C[i]) + "\, \mu g/ml$")  # mol/L to micrograms/ml
    plt.axis([0.0, 60.0, 0.0, 100.0])
    plt.xlabel('$t \, (sec)$')
    plt.ylabel('$\mu g/ml$')
    plt.legend(loc='center right', handlelength=3)

    # Find time at which concentration reaches target %
    index = abs(c - c.max() * target_fraction).argmin()
    print t[index]
    # Surface concentration
    plt.figure(2)
    plt.plot(exp_t[i], exp_mean[i], dashes=dashes[i], color='k', 
            label=r"$\mathrm{Exp} \, " + str(exp_C[i]) + "\, \mu g/ml $")

    fileName = baseNames[i] + '_Surf_Conc.DAT'
    t, cB, CAB = read_ACE_surf_conc(fileName)
    plt.plot(t, CAB * f, color='k', linewidth=3, dashes=dashes[i], 
            label=r"$\mathrm{CFD} \," + str(exp_C[i]) + "\, \mu g/ml $")
#    plt.title('Surface Concentration')
    plt.axis([0.0, 200.0, 0.0, 120.0])
    plt.xlabel('$t \, (sec)$')
    plt.ylabel('$ng/cm^2$')
    plt.legend(loc='best', handlelength=4)

    # Adsorption rate
    fileName = baseNames[i] + '_RXN_rate.DAT'
    t, A_rate, CB_rate, CAB_rate = read_ACE_reaction_rate(fileName)
    plt.figure(3)
    plt.plot(t, CAB_rate * f, label=r'AB ' + labels[i])
    plt.title('Adsorption Rate')
    plt.xlabel('$t \, (sec)$')
    plt.ylabel('$ng/cm^2/s$')
    plt.legend(loc='best')


plt.show()
