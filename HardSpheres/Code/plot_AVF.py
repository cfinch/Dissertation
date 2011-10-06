#!/usr/bin/env python
from numpy import *
import tables
from subprocess import Popen
import xdrlib

### Setup ###

# Path for loading data from Brownian Dynamics simulation
basePath = "/home/cfinch/Brownian_Dynamics/Data/noColloidalForces/Blocking/"
baseName = "ConstantC/150x150/vf01/Results/"
outputPath = "../Plots/AVF_publication_plot"

### Load Data ###
h5fileName = basePath + baseName + "AVF_average.h5"
print "Loading " + h5fileName

h5file = tables.openFile(h5fileName, mode="r")
AVF_h_theta = h5file.root.AVF.read()
theta_values = h5file.root.theta.read()
h_values = h5file.root.h.read()
h5file.close()

p = xdrlib.Packer()

p.pack_array(h_values, p.pack_double)       # x
p.pack_array(theta_values, p.pack_double)   # y

for i in range(len(h_values)):
    p.pack_farray(len(AVF_h_theta[i,:]), AVF_h_theta[i,:], p.pack_double)

fileName = "AVF_plot_data.xdr"
f = open(fileName, 'w')
f.write(p.get_buffer())
f.close()

# option "-noprc" creates a 2D projection of the 3D plot, and does not embed
# the data needed to make an interactive 3D plot.
p = Popen(["asy", "plot_AVF.asy", "-o", outputPath + ".pdf", "-noprc", "-f", "pdf"])

retcode = p.wait()
