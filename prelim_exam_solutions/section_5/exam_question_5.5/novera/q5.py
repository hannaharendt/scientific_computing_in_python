#!/usr/bin/env python

import os
import sys


fileVar = open(sys.argv[1], 'r')    # argv[0] is name of program

fileVarOut = open("fasta_output.txt", 'w')

lines = fileVar.readline()

 

while lines:

     lines.lower()

     fileVarOut.write(lines)    # not a string, but a reference variable to the line being processed

     lines = fileVar.readline()


fileVar.close()

fileVarOut.close()
