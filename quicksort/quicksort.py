#!/usr/bin/env python3
# quicksort.py

def quicksort(inputArray, lowIndex=0, highIndex=None):
    if highIndex == None:
        highIndex = len(inputArray) - 1
    if lowIndex < highIndex:
        partitionIndex = partition(inputArray, lowIndex, highIndex)
        quicksort(inputArray, lowIndex, partitionIndex - 1)
        quicksort(inputArray, partitionIndex + 1, highIndex)

def partition(partArray, low, high):
    pivot = partArray[high]

    smallIndex = low - 1

    for index in range(low, high):
        if partArray[index] <= pivot:
            smallIndex += 1
            partArray[smallIndex], partArray[index] = partArray[index], partArray[smallIndex]

    partArray[smallIndex + 1], partArray[high] = partArray[high], partArray[smallIndex + 1]
    return smallIndex + 1

if __name__ == '__main__':
    sourceData = 'data.txt'
    dataArray = []
    with open(sourceData, 'r') as file:
        for line in file:
            dataArray.extend(map(int, line.rstrip().split()))
    quicksort(dataArray)
    print(dataArray)

