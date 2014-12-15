ljrr: Lennard-Jones reproducible research
=========================================

Copyright © 2014 Pierre de Buyl

ljrr is a repository containing reproducible computations for Molecular Dynamics
simulations of Lennard-Jones particles.
The parameters are those of the
[benchmark simulations](http://www.nist.gov/mml/csd/informatics_research/lj_pure.cfm)
proposed by the
[National Institute of Standards and Technology (NIST)](http://nist.gov/) for
the "MD NVE" category.

ljrr is written by Pierre de Buyl and is released under the modified BSD
license that can be found in the file LICENSE.

Requirements and usage
----------------------

ljrr requires:

- [lammps](http://lammps.sandia.gov)
- [Make](http://www.gnu.org/software/make/)
- [bash](https://www.gnu.org/software/bash/)
- [HDF5](http://www.hdfgroup.org/HDF5/)
- [Python](https://www.python.org/) with [NumPy](http://www.numpy.org/),
  [matplotlib](http://matplotlib.org/) and [h5py](http://www.h5py.org/)

Apart from lammps that requires a separate installation, the other packages can
be installed under Debian with

    apt-get install make bash libhdf5-dev hdf5-tools python python-numpy python-matplotlib python-h5py

The program called `sftmpl` (for "Single file templater") is available via
pip

    pip install sftmpl


or at <https://github.com/pdebuyl/sftmpl>. If you do not have installation
rights on your machine, you may use `pip install --user sftmpl`.

The custom dump style for [H5MD](http://nongnu.org/h5md/) is available at
<https://github.com/pdebuyl/lammps> and is needed to take advantage of the
analysis tools in ljrr.

To reproduce the test computation, invoke the make command.

    make all_nist

This runs simulations for all parameters of the nist benchmark and stores the
simulation results in `simu_lj3d_NIST_{RHO}` (where `{RHO}` is the value of the
density).
The program `code/compute_rdf.py` then computes the radial distributions
function from the simulation data and stores it in `data/nist_{RHO}_rdf.txt`.

If a lammps executable named `lmp_mpi` is not found in your PATH environment
variable, you may specify it on the command-line

    make all_nist LMP=/path/to/lammps

Specific parameters to the Lennard-Jones system can be appended to the
command-line as `RHO` (density), `NSTEPS` (number of steps for the run), `SIDE`
(number of particles along each dimension, so that the total number is
`SIDE**3`) and `SEED`. If no seed is given, a new one is generated from the
`/dev/urandom` device of your computer.

    make RHO=0.6 SEED=123
