#!/usr/bin/env python

import os, sys

path = sys.argv[1]

in_f = open(path, 'r')
to_f = open('fasta_output.txt', 'w')

for anything in in_f:
	if anything.startswith('>'): # Added correction
		to_f.write(anything) # Added correction
	else:
		to_f.write(anything.lower())

in_f.close()
to_f.close()
