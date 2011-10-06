#!/usr/bin/env python
from numpy import *
from matplotlib import pyplot as plt
import matplotlib as mpl
import tables

#### Setup ####
#dashes = [(8,8), (10,5,3,5), (20,5), (10,5), (2,4)]
#colors = ['k', 'b', 'g', 'r', 'm', 'c']
colors = ['b', 'g', 'r', 'c', 'm', 'y']
dashes = [(None,None), (12,6), (12,6,4,6), (24,6), (8,8)]

## Plotting setup ##
mpl.rc('text', usetex=True)
mpl.rc('font',**{'family':'serif'})
mpl.rc('font', size=10)

## Plot effect of time step ##
BrD_paths = ["/home/cfinch/Brownian_Dynamics/Data/noColloidalForces/Blocking/vf001_dt1e-6/Results/",
        "/home/cfinch/Brownian_Dynamics/Data/noColloidalForces/Blocking/vf01_dt1e-6/Results/",
        "/home/cfinch/Brownian_Dynamics/Data/noColloidalForces/Blocking/vf05_dt1e-6/Results/"]

BrD_labels=[r"$\phi = 0.001$", r"$\phi = 0.01$", r"$\phi = 0.05$"]

# Other
dimensioned = True
D_multiplier = 1.0
markers = ['', '', '', '']

# Constants
NA = 6.0221415e23
phi = 0.01
r=5.8e-8
D=3.77e-12      # m^2/s

#### Load and plot ####

# Fractional surface coverage
plt.figure(facecolor='white', figsize=(4,8.0/3))

max_nd_time = 0.0
max_time = 25
        
# Brownian dynamics
for i in range(len(BrD_paths)):
    BrD_path = BrD_paths[i]

    # Fractional surface coverage
    h5File = tables.openFile(BrD_path + "theta_average.h5", 'r')
    nd_BrD_times = h5File.root.Times.read()
    theta_average = h5File.root.Theta.read()
    theta_stdev = h5File.root.Theta_std.read()
    h5File.close()

    if dimensioned:
        BrD_times = nd_BrD_times*r**2/(D_multiplier*D)
        plt.plot(BrD_times, theta_average, color=colors[i], linewidth=1,
                dashes=dashes[i], marker='', markevery=100, label=BrD_labels[i])
        plt.plot(BrD_times, theta_average-theta_stdev, color=colors[i], linewidth=1, ls=':')
        plt.plot(BrD_times, theta_average+theta_stdev, color=colors[i], linewidth=1, ls=':')
    else:
        plt.plot(nd_BrD_times, theta_average, color=colors[i], linewidth=1, 
                dashes=dashes[i], marker='', label=BrD_labels[i])
        plt.plot(nd_BrD_times, theta_average-theta_stdev, color=colors[i], 
                linewidth=1, ls=':')
        plt.plot(nd_BrD_times, theta_average+theta_stdev, color=colors[i],
                linewidth=1, ls=':')

# Format plots
if dimensioned:
    plt.xlabel(r"$t/sec$")
    plt.axis([0, max_time, 0, 0.55])
else:
    plt.xlabel(r"$\bar{t}$")
#    max_nd_time = 11200
#    plt.axis([0, max_nd_time, 0, 0.547])
plt.ylabel(r"$\theta$")
plt.legend(loc='center right', handlelength=6, prop={'size' : 10})
plt.subplots_adjust(bottom=0.13, right=0.95, top=0.95)

plt.show()
