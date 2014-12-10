
LMP=lmp_mpi
RUN=test
SEED=NONE
RHO=0.8
SIDE=10
NSTEPS=20000
TEMPERATURE=0.85

lj3d:
	mkdir -p simu_lj3d_$(RUN)
	(cd simu_lj3d_$(RUN) ; SEED=$(SEED) LMP="$(LMP)" ../run_lj3d.sh ../in.lj3d.tmpl --rho ${RHO} --temp ${TEMPERATURE} --side ${SIDE} --nsteps ${NSTEPS})

nist: TEMPERATURE=0.85
nist: RUN=NIST_$(RHO)
nist: SIDE=8
nist:  lj3d
