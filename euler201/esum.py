#!/bin/python3

import itertools
            

def eulerSum(inputSet, setLength, subsetSize):
    setA = inputSet
    permutations = tuple(itertools.combinations(inputSet, subsetSize))
    counts = {}
    for entry in permutations:
        thisSum = sum(entry)
        if thisSum not in counts:
            counts[thisSum] = 1
        else:
            counts[thisSum] += 1

    uniqueSums = [n[0] for n in counts.items() if n[1] == 1]
    result = sum(uniqueSums)
    return result

if __name__ == '__main__':
    params = list(map(int, input().rstrip().split()))
    problem = list(map(int, input().rstrip().split()))
    result = eulerSum(problem, params[0], params[1])
    print(result)