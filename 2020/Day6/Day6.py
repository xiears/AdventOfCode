import os

def readInput(pathToInput):
    fn = os.path.join(os.path.dirname(__file__), pathToInput)
    inputFile = open(fn)
    return inputFile.read()

def calculateTotalQs(answerString):
    return len(set("".join(answerString.split())))

def calculateAllYesQs(answerString):
    lines = answerString.split("\n")
    index = 1
    check = True
    total = 0

    for char in lines[0]:
        index = 1
        check = True
        while index < len(lines):
            check &= char in lines[index]
            index += 1
        if check:
            total += 1

    return total
    
inputs = readInput('Input/input').split("\n\n")
total = 0
allTotal = 0

for i in inputs:
    print(i)
    qs = calculateTotalQs(i)
    print(qs)
    total += qs
    qs = calculateAllYesQs(i)
    print(qs)
    allTotal += qs

print(total)
print(allTotal)