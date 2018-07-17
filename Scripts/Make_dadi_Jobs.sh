#!/bin/bash
# This is a dumb script that will just generate a series of command lines to
# pass to GNU parallel to run dadi analyses on MSI.

# Set paths. These are MSI paths, not local workstation paths.
DATA_DIR="/home/mcgaughs/konox006/Projects/Demography/Data/2DSFS_Invariant"
DADI_SCRIPT="/home/mcgaughs/konox006/Projects/GH/SEM_CaveFish/Demography/Scripts/SEM_CaveFish_Dadi.py"

# Set the mdoels to run
MODELS=("SI" "SC" "AM" "IM" "SC2M" "IM2M" "AM2M")
# And the number of reps
NREPS=50

for sfs in $(find ${DATA_DIR} -name '*.sfs' | sort -V)
do
    pop1=$(basename ${sfs} | cut -f 1 -d '_')
    pop2=$(basename ${sfs} | cut -f 2 -d '_')
    loclen=$(grep -i 'sites' ${sfs} | awk '{print $3}')
    for mod in ${MODELS[@]}
    do
        for ((r=1;r<=${NREPS};r++))
        do
            out="${pop1}-${pop2}-rep${r}"
            echo "python ${DADI_SCRIPT} -f ${sfs} -p ${pop1} -p ${pop2} -l ${loclen} -n 500 -r 1 -m ${mod} -o ${out}"
        done
    done
done
