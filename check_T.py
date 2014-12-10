#!/usr/bin/env python

import sys
import os
import os.path

if len(sys.argv)!=2:
    print("Usage:", sys.argv[0], "simu_directory")
    sys.exit(0)

import numpy as np
from io import StringIO

# Open lammps log file to extract thermodynamic observables
logfile = open(os.path.join(os.getcwd(),sys.argv[1], 'log.lammps')).readlines()
start_indices = [(i,l) for (i,l) in enumerate(logfile) if l.startswith('Step Time Temp')]
stop_indices = [(i,l) for (i,l) in enumerate(logfile) if l.startswith('Loop time')]

def from_log(idx=-1):
    i0 = start_indices[idx][0]
    i1 = stop_indices[idx][0]
    return np.loadtxt(StringIO(u''.join(logfile[i0+1:i1])), unpack=True)

time, step, temp, e_kin, e_vdw, press, vol, rho = from_log()

target = 0.85
T_av = temp.mean()
T_std = temp.std()

print("Temperature: {} +/- {}".format(T_av, T_std))

if (T_av-target)**2>0.002**2:
    print("Temperature too far off")
    sys.exit(1)
else:
    print("Temperature OK")
    sys.exit(0)
