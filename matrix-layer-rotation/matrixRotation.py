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

    rings = []

    numberOfRings = math.floor(min(rows, columns) / 2)

    # this time we do a mapping

    # first sort the matrix locations a[i][j] into "orbits", so to speak
    # starting with the outside "ring" of the matrix, and going inward
    # top left is first position in the ring
    for ringNumber in range(1, numberOfRings + 1):
        ring = []
        leftColumn = [] # these are last
        firstRowIndex = 0 + (ringNumber - 1)
        lastRowIndex = (rows - 1) - (ringNumber - 1)
        leftColumnIndex = 0 + (ringNumber - 1)
        rightColumnIndex = (columns - 1) - (ringNumber - 1)
        for row in range(firstRowIndex, lastRowIndex + 1):
            # if it's the first row, add that row to the ring, minus the ring level
            if row == firstRowIndex:
                for column in range(columns):
                    if column >= leftColumnIndex and column <= rightColumnIndex:
                       ring.append([row, column])
            # if it's the last row, add that row (reversed) to the ring, minus the ring level
            elif row == lastRowIndex:
                lastRow = []
                for column in range(columns):
                    if column >= leftColumnIndex and column <= rightColumnIndex:
                        lastRow.append([row, column])
                lastRow.reverse()
                ring.extend(lastRow)
            else:
                leftColumn.append([row, leftColumnIndex])
                ring.append([row, rightColumnIndex])
        leftColumn.reverse()
        ring.extend(leftColumn)
        rings.append(ring)

    # now for each list of coordinates, we add a second pair that corresponds to the point
    # in the matrix that is r rotations down the line

    for ring in rings:
        for index in range(len(ring)):
            mappingPoint = (index - r) % (len(ring))
            ring[index].extend(ring[mappingPoint])

    # create an empty output matrix of the same size
    outputMatrix = []
    for row in range(rows):
        row = []
        for column in range(columns):
            row.append(0)
        outputMatrix.append(row)

    # now we just read our rings as a neat little mapping to where
    # the original points go in the final matrix
    for ring in rings:
        for entry in ring:
            # map original a[i][j] to new m[x][y]
            # variable assignments for readability
            i = entry[0]
            j = entry[1]
            x = entry[2]
            y = entry[3]
            outputMatrix[x][y] = matrix[i][j]

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
