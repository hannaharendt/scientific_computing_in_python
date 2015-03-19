#!/usr/bin/env python

import sys
import os

if sys.argv[1]:
	ipt = open(sys.argv[1], "r")
	out = open("fasta_output.txt", "w")

	for line in ipt:
		if ">" in line:
			out.write(line)
		else:
			out.write(line.lower())

	ipt.close()
	out.close()
