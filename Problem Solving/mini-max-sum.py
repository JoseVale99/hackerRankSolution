#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    aux, final = [],[]
    for i in range(len(arr)):
        aux = []
        for j in range(len(arr)):
            if i != j:
                aux.append(arr[j])
        final.append(sum(aux))
    
    print(min(final), max(final)) 



if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
