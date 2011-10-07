#!/usr/bin/env python
from numpy import *
from matplotlib import pyplot as plt
import matplotlib as mpl

from Surface_Reaction_Tools.theoretical import phi_theta_fit3, Phi_alpha, \
        phi_theta_Langmuir

mpl.rc('lines', linewidth=1.5)        # Set default line width
mpl.rc('font', size=10.0, family='serif')    # Set default font

# Setup
theta_max = 0.547
d_theta = 0.01
RSA_thetas = arange(0.0, theta_max + d_theta, d_theta)
Langmuir_thetas = arange(0.0, 1.0 + d_theta, d_theta)

# Plot
plt.figure(facecolor='white', figsize=(3,3))
plt.subplots_adjust(left=0.2, bottom=0.08, right=0.95, top=1.0)

plt.plot(Langmuir_thetas, phi_theta_Langmuir(Langmuir_thetas, theta_max=1.0),
        color='k', ls='-.', label="Langmuir")
plt.plot(RSA_thetas, phi_theta_fit3(RSA_thetas), color='b', ls='--', 
        label=r"$\phi_{FIT,3}$")
plt.plot(RSA_thetas, Phi_alpha(RSA_thetas, 0.0, 1.0), color='r', ls='-', 
        label=r"$\Phi_{\alpha}$")

# Format
plt.axis([0.0, 1.0, 0.0, 1.0])
plt.xlabel(r"$\theta$")
plt.ylabel(r"$\Phi(\theta)$")
plt.legend(handlelength=4, labelspacing=0.1, loc='upper right')
plt.axes().set_aspect('equal')

#plt.savefig('../Figures/Langmuir_RSA_SPT.eps')
#plt.savefig('../Figures/Langmuir_RSA_SPT.png', dpi=300)

plt.show()
