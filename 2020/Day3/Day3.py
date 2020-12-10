import os

def readInput(pathToInput):
    fn = os.path.join(os.path.dirname(__file__), pathToInput)
    inputFile = open(fn)
    return inputFile.readlines()

def countSlopeTree(terrain, downInc, rightInc):
    x = 0
    y = 0

    total = 0

    while y < len(terrain):
        if terrain[y][x] == "#":
            total = total + 1
        x = (x + rightInc) % 31
        y = y + downInc

    return total


inputArray = readInput('Input/input')

print (countSlopeTree(inputArray, 1, 3))

slope1 = countSlopeTree(inputArray, 1, 1)
slope2 = countSlopeTree(inputArray, 1, 3)
slope3 = countSlopeTree(inputArray, 1, 5)
slope4 = countSlopeTree(inputArray, 1, 7)
slope5 = countSlopeTree(inputArray, 2, 1)

print(slope1*slope2*slope3*slope4*slope5)