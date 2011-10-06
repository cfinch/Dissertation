#!/usr/bin/env python
from numpy import *
import tables

from subprocess import Popen
import xdrlib

### Setup ###

# Path for loading data from Brownian Dynamics simulation
basePath = "/home/cfinch/Brownian_Dynamics/Data/noColloidalForces/Blocking/ConstantC/150x150/vf01/Results/"
baseName = "coeff_b.h5"
outputPath = "../Plots/"

### Load Data ###
h5fileName = basePath + baseName
print "Loading " + h5fileName

h5file = tables.openFile(h5fileName, mode="r")
coeff_a = h5file.root.coeff_b.read()
theta_values = h5file.root.theta.read()
h_values = h5file.root.h.read()
h5file.close()

p = xdrlib.Packer()

p.pack_array(h_values, p.pack_double)       # x
p.pack_array(theta_values, p.pack_double)   # y

for i in range(len(h_values)):
    p.pack_farray(len(coeff_a[i,:]), coeff_a[i,:], p.pack_double)

fileName = "coeff_plot_data.xdr"
f = open(fileName, 'w')
f.write(p.get_buffer())
f.close()

# option "-noprc" creates a 2D projection of the 3D plot, and does not embed
# the data needed to make an interactive 3D plot.
p = Popen(["asy", "plot_coeff_k2.asy", "-o", 
    outputPath + "coeff_b_publication_plot.pdf", "-noprc", "-f", "pdf"])
retcode = p.wait()
