#!/bin/bash

trap exit SIGINT

until SEED=$(head --bytes=2 /dev/urandom | od -t u2 | head -n1 | awk '{print $2}') && \
sftmpl $@ --seed ${SEED} > in.lj3d && \
${LMP} -i in.lj3d && \
../check_T.py .
do
    :
done
