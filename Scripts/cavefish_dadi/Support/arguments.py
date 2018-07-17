#!/usr/bin/env python
"""Set up and parse command line arguments for the cave fish dadi analysis."""

import sys
import argparse

# A list of models that have been implemented already.
MODELS = ['SI', 'SC', 'AM', 'IM', 'SC2M', 'AM2M', 'IM2M']


def parse_args():
    """Set up an argument parser, and parse then arguments with it."""
    # This is the main argument parser object
    parser = argparse.ArgumentParser(
        description='Cave fish dadi analyses',
        add_help=True)
    # Add some arguements to it.
    parser.add_argument(
        '-f',
        '--sfs',
        required=True,
        help='Joint SFS file, in dadi format')
    parser.add_argument(
        '-m',
        '--model',
        required=True,
        action='append',
        choices=MODELS,
        type=str,
        help='Specify a model to run. May be specified multiple times, with different models.')
    parser.add_argument(
        '-p',
        '--pop',
        required=True,
        action='append',
        type=str,
        help='Population labels. Must be specified in order that they are listed in dadi SFS file.')
    parser.add_argument(
        '-o',
        '--out',
        required=False,
        default='CaveFish_Dadi_Out',
        help='Output prefix for results files. Defaults to CaveFish_Dadi_Out')
    parser.add_argument(
        '-n',
        '--niter',
        required=False,
        default=10,
        type=int,
        help='Number of iterations for the simulated annealing.')
    parser.add_argument(
        '-r',
        '--replicates',
        required=False,
        default=1,
        type=int,
        help='Number of replicates to perform for each model.')
    parser.add_argument(
        '-l',
        '--length',
        required=True,
        type=int,
        help='Length of the locus. Note that this is the size of region, including invariant sites, that was used to generate the SFS.')
    if len(sys.argv) == 1:
        parser.print_help()
        return
    else:
        args = parser.parse_args()
        return args
