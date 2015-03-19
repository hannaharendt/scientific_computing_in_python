#!/usr/bin/env python

"""
   This version of the function addDict initializes an empty dict, which is subsquently populated by the
   two dictionaries to be added.

   Drawback:
   1.  This is not generalizable to lists.
"""

def addDict(d1, d2):
     new = {}
     for key in d1.keys():
          new[key] = d1[key]
     for key in d2.keys():
          new[key] = d2[key]
     return new

if __name__ == '__main__':
     a = {1:1, 2:2}
     b = {2:2, 3:3}
     print addDict(a, b)

