#!/usr/bin/env python
"""Implement the secondary contact (SC) model."""

import numpy
import dadi


def sc(params, (n1,n2), pts):
    nu1, nu2, m12, m21, Ts, Tsc = params
    """
    Secondary Contact model.

    nu1: Size of population 1 after split.
    nu2: Size of population 2 after split.
    m12: Migration from pop 2 to pop 1 (2*Na*m12).
    m21: Migration from pop 1 to pop 2.
    Ts: The scaled time between the split and the secondary contact (in units of 2*Na generations).
    Tsc: The scale time between secondary contact and present.
    n1,n2: Size of fs to generate.
    pts: Number of points to use in grid for evaluation.
    """
    # Define the grid we'll use
    xx = dadi.Numerics.default_grid(pts)

    # phi for the equilibrium ancestral population
    phi = dadi.PhiManip.phi_1D(xx)
    # Now do the divergence event
    phi = dadi.PhiManip.phi_1D_to_2D(xx, phi)
    # We set the population sizes after the split to nu1 and nu2 and the migration rate to zero
    phi = dadi.Integration.two_pops(phi, xx, Ts, nu1, nu2, m12=0, m21=0)
    # We keep the population sizes after the split to nu1 and nu2 and set the migration rates to m12 and m21
    phi = dadi.Integration.two_pops(phi, xx, Tsc, nu1, nu2, m12=m12, m21=m21)

    # Finally, calculate the spectrum.
    fs = dadi.Spectrum.from_phi(phi, (n1,n2), (xx,xx))
    return fs
