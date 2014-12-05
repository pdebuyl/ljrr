ljrr: Lennard-Jones reproducible research
=========================================

Copyright © 2014 Pierre de Buyl

ljrr is a repository containing reproducible computations for Molecular Dynamics
simulations of Lennard-Jones particles.

ljrr is written by Pierre de Buyl and is released under the modified BSD
license that can be found in the file LICENSE.

Requirements and usage
----------------------

ljrr requires [lammps](http://lammps.sandia.gov),
[Make](http://www.gnu.org/software/make/) and a program called `sftmpl` (for
"Single file templater") that is available via pip

    pip install sftmpl

or at <https://github.com/pdebuyl/sftmpl>. If you do not have installation
rights on your machine, you may use `pip install --user sftmpl`.
The custom dump style for [H5MD](http://nongnu.org/h5md/) is available at
https://github.com/pdebuyl/lammps and is needed to take advantage of the
analysis tools in ljrr.

To reproduce the test computation, invoke the make command.

    make

This runs a simulation and stores the result in `simu_lj3d_test` (where `test`
is the name of the simulation run and can be adjusted with the `RUN` argument to
make). 

If a lammps executable named `lmp_mpi` is not found in your PATH environment
variable, you may specify it on the command-line

    make LMP=/path/to/lammps

Specific parameters to the Lennard-Jones system can be appended to the
command-line as `RHO` (density), `NSTEPS` (number of steps for the run), `SIDE`
(number of particles along each dimension, so that the total number is
`SIDE**3`) and `SEED`. If no seed is given, a new one is generated from the
`/dev/urandom` device of your computer.

    make RHO=0.6 SEED=123

The default values are `RHO=0.8`, `SIDE=10`, `NSTEPS=10000`, `RUN=test`.

