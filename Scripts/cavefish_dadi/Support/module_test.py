#!/usr/bin/env python
"""Test for the installation of necessary modules."""


def test_imports():
    """Run the import statements and print messages about them not being
    correct."""
    mod_problems = False
    try:
        import dadi
        dadi_exists = True
    except ImportError:
        dadi_exists = False

    try:
        import matplotlib
        matplotlib.use('agg')
        import matplotlib.pylab as plt
        matplotlib_exists = True
    except ImportError:
        matplotlib_exists = False

    try:
        import scipy
        assert scipy.__version__ == '0.14.0'
        scipy_exists = True
        scipy_version = True
    except ImportError:
        scipy_exists = False
        scipt_version = False
    except AssertionError:
        scipy_exists = True
        scipy_version = False

    if not all([dadi_exists, matplotlib_exists, scipy_exists, scipy_version]):
        print 'Some module errors were found on your system:\n'
        mod_problems = True
    if not dadi_exists:
        print 'You do not have dadi installed. Please download it from'
        print 'https://bitbucket.org/gutenkunstlab/dadi and install it.\n'
    if not matplotlib_exists:
        print 'You do not have matplotlib installed. Please install it with'
        print '"pip install matplotlib".\n'
    if not scipy_exists and not scipy_version:
        print 'You do not have SciPy version 0.14.0 installed. Please install'
        print 'it with \'pip install "scipy==0.14"\'.\n'
    if scipy_exists and not scipy_version:
        print 'Your scipy version (' + scipy.__version__ + ') is incompatible'
        print 'with this script. Please install version 0.14 by running'
        print '\'pip install "scipy==0.14"\n'
    return mod_problems
