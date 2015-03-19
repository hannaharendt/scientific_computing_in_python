#!/usr/bin/env python

import sys
import os

if len(sys.argv) < 2:
	raise ValueError(' No input file provided in program execution. Please supply input file name argument.')

else:
        input = open(sys.argv[1], "r")
        output = open("fasta_output.txt", "w")

        for line in input:
                if line.startswith('>'):
                        output.write(line)
                else:
                        output.write(line.lower())

        input.close()
        output.close()

