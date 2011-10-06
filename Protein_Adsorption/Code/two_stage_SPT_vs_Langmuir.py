#!/usr/bin/env python
import numpy 
from matplotlib import pyplot as plt
import matplotlib as mpl
from Surface_Reaction_Tools.theoretical import Van_Tassel_kinetics, \
        Langmuir_transition_kinetics

mpl.rc('font', size=8.0, family='serif')        # Set default fonts to a smaller size
mpl.rc('lines', linewidth=1.5)        # Set default line width

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

theta_alpha, theta_beta = Van_Tassel_kinetics(ka * a_alpha, ks, kd, Sigma,
        times, c)

plt.figure(facecolor='white', figsize=(3,4))
plt.subplot(2, 1, 1)
plt.plot(nd_times, theta_alpha, color='r', ls='--', label=r"$\theta_{\alpha}$")
plt.plot(nd_times, theta_beta, color='b', ls=':', label=r"$\theta_{\beta}$")
plt.plot(nd_times, theta_alpha + theta_beta, color='k', ls='-', label=r"$\theta$")

plt.axis([0.0, 16.0, 0.0, 0.55])
plt.title('a')

ratio = Sigma**2
theta_alpha_Langmuir, theta_beta_Langmuir = Langmuir_transition_kinetics(
        ka * a_alpha, ks, kd, ratio, times, const_C=c)

plt.subplot(2,1,2)
plt.plot(nd_times, theta_alpha_Langmuir, color='r', ls='--', label=r"$\theta_{\alpha}$")
plt.plot(nd_times, theta_beta_Langmuir, color='b', ls=':', label=r"$\theta_{\beta}$")
plt.plot(nd_times, theta_alpha_Langmuir + theta_beta_Langmuir, color='k', ls='-', label=r"$\theta$")

plt.axis([0.0, 16.0, 0.0, 0.55])
plt.xlabel(r"$t$")
plt.legend(loc='lower right', handlelength=4, labelspacing=0.0)
plt.title('b')

plt.subplots_adjust(hspace=0.35, bottom=0.12, top=0.92)

plt.show()
