#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the saveThePrisoner function below.
def saveThePrisoner(n, m, s):
    chair = (m + s - 1) % n
    return chair if chair != 0 else n

if __name__ == '__main__':
    fptr = open('output.txt', 'w')

    t = int(input())

    for t_itr in range(t):
        nms = input().split()

        n = int(nms[0])

        m = int(nms[1])

        s = int(nms[2])

        result = saveThePrisoner(n, m, s)
        print(result)
        fptr.write(str(result) + '\n')

    fptr.close()
