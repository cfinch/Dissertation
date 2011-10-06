#!/usr/bin/env python
from numpy import *
from matplotlib import pyplot as plt
from matplotlib import rc
import tables

rc('text', usetex=True)
rc('font',**{'family':'serif'})
rc('font', size=10)

### Setup ###

### Constant concentration, domain size ##
#paths = ["/home/cfinch/Brownian_Dynamics/Data/noColloidalForces/Blocking/constant_C/75x75/vf01/",
#        "/home/cfinch/Brownian_Dynamics/Data/noColloidalForces/Blocking/constant_C/100x100/vf01/",
#        "/home/cfinch/Brownian_Dynamics/Data/noColloidalForces/Blocking/constant_C/150x150/vf01/"]
#RSA_path = '/home/cfinch/RSA/Results/'
#labels = ["75x75", "100x100", "150x150"]

## Diffusing, time step size ###
#paths = ["/home/cfinch/Brownian_Dynamics/Data/noColloidalForces/Blocking/vf01_dt1e-5/",
#        "/home/cfinch/Brownian_Dynamics/Data/noColloidalForces/Blocking/vf01_dt1e-6/",
#        "/home/cfinch/Brownian_Dynamics/Data/noColloidalForces/Blocking/vf01_dt1e-7/"]
#RSA_path = '/home/cfinch/RSA/Results/'
#labels = ["$\Delta t=10^{-5} \, s$", "$\Delta t=10^{-6} \, s$", "$\Delta t=10^{-7} \, s$"]

## Diffusing, volume fraction ###
paths = ["/home/cfinch/Brownian_Dynamics/Data/noColloidalForces/Blocking/vf001_dt1e-6/",
        "/home/cfinch/Brownian_Dynamics/Data/noColloidalForces/Blocking/vf01_dt1e-6/",
        "/home/cfinch/Brownian_Dynamics/Data/noColloidalForces/Blocking/vf05_dt1e-6/"]
RSA_path = '/home/cfinch/RSA/Results/'
labels = ["$\phi=0.001$", "$\phi=0.01$", "$\phi=0.05$"]

### Formatting ###
colors = ['b', 'g', 'r', 'c', 'm', 'y']
dashes = [(None,None), (12,6), (12,6,4,6), (24,6), (8,8)]
theoretical_dashes = (4,4)
offset = 2.0

### Load and plot ###
plt.figure(figsize=(4,5), facecolor='white')
ax = plt.axes([0.12, 0.1, 0.525, 0.85], axisbg='white')

num_figures = 0
max_gr = 0.0
max_h = 0.0
for i in range(len(paths)):
    h5Path = paths[i] + "Results/"
    h5FileName = h5Path + "radial_distribution_function.h5"
    print "Loading " + h5FileName
    h5File = tables.openFile(h5FileName, 'r')

    if h5File.root._v_nchildren > num_figures:
        num_figures = h5File.root._v_nchildren

    for theta_index in range(h5File.root._v_nchildren):
#        plt.figure(theta_index+1, figsize=(4, 2.667))
        group = h5File.root._f_getChild('theta'+str(theta_index))
        theta = group._v_attrs.theta
        h_values = group.radii.read()
        g_r_average = group.Mean.read()
        g_r_stdev = group.Std.read()

        if g_r_average.max() > max_gr:
            max_gr = g_r_average.max()
        if h_values.max() > max_h:
            max_h = h_values.max()

#        plt.plot(h_values, g_r_average, color='k', label=labels[i])

        if theta_index == 0:
            ax.plot(h_values, g_r_average + offset * theta_index,
                    color=colors[i], dashes=dashes[i], label=labels[i])
        else:
            ax.plot(h_values, g_r_average + offset * theta_index,
                    color=colors[i], dashes=dashes[i])

#        plt.plot(h_values, g_r_average+3*theta_index+g_r_stdev,
#                color='k', ls=":")
#        plt.plot(h_values, g_r_average+3*theta_index-g_r_stdev,
#                color='k', ls=":")
#        plt.title('theta=' + str(theta))
        theta_string = r"$\theta={0}$".format(theta)
        plt.text(7, offset * theta_index + 1.25, theta_string)
    h5File.close()

h5Path = RSA_path + "Results/"
h5FileName = h5Path + "radial_distribution_function.h5"
print "Loading " + h5FileName
h5File = tables.openFile(h5FileName, 'r')

for theta_index in range(h5File.root._v_nchildren):
    group = h5File.root._f_getChild('theta'+str(theta_index))
    theta = group._v_attrs.theta
    h_values = group.radii.read()
    g_r_average = group.Mean.read()
    g_r_stdev = group.Std.read()

    if g_r_average.max() > max_gr:
        max_gr = g_r_average.max()
    if h_values.max() > max_h:
        max_h = h_values.max()

    if theta_index == 0:
        ax.plot(h_values, g_r_average + offset * theta_index,
                color='k', dashes=theoretical_dashes, label="RSA")
    else:
        ax.plot(h_values, g_r_average + offset * theta_index,
                color='k', dashes=theoretical_dashes)
h5File.close()

plt.xlabel('$r/a$')
plt.ylabel('$g(r/a)$')
plt.legend(labelspacing=0.1, handlelength=5, loc='lower left', 
        bbox_to_anchor=(1.05, 0), borderaxespad=0, prop={'size' : 8})
plt.xlim(0.0, max_h)
#plt.subplots_adjust(left=0.2, bottom=0.11, right=0.92, top=0.95)
plt.axis([0.0, 10.0, 0.0, 11.0])

plt.show()
