#!/usr/bin/env python
import numpy 
from matplotlib import pyplot as plt
import matplotlib as mpl
from Surface_Reaction_Tools.theoretical import Van_Tassel_kinetics, \
        Langmuir_transition_kinetics

mpl.rc('font', size=10.0, family='serif')        # Set default font
mpl.rc('lines', linewidth=1.5)        # Set default line width
width = 90.0/25.4

# Original
r_alpha = 1.0
Sigma = 1.2
Ks = 0.1
Kd = 0.1
ka = 1.0
c = 1.0

# Derived
r_beta = Sigma * r_alpha
a_alpha = numpy.pi * r_alpha**2
a_beta = numpy.pi * r_beta**2
ks = Ks * ka * c * a_alpha
kd = Kd * ka * c * a_alpha
nd_times = numpy.arange(0.0, 16.0, 0.1)
times = nd_times/(ka * c * a_alpha)

print("ka = " + str(ka))
print("ks = " + str(ks))
print("kd = " + str(kd))

# SPT theory derived by Van Tassel et al
theta_alpha, theta_beta = Van_Tassel_kinetics(ka * a_alpha, ks, kd, Sigma,
        times, c)

plt.figure(facecolor='white', figsize=(width, width/1.618))
plt.subplots_adjust(left=0.1, top=0.95, right=0.95, bottom=0.2)

plt.plot(nd_times, theta_alpha, color='r', ls='--', label=r"$\theta_{\alpha}$")
plt.plot(nd_times, theta_beta, color='b', ls=':', linewidth=2,
        label=r"$\theta_{\beta}$")
plt.plot(nd_times, theta_alpha + theta_beta, color='k', ls='-', label=r"$\theta$")

plt.axis([0.0, 16.0, 0.0, 0.55])
plt.xlabel(r"$t$")

#plt.savefig('../Figures/SPT_with_transition.eps')
#plt.savefig('../Figures/SPT_with_transition.png', dpi=300)

# Langmuir as derived by Michael et al
ratio = Sigma**2
theta_alpha_Langmuir, theta_beta_Langmuir = Langmuir_transition_kinetics(
        ka * a_alpha, ks, kd, ratio, times, const_C=c, blocking_fn_args=0.547)

plt.figure(facecolor='white', figsize=(width, width/1.618))
plt.subplots_adjust(left=0.1, top=0.95, right=0.95, bottom=0.2)

plt.plot(nd_times, theta_alpha_Langmuir, color='r', ls='--', label=r"$\theta_{\alpha}$")
plt.plot(nd_times, theta_beta_Langmuir, color='b', ls=':', linewidth=2,
        label=r"$\theta_{\beta}$")
plt.plot(nd_times, theta_alpha_Langmuir + theta_beta_Langmuir, color='k',
        ls='-', label=r"$\theta$")

plt.axis([0.0, 16.0, 0.0, 0.55])
plt.xlabel(r"$t$")
plt.legend(loc='center right', handlelength=4, labelspacing=0.0)

#plt.savefig('../Figures/Langmuir_with_transition.eps')
#plt.savefig('../Figures/Lanmguir_with_transition.png', dpi=300)

plt.show()
