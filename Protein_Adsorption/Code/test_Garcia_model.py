#!/usr/bin/env python
from Surface_Reaction_Tools.theoretical import Garcia_kinetics, \
        Langmuir_transition_kinetics

from numpy import * 
import matplotlib.pyplot as plt

NA = 6.022e23   # molecules/mole
M = 39e3   # g/mole
A_total = 0.0075   # cm^2
f = NA/M/1e9
c = 10 * 1000   # ng/cm^2
times = arange(0.0, 120.0, 1.0) # sec

plt.figure()

# CH3
plt.subplot(2,2,1)
k = 0.19    # /cm /sec
s = 7.0     # /cm^2 /sec
a1 = 0.33e-14   # cm^2/molecule
b = 150.0   # ratio
r = 0.60    # 1/s

Y1, Y2 = Garcia_kinetics(k, s, a1, b, r, A_total, c, f, times)

plt.plot(times, Y1, label='Y1')
plt.plot(times, Y2, label='Y2')
plt.plot(times, Y1 + Y2, label='YT')
plt.ylabel('ng/cm^2')
plt.axis([0.0, 90.0, 0.0, 90.0])

ka = k * f * a1 * A_total
ks = s * A_total
kd = r
ratio = b
theta1, theta2 = Langmuir_transition_kinetics(ka, ks, kd, ratio, times, const_C=c)
plt.plot(times, theta1 / a1 / f, ls=':', color='k')
plt.plot(times, theta2 / (a1 * b) / f, ls='--', color='k')
plt.plot(times, theta1 / a1 / f + theta2 / (a1 * b) / f, ls='-', color='k')

plt.legend(loc='upper left')

# OH
plt.subplot(2,2,2)
k = 0.049    # /cm /sec
s = 13.0     # /cm^2 /sec
a1 = 6.8e-14   # cm^2/molecule
b = 13.0   # ratio
r = 0.31    # 1/s

Y1, Y2 = Garcia_kinetics(k, s, a1, b, r, A_total, c, f, times)

plt.plot(times, Y1, label='Y1')
plt.plot(times, Y2, label='Y2')
plt.plot(times, Y1 + Y2, label='YT')
plt.axis([0.0, 90.0, 0.0, 50.0])

# NH2
plt.subplot(2,2,3)
k = 0.14    # /cm /sec
s = 7.3     # /cm^2 /sec
a1 = 2.4e-14   # cm^2/molecule
b = 28.0   # ratio
r = 0.32    # 1/s

Y1, Y2 = Garcia_kinetics(k, s, a1, b, r, A_total, c, f, times)

plt.plot(times, Y1, label='Y1')
plt.plot(times, Y2, label='Y2')
plt.plot(times, Y1 + Y2, label='YT')

plt.xlabel('time (sec)')
plt.ylabel('ng/cm^2')
plt.axis([0.0, 120.0, 0.0, 70.0])

# COOH
plt.subplot(2,2,4)
k = 0.080    # /cm /sec
s = 4.4     # /cm^2 /sec
a1 = 3.1e-14   # cm^2/molecule
b = 38.0   # ratio
r = 0.34    # 1/s

Y1, Y2 = Garcia_kinetics(k, s, a1, b, r, A_total, c, f, times)

plt.plot(times, Y1, label='Y1')
plt.plot(times, Y2, label='Y2')
plt.plot(times, Y1 + Y2, label='YT')

plt.xlabel('time (sec)')
plt.axis([0.0, 110.0, 0.0, 40.0])

## My implementation
#plt.figure()
#ka = k * f * a1 * A_total
#ks = s * A_total
#kd = r
#ratio = b
#theta1, theta2 = Langmuir_transition_kinetics(ka, ks, kd, ratio, times, const_C=c)
#plt.plot(times, theta1 / a1 / f, ls=':', color='k', label="theta 1")
#plt.plot(times, theta2 / (a1 * b) / f, ls='--', color='k',  label="theta 2")
#print theta1
#print theta2
#plt.plot(times, theta1 / a1 / f + theta2 / (a1 * b) / f, ls='-', color='k',  label="theta")

plt.show()


