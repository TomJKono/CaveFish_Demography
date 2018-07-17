#!/usr/bin/env python
"""Parse the VCF with invariant sites, and generate a 2D SFS for dadi input.
We will use all sitest hat are applicable, despite them being variant or not.
This is because we want an accurate denominator for the locus length in scaling
the parameter estimates for divergence times and effective population sizes to
real values. We will skip sites that have any missing data in any of the
populations of interest. Takes three arguments:
    1) Gzipped VCF with invariant sites
    2) Population 1 name
    3) Populaiton 2 name
"""

import sys
import gzip
import pprint


# Unpack arguments
try:
    gzvcf = sys.argv[1]
    pop1 = sys.argv[2]
    pop2 = sys.argv[3]
except IndexError:
    print """Parse the VCF with invariant sites, and generate a 2D SFS for dadi input.
We will use all sitest hat are applicable, despite them being variant or not.
This is because we want an accurate denominator for the locus length in scaling
the parameter estimates for divergence times and effective population sizes to
real values. We will skip sites that have any missing data in any of the
populations of interest. Takes three arguments:
    1) Gzipped VCF with invariant sites
    2) Population 1 name
    3) Populaiton 2 name"""
    exit(1)

# Define a population name dictionary, because the VCF doesn't have the full
# names of the populations in the header
POPNAMES = {
    'Choy': 'Choy',
    'Molino': 'Molino',
    'Pachon': 'Pach',
    'Rascon': 'Rascon',
    'Tinaja': 'Tinaja'}

# We want to exclude individuals that are admixed, or appear to be of recent
# hybrid origin.
EXCLUDE = ['Rascon_6', 'Tinaja_6', 'Choy_14', 'Tinaja_E']

# Translate the names from the full name into the VCF name
pop1 = POPNAMES[pop1]
pop2 = POPNAMES[pop2]
# And define the ancestral
ANCESTRAL = 'White_Long_Fin'

# Start a counter for the number of sites considered
n_sites = 0

with gzip.open(gzvcf, 'rb') as f:
    for line in f:
        if line.startswith('##'):
            continue
        elif line.startswith('#CHROM'):
            header = line.strip().split()
            # Get the indices of the sample fields we want to process
            pop1_samples = [i for i, s in enumerate(header) if pop1 in s and s not in EXCLUDE]
            pop2_samples = [i for i, s in enumerate(header) if pop2 in s and s not in EXCLUDE]
            anc_sample = header.index(ANCESTRAL)
            # Write some output to stderr
            sys.stderr.write('Pop 1: ' + ','.join([header[i] for i in pop1_samples]) + '\n')
            sys.stderr.write('Pop 2: ' + ','.join([header[i] for i in pop2_samples]) + '\n')
            sys.stderr.write('Anc: ' + ANCESTRAL + '\n')
            # How many alleleic states can we identify?
            pop1_n = (2*len(pop1_samples)) + 1
            pop2_n = (2*len(pop2_samples)) + 1
            # Then, start an empty matrix to hold the SFS data. Rows will be
            # pop1 samples, and columns will be pop2 samples.
            sfs = []
            for i in range(0, pop1_n):
                tmp = []
                for j in range(0, pop2_n):
                    tmp.append(0)
                sfs.append(tmp)
        else:
            tmp = line.strip().split()
            # Check ref and alt. If there are length polymorphisms, we want to
            # avoid those.
            ref = tmp[3]
            alt = tmp[4]
            if len(ref) != 1 or len(alt) != 1:
                continue
            # Now, we are in the data rows. First, subset the genotypes
            pop1_geno = [tmp[g].split(':')[0] for g in pop1_samples]
            pop2_geno = [tmp[g].split(':')[0] for g in pop2_samples]
            anc_geno = tmp[anc_sample].split(':')[0]
            # In the cases where the ancestral genotype is missing or hetero-
            # zygous, we skip it. We also skip sites with any missing data
            # because then the sample size is messed up.
            if anc_geno not in ['0/0', '1/1'] or './.' in pop1_geno or './.' in pop2_geno:
                continue
            # Next, we count up the derived alleles
            if anc_geno == '0/0':
                derived = '1'
                anc = '0'
            elif anc_geno == '1/1':
                derived = '0'
                anc = '1'
            pop1_der = 0
            pop2_der = 0
            for call in pop1_geno:
                if call == derived + '/' + derived:
                    pop1_der += 2
                elif call == derived + '/' + anc or call == anc + '/' + derived:
                    pop1_der += 1
                else:
                    pop1_der += 0
            for call in pop2_geno:
                if call == derived + '/' + derived:
                    pop2_der += 2
                elif call == derived + '/' + anc or call == anc + '/' + derived:
                    pop2_der += 1
                else:
                    pop2_der += 0
            # Then, put them into the matrix
            sfs[pop1_der][pop2_der] += 1
            n_sites += 1

# Unpack the SFS into the vector expected by dadi, and build the mask
sfs_vec = []
mask = []
for row in sfs:
    for col in row:
        sfs_vec.append(str(col))
        mask.append('0')

# Then, we want to mask the fixed sites, and the sites at 50% frequency in
# both populations.
mask[0] = '1'
mask[-1] = '1'
het_offset = (len(mask)-1)/2
mask[het_offset] = '1'

# Print the SFS. We can inclue comment lines.
print '#Pop 1: ' + pop1
print '#Pop 1 Samples: ' + ','.join([header[i] for i in pop1_samples])
print '#Pop 2: ' + pop2
print '#Pop 2 Samples: ' + ','.join([header[i] for i in pop2_samples])
print '#Ancestral: ' + ANCESTRAL
print '#N sites: ' + str(n_sites)
print pop1_n, pop2_n, 'unfolded'
print ' '.join(sfs_vec)
print ' '.join(mask)
