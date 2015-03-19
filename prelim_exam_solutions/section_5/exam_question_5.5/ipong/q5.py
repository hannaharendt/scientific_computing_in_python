#!/usr/bin/env python

import os

import sys



filename = sys.argv[1]



r = open(filename, "r")

w = open("fasta_output.txt", "w")

lines = r.readline();

#lines2 = ""    # superfluous

while(lines):

    if not lines.startswith(">"):

        lines = lines.lower()
        w.write(lines)
    else:
        w.write(lines)

    lines = r.readline()    



r.close()

w.close()
