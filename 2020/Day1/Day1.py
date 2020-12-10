import os

def readInput(pathToInput):
    fn = os.path.join(os.path.dirname(__file__), pathToInput)
    inputFile = open(fn)
    return inputFile.readlines()

def findMatch(arrayOfInt):
    for x in arrayOfInt:
        for y in arrayOfInt:
            if x+y == 2020:
                return x*y
    return 0

def findThreeMatch(arrayOfInt):
    for x in arrayOfInt:
        for y in arrayOfInt:
            for z in arrayOfInt:
                if x+y+z == 2020:
                    return x*y*z
    return 0

inputArray = list(map(int, readInput('Input/input')))
print(findMatch(inputArray))
print(findThreeMatch(inputArray))