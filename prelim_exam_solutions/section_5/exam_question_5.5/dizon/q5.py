#!/usr/bin/env python

import sys
input_file = open(sys.argv[1], 'r')

output_file = open('fasta_output.txt', 'w')

line = input_file.readline()

while line:
    line = line.lower()
    output_file.write(line)
    line = input_file.readline()

input_file.close()
output_file.close()
