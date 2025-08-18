#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import permutations

#
# Complete the 'twoArrays' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#  3. INTEGER_ARRAY B
#


def birthday(s, d, m):
    res = 0

    permutations = (s[j:j + m] for j in range(0, len(s) - (m - 1)))

    for combinations in list(permutations):
        if sum(combinations) == d:
            res += 1

    return res


if __name__ == '__main__':
    s = [2, 2, 1, 3, 2]
    d = 4
    m = 2

    res = birthday(s, d, m)
    print(res)