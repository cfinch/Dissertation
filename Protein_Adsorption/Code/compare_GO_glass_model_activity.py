#!/usr/bin/env python
from numpy import *
import matplotlib as mpl
mpl.rc('font', size=10, family='serif')        # Set default fonts to a smaller size
from matplotlib import pyplot as plt

### Experimental ###

## Active (slope of first 10 points)
#active_surface_density_10ugml = array([7.5233503452, 51.2099331115, 6.66433808936, 0.319532067239])
#active_surface_density_10ugml_std = array([5.32618915675, 11.7991310131, 0.615240113626, 0.301773520496])
#
#active_surface_density_100ugml = array([79.7203561438, 62.520129193, 62.6759482151, 3.26552027325])
#active_surface_density_100ugml_std = array([19.5867955525, 11.8956868286, 19.6251346621, 4.35229867374])

## Total
#total_surface_density_10ugml = array([23.5, 47.0, 88.0, 0.0])    # ng/cm^2
#total_density_std_10ugml = array([9.4, 0.0, 20.5, 3.0])
#
#total_surface_density_100ugml = array([73.0, 137.0, 105.0, 23.0])    # ng/cm^2
#total_density_std_100ugml = array([10.0, 10.9, 3.0, 7.3])

# Set up figures
fig = plt.figure(facecolor='white', figsize=(6.5,3))    # Figure 1 for 10 ug/ml

labels = ['Experiment', 'Langmuir\n2-stage*', 'RSA\n2-stage', 'Langmuir\n2-layer']
bar_width = 0.3
bar_centers = arange(len(labels)) + 0.5

# Experimental
exp_active_glass_10ugml = 7.5233503452
exp_active_glass_10ugml_std = 5.32618915675
exp_total_glass_10ugml = 23.5
exp_total_glass_10ugml_std = 9.4

exp_active_glass_100ugml = 79.7203561438
exp_active_glass_100ugml_std = 19.5867955525
exp_total_glass_100ugml = 73.0
exp_total_glass_100ugml_std = 10.0

# Langmuir with post-adsorption transition
Lang_trans_active_glass_10ugml = 7.7
Lang_trans_total_glass_10ugml = 24.7

Lang_trans_active_glass_100ugml = 23.2
Lang_trans_total_glass_100ugml = 72.3

# SPT two-stage
SPT_trans_active_glass_10ugml = 7.0
SPT_trans_total_glass_10ugml = 23.9

SPT_trans_active_glass_100ugml = 48.7
SPT_trans_total_glass_100ugml = 73.2

# Langmuir two-layer
Lang_2layer_active_glass_10ugml = 21.5
Lang_2layer_total_glass_10ugml = 23.7

Lang_2layer_active_glass_100ugml = 49.4
Lang_2layer_total_glass_100ugml = 76.3

# Data arrays for 10ug/ml
active_surface_density_10ugml = [exp_active_glass_10ugml, 
        Lang_trans_active_glass_10ugml, SPT_trans_active_glass_10ugml,
        Lang_2layer_active_glass_10ugml]
active_surface_density_10ugml_std = [exp_active_glass_10ugml_std, 0.0, 0.0, 0.0]

total_surface_density_10ugml = [exp_total_glass_10ugml,
        Lang_trans_total_glass_10ugml, SPT_trans_total_glass_10ugml,
        Lang_2layer_total_glass_10ugml]
total_density_std_10ugml = [exp_total_glass_10ugml_std, 0.0, 0.0, 0.0]

# Bar chart for 10 ug/ml
plt.figure(1)
plt.subplot(1, 2, 1)
active_bars = plt.bar(bar_centers - bar_width/2, active_surface_density_10ugml,
        align='center', width=bar_width, color='gray', 
        yerr=active_surface_density_10ugml_std, label='Active protein',
        ecolor='black')
total_bars = plt.bar(bar_centers + bar_width/2, total_surface_density_10ugml, 
        align='center', width=bar_width, color='white',
        yerr=total_density_std_10ugml, label='Total protein', ecolor='black')

plt.axis([0, 4, 0, 160])
plt.xticks(bar_centers + bar_width/2, labels)
plt.ylabel(r'$ng/cm^2$')
plt.title(r'$10 \, \mu g/ml$', fontsize=12)
plt.legend((active_bars[0], total_bars[0]), ('active', 'total'))
fig.autofmt_xdate()

# Data arrays for 100 ug/ml
active_surface_density_100ugml = [exp_active_glass_100ugml,
        Lang_trans_active_glass_100ugml, SPT_trans_active_glass_100ugml,
        Lang_2layer_active_glass_100ugml]
active_surface_density_100ugml_std = [exp_active_glass_100ugml_std, 0.0, 0.0, 0.0]

total_surface_density_100ugml = [exp_total_glass_100ugml,
        Lang_trans_total_glass_100ugml, SPT_trans_total_glass_100ugml,
        Lang_2layer_total_glass_100ugml]
total_density_std_100ugml = [exp_total_glass_100ugml_std, 0.0, 0.0, 0.0]

# Bar chart for 100 ug/ml
plt.subplot(1, 2, 2)
plt.bar(bar_centers - bar_width/2, active_surface_density_100ugml, align='center',
        width=bar_width, color='gray', yerr=active_surface_density_100ugml_std, 
        label='Active protein', ecolor='black')
plt.bar(bar_centers + bar_width/2, total_surface_density_100ugml, align='center',
        width=bar_width, color='white', yerr=total_density_std_100ugml,
        label='Total protein', ecolor='black')

plt.axis([0, 4, 0, 160])
plt.title('Experiment')
plt.xticks(bar_centers, labels)
# plt.ylabel(r'$ng/cm^2$')
plt.title(r'$100 \, \mu g/ml$', fontsize=12)
fig.autofmt_xdate()

# Final formatting
plt.subplots_adjust(left=0.1, right=0.97) 

plt.show()
