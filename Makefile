
LMP=lmp_mpi
RUN=test
SEED=NONE
RHO=0.8
SIDE=10
NSTEPS=20000
TEMPERATURE=0.85

lj3d:
	mkdir -p simu_lj3d_$(RUN)
	(cd simu_lj3d_$(RUN) ; SEED=$(SEED) LMP="$(LMP)" ../run_until_lj3d.sh ../in.lj3d.tmpl --rho ${RHO} --temp ${TEMPERATURE} --side ${SIDE} --nsteps ${NSTEPS})

%.nist: TEMPERATURE=0.85
%.nist: RUN=NIST_$(RHO)
%.nist: SIDE=8
%.nist: lj3d
	@echo in nist with RHO=$(RHO)

values := 0.776 0.780 0.820 0.840 0.860 0.900

%.settings: TEMPERATURE=0.85
%.settings: SIDE=8
%.settings:
	$(eval RHO=$*)
	$(eval RUN=NIST_$(RHO))
	$(eval SIDE=8)
	$(eval TEMPERATURE=0.85)
	@echo in settings

simu_lj3d_NIST_%/log.lammps simu_lj3d_NIST_%/dump_3d.h5 simu_lj3d_NIST_%/in.lj3d: %.settings
	@echo in simu RHO=$(RHO) stem=$* RUN=$(RUN)
	mkdir -p simu_lj3d_$(RUN)
	(cd simu_lj3d_$(RUN) ; SEED=$(SEED) LMP="$(LMP)" ../run_until_lj3d.sh ../in.lj3d.tmpl --rho ${RHO} --temp ${TEMPERATURE} --side ${SIDE} --nsteps ${NSTEPS})

data/nist_%_rdf.txt: simu_lj3d_NIST_%/dump_3d.h5 code/compute_rdf.py | data
	python code/compute_rdf.py $< $@

.SECONDARY: $(foreach v, $(values), simu_lj3d_NIST_$(v)/log.lammps) \
	$(foreach v, $(values), simu_lj3d_NIST_$(v)/dump_3d.h5) \
	$(foreach v, $(values), simu_lj3d_NIST_$(v)/in.lj3d) \
	$(foreach v, $(values), data/nist_$(v)_rdf.txt)

data:
	mkdir -p data

all_nist: $(foreach v, $(values), data/nist_$(v)_rdf.txt)

data/nist_rdf.png: code/plot_rdf.py $(foreach v, $(values), data/nist_$(v)_rdf.txt)
	python $< $@ $(foreach v, $(values), data/nist_$(v)_rdf.txt)
