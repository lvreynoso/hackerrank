#!/bin/python3

# wat? bitmasking?

def eulerSum(inputSet, setLength, subsetSize):
    setA = inputSet
    result = 0
    return result

if __name__ == '__main__':
    params = list(map(int, input().rstrip().split()))
    problem = list(map(int, input().rstrip().split()))
    result = eulerSum(problem, params[0], params[1])
    print(result)