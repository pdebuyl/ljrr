
LMP=lmp_mpi
RUN=test
SEED=NONE
RHO=0.8
SIDE=10
NSTEPS=10000

lj3d:
	mkdir -p simu_lj3d_$(RUN)
ifeq ($(SEED),NONE)
	$(eval SEED=$(shell head --bytes=2 /dev/urandom | od -t u2 | head -n1 | awk '{print $$2}'))
endif
	sftmpl in.lj3d.tmpl --seed ${SEED} --rho ${RHO} --side ${SIDE} --nsteps ${NSTEPS} > simu_lj3d_$(RUN)/in.lj3d
	(cd simu_lj3d_$(RUN) ; $(LMP) -i in.lj3d)

