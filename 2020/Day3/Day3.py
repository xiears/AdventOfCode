import os

def readInput(pathToInput):
    fn = os.path.join(os.path.dirname(__file__), pathToInput)
    inputFile = open(fn)
    return inputFile.readlines()

def countSlopeTree(terrain):
    x = 0
    total = 0
    for line in terrain:
        if line[x] == "#":
            total = total + 1
        x = (x + 3) % 31

    return total


inputArray = readInput('Input/input')

print (countSlopeTree(inputArray))