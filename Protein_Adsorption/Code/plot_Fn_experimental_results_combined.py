#!/usr/bin/env python
import tables
from numpy import *
import matplotlib as mpl
from matplotlib import pyplot as plt

from Surface_Reaction_Tools.adsorption_fitting_tools import load_average_data

# Setup
separate_plots = False

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

if not separate_plots:
    width = 190.0/25.4
    plt.figure(figsize=(width,width/1.618), facecolor='w')
    plt.subplots_adjust(left=0.08, right=0.96, top=0.93, bottom=0.09, 
            wspace=0.15, hspace=0.4)
else:
    width = 90.0/25.4

# Fn on 13F
experimentalFileName = "/home/cfinch/cfinch/Microfluidics/Whispering Gallery Mode Sensor/Experimental Data Analysis/Fn/Kerry/Fn_13F_experiments.h5"

(concentrations, times, mean_surf_conc, std_surf_conc, exp_labels) = \
        load_average_data(experimentalFileName)

if separate_plots:
    plt.figure(figsize=(width,width/1.618), facecolor='w')
    plt.subplots_adjust(left=0.16, bottom=0.2, top=0.87)
else:
    plt.subplot(2,2,1)
    plt.title("FN on 13F")

for i in range(len(mean_surf_conc)):
    plt.plot(times[i], mean_surf_conc[i], color=colors[exp_labels[i]], 
            dashes=dashes[exp_labels[i]], antialiased=True, label=labels[exp_labels[i]])
    plt.plot(times[i], mean_surf_conc[i]+std_surf_conc[i], 
            color=colors[exp_labels[i]], linestyle=':', antialiased=True)
    plt.plot(times[i], mean_surf_conc[i]-std_surf_conc[i], 
            color=colors[exp_labels[i]], linestyle=':', antialiased=True)

plt.xlabel(x_label)
plt.ylabel(y_label)
plt.axis([0.0, 3000, 0, 250])

# Fn on DETA
experimentalFileName = "/home/cfinch/cfinch/Microfluidics/Whispering Gallery Mode Sensor/Experimental Data Analysis/Fn/Kerry/Fn_DETA_experiments.h5"

(concentrations, times, mean_surf_conc, std_surf_conc, exp_labels) = \
        load_average_data(experimentalFileName)

if separate_plots:
    plt.figure(figsize=(width,width/1.618), facecolor='w')
    plt.subplots_adjust(left=0.16, bottom=0.2, top=0.87)
else:
    plt.subplot(2,2,2)
    plt.title("FN on DETA")

for i in range(len(mean_surf_conc)):
    l, =plt.plot(times[i], mean_surf_conc[i], color=colors[exp_labels[i]], 
            dashes=dashes[exp_labels[i]], antialiased=True, 
            label=labels[exp_labels[i]])
    plt.plot(times[i], mean_surf_conc[i]+std_surf_conc[i], 
            color=colors[exp_labels[i]], linestyle=':', antialiased=True)
    plt.plot(times[i], mean_surf_conc[i]-std_surf_conc[i], 
            color=colors[exp_labels[i]], linestyle=':', antialiased=True)

plt.xlabel(x_label)
if separate_plots:
    plt.ylabel(y_label)
plt.axis([0.0, 3000, 0, 250])

if separate_plots:
    # Make the legend without a figure
    from matplotlib.lines import Line2D
    plt.figure(figsize=(width,width/1.618), facecolor='w')
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
else:
    plt.legend(borderaxespad=0, bbox_to_anchor=(0,-1.3), loc='lower left', 
            handlelength=6, labelspacing=0.1)

# Fn on OEG
experimentalFileName = "/home/cfinch/cfinch/Microfluidics/Whispering Gallery Mode Sensor/Experimental Data Analysis/Fn/Kerry/Fn_PEG_experiments.h5"

(concentrations, times, mean_surf_conc, std_surf_conc, exp_labels) = \
        load_average_data(experimentalFileName, reduce=True, max_points=100)

if separate_plots:
    plt.figure(figsize=(width,width/1.618), facecolor='w')
    plt.subplots_adjust(left=0.15, bottom=0.2, top=0.87)
else:
    plt.subplot(2,2,3)
    plt.title("FN on OEG")

for i in range(len(mean_surf_conc)):
    plt.plot(times[i], mean_surf_conc[i], color=colors[exp_labels[i]], 
            dashes=dashes[exp_labels[i]], label=labels[exp_labels[i]])

    # Only one good run for each concentration on OEG, so std=0
#    plt.plot(times[i], mean_surf_conc[i]+std_surf_conc[i], 
#            color=colors[exp_labels[i]], linestyle=':')
#    plt.plot(times[i], mean_surf_conc[i]-std_surf_conc[i], 
#            color=colors[exp_labels[i]], linestyle=':')

plt.xlabel(x_label)
plt.ylabel(y_label)
plt.axis([0.0, 3000, 0, 30])

#plt.savefig('Plots/Fn_experimental_averaged.eps')

plt.show()

