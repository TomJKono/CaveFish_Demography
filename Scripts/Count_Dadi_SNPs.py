#!/usr/bin/env python
"""A really simple script to count the number of vairants that are in
non-masked regions of the genome. Takes one argument:
    1) Dadi SFS input file
"""

import sys
import os
import subprocess


def main(sfs):
    """Main function."""
    # Tail the last two lines of the file. Sanitize the path and use the
    # subprocess module to call the command. This is ugly, but safe.
    fp = os.path.abspath(os.path.expanduser(sfs))
    cmd = ['tail', '-n', '2', fp]
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    o, e = proc.communicate()
    # Take stdout. 
    nsites, mask = o.strip().split('\n')
    # Split the number of sites and the mask on whitespace
    nsites = nsites.strip().split()
    mask = mask.strip().split()
    # Start accumulating the number of SNPs, based on masked
    snps = 0
    for n, m in zip(nsites, mask):
        if m == '1':
            continue
        else:
            snps += int(n)
    # Print it out. First get the basename of the input file and then print
    # the accumulated NSNPs
    popname = os.path.split(sfs)[1]
    print popname, snps
    return


if len(sys.argv) != 2:
    print """A really simple script to count the number of vairants that are in
non-masked regions of the genome. Takes one argument:
    1) Dadi SFS input file"""
    exit(1)
else:
    main(sys.argv[1])
