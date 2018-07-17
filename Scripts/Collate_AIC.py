#!/usr/bin/env python
"""Collate the AIC values into a nice matrix for estimating the Akaike weights
for model selection. Takes two arguments:
    1) Directory of model output text files.
    2) Population name prefix
"""

import os
import sys
import pprint

try:
    fpath = os.path.abspath(os.path.expanduser(sys.argv[1]))
    popcomp = sys.argv[2]
except IndexError:
    print """Collate the AIC values into a nice matrix for estimating the Akaike weights
for model selection. Takes two arguments:
    1) Directory of model output text files.
    2) Population name prefix"""
    exit(1)
except IOError:
    print 'The directory you specified does not exist, or is not readable.'
    exit(1)

# Define the models in a dictionary to build up
MODELS = {
    'SI': [],
    'SC': [],
    'IM': [],
    'AM': [],
    'SC2M': [],
    'IM2M': [],
    'AM2M': []}

# Define the replicates to search for
REPS = [str(i) for i in range(1, 51)]

# Start iterating through the models and reps
for m in MODELS:
    for r in REPS:
        try:
            fname = popcomp.replace('-', '_') + '_' + popcomp + '-rep' + r + '_' + m + '.txt'
            with open(os.path.join(fpath, fname), 'r') as f:
                for line in f:
                    if line.startswith('#AIC'):
                        aic = line.strip().split()[1]
                        break
        except IOError:
            aic = 'NA'
        MODELS[m].append(aic)

# Then print it out, with the models as column headers
print '\t'.join(sorted(MODELS.keys()))
for index, r in enumerate(REPS):
    toprint = []
    for m in sorted(MODELS):
        toprint.append(MODELS[m][index])
    print '\t'.join(toprint)
