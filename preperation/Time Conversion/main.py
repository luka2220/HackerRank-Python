import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s: str) -> str:
    # Write your code here
    tod = s[-2:]
    hour = s[:2]

    if hour == '12' and tod == 'PM':
        return s[:len(s)-2]
    if hour == '12' and tod == 'AM':
        return '00' + s[2:len(s)-2]

    if tod == 'PM':
        hour = str(int(hour) + 12)
        return str(hour) + s[2:len(s)-2]
    
    return s[:len(s)-2]


if __name__ == '__main__':
    s = input()

    result = timeConversion(s)
    print(result)
