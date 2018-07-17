#!/usr/bin/evn python
"""Make a BED file to exclude sites aorund putative indels and heterozygous
sites. Note that the intervals that come out of this script should be collapsed
with bedtools prior to filtering. Takes one argument:
    1) VCF with invariant sites
"""

import sys
import gzip

with gzip.open(sys.argv[1], 'rb') as f:
    for line in f:
        if line.startswith('#'):
            continue
        else:
            tmp = line.strip().split()
            # First check if the site is an indel
            chrom = tmp[0]
            pos = int(tmp[1])
            ref = tmp[3]
            alt = tmp[4]
            if len(ref) != 1 or len(alt) != 1:
                # exclude 3 bp upstream and downstream. Be sure to handle the
                # converstion from VCF (1-based) to BED (0-based).
                ex_start = pos - 4
                ex_end = pos + 2
                # And, if the start is negative, we set it to 0
                if ex_start < 0:
                    ex_start = 0
                # Print the interval
                print '\t'.join([chrom, str(ex_start), str(ex_end)])
            else:
                # Then, check for heterozygosity
                gt = [x.split(':')[0] for x in tmp[9:]]
                # Remove missing calls
                non_missing = [x for x in gt if x != './.']
                het = [True if x == '0/1' or x == './.' else False for x in non_missing]
                if all(het):
                    print '\t'.join([chrom, str(pos-1), str(pos)])
                else:
                    continue
