#!/bin/bash

if [ "$SEED" = "NONE" ]
then
    SEED=$(head --bytes=2 /dev/urandom | od -t u2 | head -n1 | awk '{print $2}')
fi
echo $SEED
sftmpl $@ --seed ${SEED} > in.lj3d
${LMP} -i in.lj3d
