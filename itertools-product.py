from itertools import product
"""
itertools.product()

This tool computes the cartesian product of input iterables.
It is equivalent to nested for-loops.
For example, product(A, B) returns the same as ((x,y) for x in A for y in B).
"""

if __name__ == '__main__':
    a = input().split()
    b = input().split()
    
    a = sorted([int(x) for x in a])
    b = sorted([int(x) for x in b])
    print(*list(product(a,b)))
   