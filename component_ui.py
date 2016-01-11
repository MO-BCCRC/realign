'''
Created on Sep 08, 2014

@author: raniba
'''

import argparse

__version__ = '0.0.1'


#==============================================================================
# make a UI
#==============================================================================
parser = argparse.ArgumentParser(
    prog='realign',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    description=''' This script is used as a wrapper for GATK IndelRealigner
                    It is important to use this component with create_target component that should
                    be called first.
                    It takes as input the target file, a sorted bam file, and a reference Genome
                    and it generate a realigned bam file''')

# required arguments
parser.add_argument('--infile', metavar='INPUT',
                    help='Targets file created by the create_targets component')

parser.add_argument('--sorted_alignment', metavar='SORTED_ALIGNMENT',
                    help='A BAM file to be realigned')

parser.add_argument('--ref_genome', metavar='REF_GENOME',
                    help='Reference Genome)

parser.add_argument('--outfile', metavar='OUTPUT',
                    help='Realigned bam file')

args, x = parser.parse_known_args()
