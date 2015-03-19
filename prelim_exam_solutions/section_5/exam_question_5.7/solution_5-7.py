#!/usr/bin/env python

"""
Explanation:

 Make a new tuple from its parts by slicing and concatenating.  
You could also convert the tuple to a list, chafe it in-place, 
and convert it back to a tuple, but this is more expensive and 
is rarely required in practice - simply use a list if you know that 
the object will require in-place changes.

Brief Explanation:  Because they are immutable, 
you can't really change tuples in-place, 
but you can generate a new tuple with the desired value.
"""

T = (4, 5, 6)
print 'Before change:'
print T; print

T = (1,) + T[1:] # Recall that single item tuples require a trailing comma
print 'After change:'
print T; print
