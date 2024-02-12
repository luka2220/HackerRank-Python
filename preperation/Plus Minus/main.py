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
    # Write your code here
    positive_count = 0
    negative_count = 0
    zero_count = 0

    for num in arr:
        if num > 0:
            positive_count += 1
        elif num < 0:
            negative_count += 1
        else:
            zero_count += 1

    positive_count = positive_count / n
    negative_count = negative_count / n
    zero_count = zero_count / n

    pos = format(positive_count, '.6f')
    neg = format(negative_count, '.6f')
    zero = format(zero_count, '.6f')

    print(pos)
    print(neg)
    print(zero)


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
