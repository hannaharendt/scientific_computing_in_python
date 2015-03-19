#!/usr/bin/env python

"""
   The simplest addDict function simply utilizies the existing Dictionary update method.
   The drawbacks are:
   (1)  The original dictionary added to is mutated.
   (2)  The function is not generalizable to lists since lists do not have the update method.
"""

def addDict(x, y):
     x.update(y)
     return x

if __name__ == '__main__':
     d1 = {1:1, 2:2}
     d2 = {3:3, 4:4}
     d3 = {2:2, 4:4}
     l1 = [1, 2, 3, 4]
     l2 = [4, 5, 6, 7]
     print 'Original form of d1:'
     print d1; print
     print 'Calling function addDict:'
     print addDict(d1, d3); print
     print 'd1 is mutated after implementation of the update method in function.'
     print d1; print
     #print 'Function utilizing update method does not work with lists since lists do not have the update method.'
     #print addDict(l1, l2); print
     # Comment: the dictionary update method has no return value.  Dictionary y is added to Dictionary x.
     # Dictionary x is mutated from its original form to reflect the added items from Dictionary y.
     # Automatically takes care of duplicates to only contain a unique set of key:value pairs.
     # This function utilizing the update method is not generalizable to lists since lists do not have
     # the update method.


