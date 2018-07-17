#!/bin/sh
#PBS -l mem=4gb,nodes=1:ppn=1,walltime=24:00:00
#PBS -m abe
#PBS -M konox006@umn.edu
#PBS -A mcgaughs
#PBS -q lab

# Trim the whole genome VCF to just the sites that are confident, i.e., restrict
# to just single-copy sequence that is not near putative indels.

# Load modules
module load bedtools/2.25.0

# Set paths
VCF="/panfs/roc/groups/14/mcgaughs/smcgaugh/Cavefish/Astyanax_VCFs/VCFs/filtered/All_Astyanax_3.3.0_PASS_backup_copy.vcf"
BED="/panfs/roc/scratch/konox006/SEM_CaveFish/Demography/Exclude_Fixed.bed"
OUTDIR="/home/mcgaughs/shared/Datasets/demography_paper"

# Run the intersection. Be sure to include the header
(head -n 10781 ${VCF}; bedtools intersect -a ${VCF} -b ${BED} -v -wa) | gzip -c > "${OUTDIR}/All_Amex_woExclude.vcf.gz"
