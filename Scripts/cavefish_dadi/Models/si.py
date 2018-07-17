#!/usr/bin/env python
"""Implement the strict isolation (SI) model."""

import numpy
import dadi


def si(params, (n1,n2), pts):
    nu1, nu2, Ts = params
    """
    Strict Isolation model, no gene flow during divergence.

    nu1: Size of population 1 after split.
    nu2: Size of population 2 after split.
    Ts: The scaled time between the split and present (in units of 2*Na generations).
    n1,n2: Size of fs to generate.
    pts: Number of points to use in grid for evaluation.
    """
    # Define the grid we'll use
    xx = dadi.Numerics.default_grid(pts)

    # phi for the equilibrium ancestral population
    phi = dadi.PhiManip.phi_1D(xx)
    # Now do the divergence event
    phi = dadi.PhiManip.phi_1D_to_2D(xx, phi)
    # We set the population sizes after the split to nu1 and nu2
    phi = dadi.Integration.two_pops(phi, xx, Ts, nu1, nu2, m12=0, m21=0)
    # Finally, calculate the spectrum.
    fs = dadi.Spectrum.from_phi(phi, (n1,n2), (xx,xx))
    return fs
