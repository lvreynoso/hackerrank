#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the matrixRotation function below.
def matrixRotation(matrix, r):
    # pretty printing
    print('\nInput Matrix:\n')
    for row in matrix:
        outputString = ''
        for number in row:
            outputString += str(number) + ' '
        print(outputString + '\n')


    rows = len(matrix)
    columns = len(matrix[0])

    orbits = []

    numberOfRings = math.floor(min(rows, columns) / 2)

    for ringNumber in range(1, numberOfRings + 1):
        orbit = []
        leftColumn = [] # these are last
        firstRowIndex = 0 + (ringNumber - 1)
        lastRowIndex = (rows - 1) - (ringNumber - 1)
        leftColumnIndex = 0 + (ringNumber - 1)
        rightColumnIndex = (columns - 1) - (ringNumber - 1)
        for row in range(firstRowIndex, lastRowIndex + 1):
            # if it's the first row, add that row to the orbit, minus the ring level
            if row == firstRowIndex:
                orbit.extend(matrix[row][leftColumnIndex:rightColumnIndex + 1])
            # if it's the last row, add that row (reversed) to the orbit, minus the ring level
            elif row == lastRowIndex:
                values = matrix[row][leftColumnIndex:rightColumnIndex + 1]
                values.reverse()
                orbit.extend(values)
            else:
                leftColumn.append(matrix[row][leftColumnIndex])
                orbit.append(matrix[row][rightColumnIndex])
        leftColumn.reverse()
        orbit.extend(leftColumn)
        orbits.append(orbit)

    for orbit in orbits:
        shiftedValues = orbit[0:r]
        del orbit[0:r]
        orbit.extend(shiftedValues)

    outputMatrix = []
    for row in range(rows):
        row = []
        for column in range(columns):
            row.append(0)
        outputMatrix.append(row)

    for ringNumber in range(1, numberOfRings + 1):
        firstRowIndex = 0 + (ringNumber - 1)
        lastRowIndex = (rows - 1) - (ringNumber - 1)
        leftColumnIndex = 0 + (ringNumber - 1)
        rightColumnIndex = (columns - 1) - (ringNumber - 1)
        for row in range(firstRowIndex, lastRowIndex + 1):
            if row == firstRowIndex:
                for column in range(leftColumnIndex, rightColumnIndex + 1):
                    outputMatrix[row][column] = orbits[ringNumber - 1].pop(0)
            elif row == lastRowIndex:
                for column in range(leftColumnIndex, rightColumnIndex + 1):
                    outputMatrix[row][column] = orbits[ringNumber - 1].pop()
            else:
                outputMatrix[row][rightColumnIndex] = orbits[ringNumber - 1].pop(0)
                outputMatrix[row][leftColumnIndex] = orbits[ringNumber - 1].pop()

    print('\n\nOutput Matrix:\n')
    for row in outputMatrix:
        outputString = ''
        for number in row:
            outputString += str(number) + ' '
        print(outputString + '\n')






if __name__ == '__main__':
    mnr = input().rstrip().split()

    m = int(mnr[0])

    n = int(mnr[1])

    r = int(mnr[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r)
