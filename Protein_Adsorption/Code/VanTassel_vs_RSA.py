#!/usr/bin/env python
from numpy import *
from matplotlib import pyplot as plt
import matplotlib as mpl

from Surface_Reaction_Tools.theoretical import phi_theta_fit3, Phi_alpha, \
        Psi_alpha_beta, phi_theta_Langmuir

mpl.rc('font', size=8.0, family='serif')        # Set default fonts to a smaller size
mpl.rc('lines', linewidth=1.5)        # Set default line width

# Setup
theta_max = 0.547
d_theta = 0.01
thetas = arange(0.0, theta_max + d_theta, d_theta)

# Plot
plt.figure(facecolor='white', figsize=(4*0.75,3*0.75))
plt.plot(thetas, phi_theta_Langmuir(thetas), color='k', ls='-.', label="Langmuir")
plt.plot(thetas, phi_theta_fit3(thetas), color='b', ls='--', label=r"$\phi_{FIT,3}$")
plt.plot(thetas, Phi_alpha(thetas, 0.0, 1.0), color='r', ls='-', label=r"$\Phi_{\alpha}$")

# Format
plt.axis([0.0, 0.55, 0.0, 1.0])
plt.xlabel(r"$\theta$")
plt.ylabel(r"$\Phi(\theta)$")
plt.legend(handlelength=4, labelspacing=0.1, loc='upper right')
plt.subplots_adjust(left=0.19, bottom=0.16, right=0.95, top=0.95)

plt.show()
