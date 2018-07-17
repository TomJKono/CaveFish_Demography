#!/usr/bin/env python
"""A Python package to run Dadi (Gutenkunst et al. 2009, PLoS Genetics) on cave
fish data. We chose a Python package format for easier maintenance and
extension (can plug in new models, new optimization algorithms etc.).

Author: Thomas Kono (konox006@umn.edu)
Date: 2017-10-17"""

import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt


def main():
    """The main function. Controls the execution of the script."""
    # Import and run the module testing script
    from cavefish_dadi.Support import module_test
    bad_deps = module_test.test_imports()
    if bad_deps:
        exit(1)
    # Import the argument checking script
    from cavefish_dadi.Support import arguments
    # Import the demographic model class
    from cavefish_dadi.Models import demo_model
    # Parse the arguments
    args = arguments.parse_args()
    if not args:
        exit(1)
    # For each model
    for model in args.model:
        # Start a new DemoMod object. This reads the SFS data, sets the model
        # function, and sets the optima search algorithm
        dm = demo_model.DemoModel(
            args.sfs,
            model,
            args.pop,
            args.out)
        # Then, fit the model to the data
        dm.infer(args.niter, args.replicates)
        dm.summarize(args.length)
        dm.write_out(args.niter, args.length)
        dm.plot(vmin=1, vmax=100000)
    return


main()
