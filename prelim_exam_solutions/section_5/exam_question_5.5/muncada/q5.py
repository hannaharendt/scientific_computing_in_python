#!/usr/bin/env python

import sys

filename = sys.argv[1]

input_file = open(filename, 'r')
output_file = open('fasta_output.txt', 'w')

for line in input_file:
    if line[0] != '>':
        output_file.write(line.lower())
    else:
        output_file.write(line)    # no string method lower() appended.  Line is printed as is.

input_file.close()
output_file.close()
