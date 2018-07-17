#!/usr/bin/env python
"""Summarize the dadi runs into a large table that is useful for comparing the
results of multiple models. This script will have a fair amount of hard-coded
values in it, so be sure to edit it before running. Takes one argument:
    1) Directory of dadi output files
"""

import sys
import os

# Define the models that we ran
MODELS = ['SI', 'SC', 'IM', 'AM', 'SC2M', 'IM2M', 'AM2M']
# Define the parameters of interest here
PARAMS = ['N1', 'N2', 'm21', 'm12', 'mi21', 'mi12', 'Ts', 'Tsc', 'Tam', 'p']
# And define the population pairs
POPS = [
    ('Choy', 'Molino'),
    ('Choy', 'Pachon'),
    ('Choy', 'Rascon'),
    ('Choy', 'Tinaja'),
    ('Molino', 'Pachon'),
    ('Molino', 'Rascon'),
    ('Molino', 'Tinaja'),
    ('Pachon', 'Rascon'),
    ('Pachon', 'Tinaja'),
    ('Rascon', 'Tinaja')]
# And the number of reps
NREPS = 50
REPS = [str(r) for r in range(1, NREPS+1)]


def main(dadidir):
    """Main function."""
    fp = os.path.abspath(os.path.expanduser(dadidir))
    # Start with header
    print 'Pop1\tPop2\tModel\tRep\t' + '\t'.join(PARAMS)
    # Start reading the data files and printing the results
    for p_pair in POPS:
        # For each pair of populations
        pop1 = p_pair[0]
        pop2 = p_pair[1]
        for m in MODELS:
            # Then, for each model
            mod = m
            for r in REPS:
                # Then, for each replicate
                rep = r
                # Build the filename from the info.
                fname = pop1 + '_' + pop2 + '_' + pop1 + '-' + pop2 + '-' + 'rep' + r + '_' + m + '.txt'
                try:
                    # This is SUPER UGLY
                    est = []
                    for p in PARAMS:
                        with open(os.path.join(fp, fname), 'r') as f:
                            for line in f:
                                if line.startswith('#' + p):
                                    est.append(line.strip().split()[1])
                                    break
                            else:
                                est.append('NA')
                    # Now that we have the parameter estimates from the dadi files,
                    # We will print the huge table out
                    print '\t'.join([pop1, pop2, mod, rep] + est)
                except IOError:
                    sys.stderr.write(fname + ' not found! Rerun it.\n')
    return


if len(sys.argv) != 2:
    print """Summarize the dadi runs into a large table that is useful for comparing the
results of multiple models. This script will have a fair amount of hard-coded
values in it, so be sure to edit it before running. Takes one argument:
    1) Directory of dadi output files"""
    exit(1)
else:
    main(sys.argv[1])
