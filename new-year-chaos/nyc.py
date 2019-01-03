#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    numberOfBribes = 0
    chaotic = False
    sortExhausted = False
    bribeMap = {}

    while not sortExhausted:
        sortExhausted = True
        for index in range(len(q)):
            head = -index - 1
            value = q[head]
            displacement = value - (head + 1)
            limitReached = False
            # print(q)
            if value in bribeMap:
                # print('Bribe #: {}'.format(bribeMap[value]))
                if bribeMap[value] > 1:
                    limitReached = True
            if displacement > 0 and not limitReached and head < -1 and (q[head] > q[head + 1]):
                # print('Swapping {}, {}'.format(q[head], q[head + 1]))
                q[head], q[head + 1] = q[head + 1], q[head]
                numberOfBribes += 1
                sortExhausted = False
                if value not in bribeMap:
                    bribeMap[value] = 1
                else:
                    bribeMap[value] += 1

    # now check for chaos
    for index in range(len(q)):
        if q[index] != index + 1:
            chaotic = True

    # print('{}'.format(q))

    if not chaotic:
        print('{}'.format(numberOfBribes))
    else:
        print('Too chaotic')

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
