#!/usr/bin/env python

import sys
import os

input_file = open(sys.argv[1], 'r')

output_file = open('fasta_output.txt', 'w')

for line in input_file:

    line = line.lower()

    #print >> output_file,line
    output_file.write(line)

input_file.close()

output_file.close()
