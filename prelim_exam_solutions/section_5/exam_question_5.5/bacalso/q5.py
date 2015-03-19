#!/usr/bin/env python

file1 = open('fasta_input.txt', 'r')

lol = file1.read()

low = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',

       'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',

       'u', 'v', 'w', 'x', 'y', 'z')

def check(n):

        for x in low:

                if x == n:

                        return True

                        break

        return False

yo = ''

for n in lol:

        if check(n):

                yo+= n.upper()

                

        else:

                yo+= str(n.lower())



file2 = open('fasta_output.txt', 'w')

file2.write(yo)

file1.close()

file2.close()


