#!/bin/python3

import itertools
            

def eulerSum(inputSet, setLength, subsetSize):
    setA = inputSet
    iterator = itertools.combinations(inputSet, subsetSize)
    sums = {}
    for entry in iterator:
        value = sum(entry)
        if value in sums:
            sums[value] += 1
        else:
            sums[value] = 1

    uniqueSums = [n[0] for n in sums.items() if n[1] == 1]
    result = sum(uniqueSums)
    return result

if __name__ == '__main__':
    params = list(map(int, input().rstrip().split()))
    problem = list(map(int, input().rstrip().split()))
    result = eulerSum(problem, params[0], params[1])
    print(result)