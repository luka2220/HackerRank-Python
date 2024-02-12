#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    return min(a, key=a.count)

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))
 
    result1 = lonelyinteger(a)    
