#!/usr/bin/env python

import sys
import os

#f= open('fasta_input.txt','r')
f = open(sys.argv[1], 'r')
save = open('fasta_output.txt', 'w')

#text=f.read()

for line in f:
     line = line.lower()
     save.write(line)

save.close()
