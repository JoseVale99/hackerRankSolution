# Enter your code here. Read input from STDIN. Print output to STDOUTfrom itertools import permutations
from itertools import permutations
"""
itertools.permutations(iterable[, r])

This tool returns successive  length permutations of elements in an iterable.

If  is not specified or is None, then  defaults to the length of the iterable, and all possible full length permutations are generated.

Permutations are printed in a lexicographic sorted order. So, if the input iterable is sorted, the permutation tuples will be produced in a sorted order.
"""
if __name__ == '__main__':
    s, max_width = input('').split()
    for string in sorted(list(permutations(s, int(max_width)))):
        print(''.join(string)) 