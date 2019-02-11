#!/bin/python3

import math
import os
import random
import re
import sys

def subSum(targetSet, summa, subIndex, count, targetMap):
    partial = targetSet[subIndex]
    if count == 1:
        result = partial + summa
        if result not in targetMap:
            targetMap[result] = 1
        else:
            targetMap[result] += 1
    else:
        for nextIndex in range(subIndex + 1, len(targetSet)):
            subSum(targetSet, partial + summa, nextIndex, count - 1, targetMap)
            

def eulerSum(inputSet, setLength, subsetSize):
    setA = inputSet
    sums = {}

    for index in range(setLength - subsetSize + 1):
        subSum(setA, 0, index, subsetSize, sums)

    uniqueSums = [n[0] for n in sums.items() if n[1] == 1]
    result = sum(uniqueSums)
    return result

if __name__ == '__main__':
    params = list(map(int, input().rstrip().split()))
    problem = list(map(int, input().rstrip().split()))
    result = eulerSum(problem, params[0], params[1])
    print(result)