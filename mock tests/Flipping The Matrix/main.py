# !/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def flippingMatrix(matrix):
    # Write your code here
    n = len(matrix)
    res = 0

    for i in range(n):
        for j in range(n):

    
    
if __name__ == '__main__':
    n = int(input().strip())

    matrix = []

    for _ in range(2 * n):
        matrix.append(list(map(int, input().rstrip().split())))

    result = flippingMatrix(matrix)
    # print(result)
        
