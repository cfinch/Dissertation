#!/usr/bin/env python
import csv
from numpy import *
from matplotlib import pyplot as plt
import tables
from scipy.special import erf

from Surface_Reaction_Tools.theoretical import diffusion_limited_theta, \
        diffusion_limited_flux

colors = ['k', 'b', 'r', 'g', 'c', 'y']
linestyles = ['-','--',':','.-']
markers = ['', '', '', '']

def make_plots(BrD_paths, BrD_labels, title='', dimensioned=False, D_multiplier=1.0):
    # Fractional surface coverage
    plt.figure()        # 1 for theta
    plt.figure()        # 2 for Js

    # Brownian dynamics
    for i in range(len(BrD_paths)):
        BrD_path = BrD_paths[i]

        # Fractional surface coverage
        h5File = tables.openFile(BrD_path + "theta_average.h5", 'r')
        nd_BrD_times = h5File.root.Times.read()
        theta_average = h5File.root.Theta.read()
        theta_stdev = h5File.root.Theta_std.read()
        h5File.close()

        plt.figure(1)

        if dimensioned:
            BrD_times = nd_BrD_times*r**2/(D_multiplier*D)
            plt.plot(BrD_times, theta_average, color=colors[i], linewidth=2, ls='--', marker='', 
                    markevery=100, label=BrD_labels[i] + ' D*' + str(D_multiplier))
            plt.plot(BrD_times, theta_average-theta_stdev, color=colors[i], linewidth=2, ls=':')
            plt.plot(BrD_times, theta_average+theta_stdev, color=colors[i], linewidth=2, ls=':')
        else:
            plt.plot(nd_BrD_times, theta_average, color=colors[i], linewidth=2, 
                    ls='--', marker='', label=BrD_labels[i])
            plt.plot(nd_BrD_times, theta_average-theta_stdev, color=colors[i], 
                    linewidth=2, ls=':')
            plt.plot(nd_BrD_times, theta_average+theta_stdev, color=colors[i],
                    linewidth=2, ls=':')

    #    if nd_BrD_times.max() > max_nd_time:
    #        max_nd_time = nd_BrD_times.max()

        # Flux at the surface
        h5File = tables.openFile(BrD_path + "Js_average.h5", 'r')
        nd_BrD_times = h5File.root.Times.read()
        Js_average = h5File.root.Surface_Flux_smoothed.read()
        Js_stdev = h5File.root.Surface_Flux_std.read()
        h5File.close()

        plt.figure(2)
        plt.plot(nd_BrD_times, Js_average, color=colors[i], ls='--', marker='', label=BrD_labels[i])
        plt.plot(nd_BrD_times, Js_average-Js_stdev, color=colors[i], ls=':')
        plt.plot(nd_BrD_times, Js_average+Js_stdev, color=colors[i], ls=':')

    # Plot theoretical curves
    if plot_diffusion_limited:
        # Fractional surface coverage
        plt.figure(1)
        if dimensioned:
            pass
        else:
            if plot_constant_concentration:
                Js_eq = n_bulk/2
                plt.plot(nd_times, Js_eq*nd_times*pi, ls="-.", color='red', label="Const C, Perf abs")
            else:
                plt.plot(nd_times, diffusion_limited_theta(n_bulk, nd_times),
                        ls=":", color='red', label="Dif lim, Perf abs")

        plt.figure(2)
        if dimensioned:
            pass
        else:
            if plot_constant_concentration:
                plt.axhline(y=-D * n_bulk / ( 2 * r), ls='-.', color='red')    # constant concentration
            else:
                plt.plot(nd_times[1:], diffusion_limited_flux(0.0, nd_times[1:], n_bulk),
                        ls=":", color='red', label="Dif lim, Perf abs")

    # Format plots

    # Fractional surface coverage
    plt.figure(1)
    if dimensioned:
        plt.xlabel('time/sec')
        plt.axis([0, max_time, 0, 0.547])
    else:
        plt.xlabel('time')
        max_nd_time = 11200
        plt.axis([0, max_nd_time, 0, 0.547])
    plt.ylabel('Fractional Surface Coverage')
    plt.legend(loc='lower right')
    plt.title(title)

    # Flux
    plt.figure(2)
    plt.xlabel('time')
    plt.ylabel('Flux (amount/unit area/time)')
    plt.title(title)
    plt.legend(loc='lower right')

#### Setup ####

## Brownian Dynamics volume fraction ##
title = "Brownian Dynamics volume fraction"
BrD_paths = ["/home/cfinch/Brownian_Dynamics/Data/noColloidalForces/Blocking/vf001_dt1e-6/Results/",
        "/home/cfinch/Brownian_Dynamics/Data/noColloidalForces/Blocking/vf01_dt1e-6/Results/",
        "/home/cfinch/Brownian_Dynamics/Data/noColloidalForces/Blocking/vf05_dt1e-6/Results/"]

BrD_labels=["BrD vf001", "BrD vf01", "BrD vf05"]

### Brownian Dynamics time step ##
#title = "Brownian Dynamics time step"
#BrD_paths = ["/home/cfinch/Brownian_Dynamics/Data/noColloidalForces/Blocking/vf01_dt1e-5/Results/",
#        "/home/cfinch/Brownian_Dynamics/Data/noColloidalForces/Blocking/vf01_dt1e-6/Results/",
#        "/home/cfinch/Brownian_Dynamics/Data/noColloidalForces/Blocking/vf01_dt1e-7/Results/"]
#
#BrD_labels=["BrD dt=1e-5", "BrD dt=1e-6", "BrD dt=1e-7"]

### Size of Brownian Dynamics simulation domain ##
#title = "Size of simulation domain"
#BrD_paths = ["/home/cfinch/Brownian_Dynamics/Data/noColloidalForces/Blocking/constant_C/75x75/vf01/Results/",
#        "/home/cfinch/Brownian_Dynamics/Data/noColloidalForces/Blocking/constant_C/100x100/vf01/Results/",
#        "/home/cfinch/Brownian_Dynamics/Data/noColloidalForces/Blocking/constant_C/150x150/vf01/Results/"]
#BrD_labels=["75x75", "100x100", "150x150"]

# Other
dimensioned = False
D_multiplier = 1.0
plot_diffusion_limited = False
plot_constant_concentration = False

# Constants
NA = 6.0221415e23
phi = 0.01
r=5.8e-8
D=3.77e-12      # m^2/s

n_bulk = 3*phi/(4*pi)

if not dimensioned:
    D = 1.0
    r = 1.0

make_plots(BrD_paths, BrD_labels, title, dimensioned, D_multiplier)

plt.show()
