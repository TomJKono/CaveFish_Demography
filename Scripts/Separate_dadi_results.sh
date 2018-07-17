#!/bin/bash
# Separate the dadi results by population, into their own directory.

DADI_DIR="$1"

POP1=(
    "Choy" "Choy" "Choy" "Choy"
    "Molino" "Molino" "Molino"
    "Rascon" "Rascon"
    "Pachon"
    )
POP2=(
    "Molino" "Rascon" "Pachon" "Tinaja"
    "Rascon" "Pachon" "Tinaja"
    "Pachon" "Tinaja"
    "Tinaja"
    )

for ((i=0;i<=9;i++))
do
    p1=${POP1[$i]}
    p2=${POP2[$i]}
    mkdir -p "${PWD}/${p1}-${p2}"
    cp ${DADI_DIR}/${p1}_${p2}*.txt ${PWD}/${p1}-${p2}/
done
