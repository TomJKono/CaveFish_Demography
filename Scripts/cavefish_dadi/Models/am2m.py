#!/usr/bin/env python
"""Implement the multiclass ancient migration (AM2M) model."""

import numpy
import dadi


def am2m(params, (n1,n2), pts):
    nu1, nu2, m12, m21, me12, me21, Tam, Ts, P = params
    """
    Ancient Migration model with two categories of loci experiencing different migration rates.

    nu1: Size of population 1 after split.
    nu2: Size of population 2 after split.
    m12: Migration from pop 2 to pop 1 (2*Na*m12).
    m21: Migration from pop 1 to pop 2.
    me12: Effective migration from pop 2 to pop 1 in genomic islands.
    me21: Effective migration from pop 1 to pop 2 in genomic islands.
    Tam: The scaled time between the split and the end of ancient migration (in units of 2*Na generations).
    Ts: The scaled time between the end of ancient migration and present.
    P: The porportion of the genome evolving neutrally
    n1,n2: Size of fs to generate.
    pts: Number of points to use in grid for evaluation.
    """
    # Define the grid we'll use
    xx = dadi.Numerics.default_grid(pts)

    ### Calculate the neutral spectrum
    # phi for the equilibrium ancestral population
    phiN = dadi.PhiManip.phi_1D(xx)
    # Now do the divergence event
    phiN = dadi.PhiManip.phi_1D_to_2D(xx, phiN)
    # We set the population sizes after the split to nu1 and nu2 and the migration rate to m12 and m21
    phiN = dadi.Integration.two_pops(phiN, xx, Tam, nu1, nu2, m12=m12, m21=m21)
    # We keep the population sizes after the split to nu1 and nu2 and set the migration rates to zero
    phiN = dadi.Integration.two_pops(phiN, xx, Ts, nu1, nu2, m12=0, m21=0)
    # calculate the spectrum.
    fsN = dadi.Spectrum.from_phi(phiN, (n1,n2), (xx,xx))

    ### Calculate the genomic island spectrum
    # phi for the equilibrium ancestral population
    phiI = dadi.PhiManip.phi_1D(xx)
    # Now do the divergence event
    phiI = dadi.PhiManip.phi_1D_to_2D(xx, phiI)
    # We set the population sizes after the split to nu1 and nu2 and the migration rate to zero
    phiI = dadi.Integration.two_pops(phiI, xx, Tam, nu1, nu2, m12=me12, m21=me21)
    # We keep the population sizes after the split to nu1 and nu2 and set the migration rates to me12 and me21
    phiI = dadi.Integration.two_pops(phiI, xx, Ts, nu1, nu2, m12=0, m21=0)
    # calculate the spectrum.
    fsI = dadi.Spectrum.from_phi(phiI, (n1,n2), (xx,xx))

    ### Sum the two spectra in proportion P
    fs = P*fsN+(1-P)*fsI
    return fs
