#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    pos,neg,zero = 0,0,0
    for i in  arr:
        if i > 0:
            pos+=1
        elif i == 0:
            zero+=1
        else:
            neg +=1

    print('{0:f}'.format((pos/len(arr)))) 
    print('{0:f}'.format((neg/len(arr))))
    print('{0:f}'.format((zero/len(arr))))  

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
