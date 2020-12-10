import os

def readInput(pathToInput):
    fn = os.path.join(os.path.dirname(__file__), pathToInput)
    inputFile = open(fn)
    return inputFile.readlines()

def checkPassword(password, neededLetter, lowFreq, highFreq):
    return (lowFreq <= password.count(neededLetter)) & (password.count(neededLetter) <= highFreq)

def reallyCheckPassword(password, neededLetter, lowPos, highPos):
    return (password[lowPos-1] == neededLetter) != (password[highPos-1] == neededLetter)

inputArray = readInput('Input/input')
totalCorrect = 0
totalReallyCorrect = 0

for string in inputArray:
    inputs = string.split(" ")
    lowVal = int(inputs[0].split("-")[0])
    highVal = int(inputs[0].split("-")[1])
    letter = inputs[1][0]
    password = inputs[2]

    if checkPassword(password, letter, lowVal, highVal):
        totalCorrect = totalCorrect + 1

    if reallyCheckPassword(password, letter, lowVal, highVal):
        totalReallyCorrect = totalReallyCorrect + 1


print(totalCorrect)
print(totalReallyCorrect)

