#!/usr/bin/env python
import tables
from numpy import *
import matplotlib as mpl
from matplotlib import pyplot as plt

from Surface_Reaction_Tools.adsorption_fitting_tools import load_average_data
from Surface_Reaction_Tools.data_utilities import read_ACE_surf_conc, \
        read_ACE_reaction_rate, read_ACE_near_surface_concentration

# Setup
molar_mass = 450e3
f = molar_mass * 1e5

x_label = r"time $(s)$"
y_label = r"$ng/cm^2$"

labels = {'10.0 micrograms/ml':r'$10 \,\mu g/ml$', 
        '5.0 micrograms/ml':r'$5\,\mu g/ml$',
        '1.0 micrograms/ml':r'$1\,\mu g/ml$',
        '0.5 micrograms/ml':r'$0.5\,\mu g/ml$', 
        '0.25 micrograms/ml':r'$0.25\,\mu g/ml$'}

dashes = {'10.0 micrograms/ml':(12,6,4,6,4,6), '5.0 micrograms/ml':(22,8), 
        '1.0 micrograms/ml':(12,6,4,6), '0.5 micrograms/ml':(12,6), 
        '0.25 micrograms/ml':(1,0)}

colors = {'10.0 micrograms/ml':'k', '5.0 micrograms/ml':'b', 
        '1.0 micrograms/ml':'g', '0.5 micrograms/ml':'r', 
        '0.25 micrograms/ml':'m'}

mpl.rc('font', size=8.0, family='serif')    # Set default font to 8pt

width = 3.0

baseNames = ['/home/cfinch/cfinch/Microfluidics/Whispering Gallery Mode Sensor/CFD/FN/Results/FN_250ngml',
    '/home/cfinch/cfinch/Microfluidics/Whispering Gallery Mode Sensor/CFD/FN/Results/FN_500ngml',
    '/home/cfinch/cfinch/Microfluidics/Whispering Gallery Mode Sensor/CFD/FN/Results/FN_1ugml',
    '/home/cfinch/cfinch/Microfluidics/Whispering Gallery Mode Sensor/CFD/FN/Results/FN_5ugml',
    '/home/cfinch/cfinch/Microfluidics/Whispering Gallery Mode Sensor/CFD/FN/Results/FN_10ugml']

# Fn on 13F
experimentalFileName = "/home/cfinch/cfinch/Microfluidics/Whispering Gallery Mode Sensor/Experimental Data Analysis/Fn/Kerry/Fn_13F_experiments.h5"

(concentrations, times, mean_surf_conc, std_surf_conc, exp_labels) = \
        load_average_data(experimentalFileName)

plt.figure(figsize=(width,width/1.618), facecolor='w')
plt.subplots_adjust(left=0.16, bottom=0.2, top=0.87)

plt.figure(figsize=(width,width/1.618), facecolor='w')
plt.subplots_adjust(left=0.16, bottom=0.2, top=0.87)

for i in range(len(mean_surf_conc)):
    plt.figure(1)
    plt.plot(times[i], mean_surf_conc[i], color=colors[exp_labels[i]], 
            dashes=dashes[exp_labels[i]], antialiased=True, label=labels[exp_labels[i]])
    plt.plot(times[i], mean_surf_conc[i]+std_surf_conc[i], 
            color=colors[exp_labels[i]], linestyle=':', antialiased=True)
    plt.plot(times[i], mean_surf_conc[i]-std_surf_conc[i], 
            color=colors[exp_labels[i]], linestyle=':', antialiased=True)

    # Plot CFD surface concentration
    fileName = baseNames[i] + '_Surf_Conc.DAT'
    t, cB, CAB = read_ACE_surf_conc(fileName)
    plt.plot(t, CAB * f, color='k', linewidth=2, dashes=dashes[exp_labels[i]]) 

    # Near-surface concentration
    fileName = baseNames[i] + '_Near_Surf_Conc.DAT'
    t, c = read_ACE_near_surface_concentration(fileName)

    plt.figure(2)
    plt.plot(t, c * 1000 * molar_mass, color=colors[exp_labels[i]], 
            dashes=dashes[exp_labels[i]], label=labels[exp_labels[i]]) 

plt.figure(1)
plt.xlabel(x_label)
plt.ylabel(y_label)
plt.axis([0.0, 200, 0, 250])

plt.figure(2)
plt.axis([0.0, 200, 0.0, 10.0])
plt.xlabel('$t \, (sec)$')
plt.ylabel('$\mu g/ml$')

# Fn on DETA
experimentalFileName = "/home/cfinch/cfinch/Microfluidics/Whispering Gallery Mode Sensor/Experimental Data Analysis/Fn/Kerry/Fn_DETA_experiments.h5"

(concentrations, times, mean_surf_conc, std_surf_conc, exp_labels) = \
        load_average_data(experimentalFileName)

plt.figure(figsize=(width,width/1.618), facecolor='w')
plt.subplots_adjust(left=0.16, bottom=0.2, top=0.87)

plt.figure(figsize=(width,width/1.618), facecolor='w')
plt.subplots_adjust(left=0.16, bottom=0.2, top=0.87)

for i in range(len(mean_surf_conc)):
    plt.figure(3)
    plt.plot(times[i], mean_surf_conc[i], color=colors[exp_labels[i]], 
            dashes=dashes[exp_labels[i]], antialiased=True, 
            label=labels[exp_labels[i]])
    plt.plot(times[i], mean_surf_conc[i]+std_surf_conc[i], 
            color=colors[exp_labels[i]], linestyle=':', antialiased=True)
    plt.plot(times[i], mean_surf_conc[i]-std_surf_conc[i], 
            color=colors[exp_labels[i]], linestyle=':', antialiased=True)

    # Plot CFD surface concentration
    fileName = baseNames[i] + '_Surf_Conc.DAT'
    t, cB, CAB = read_ACE_surf_conc(fileName)
    plt.plot(t, CAB * f, color='k', linewidth=2, dashes=dashes[exp_labels[i]]) 

    # Near-surface concentration
    fileName = baseNames[i] + '_Near_Surf_Conc.DAT'
    t, c = read_ACE_near_surface_concentration(fileName)

    plt.figure(4)
    plt.plot(t, c * 1000 * molar_mass, color=colors[exp_labels[i]], dashes=dashes[exp_labels[i]]) 

plt.figure(3)
plt.xlabel(x_label)
plt.ylabel(y_label)
plt.axis([0.0, 200, 0, 250])

plt.figure(4)
plt.axis([0.0, 200, 0.0, 1.0])
plt.xlabel('$t \, (sec)$')
plt.ylabel('$\mu g/ml$')

# Make the legend without a figure
from matplotlib.lines import Line2D
plt.figure(figsize=(width,width/2.5), facecolor='w')
ax = plt.gca()
ax.set_frame_on(False)
ax.axes.get_xaxis().set_visible(False)
ax.axes.get_yaxis().set_visible(False)
lines = []
line_labels = []
for i in range(len(mean_surf_conc)):
    lines.append(Line2D((0.0, 0.0), (0.0, 0.0), color=colors[exp_labels[i]], 
            dashes=dashes[exp_labels[i]]))
    line_labels.append(labels[exp_labels[i]])
plt.legend(lines, line_labels, loc='center', 
        handlelength=6, labelspacing=0.1)

plt.show()

