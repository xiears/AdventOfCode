import os

def readInput(pathToInput):
    fn = os.path.join(os.path.dirname(__file__), pathToInput)
    inputFile = open(fn)
    return inputFile.read()

def calcSeatNo(seatString):
    row = int(seatString[:7].replace("F","0").replace("B","1"), 2)
    col = int(seatString[7:].replace("L","0").replace("R","1"), 2)

    return (row * 8) + col

inputs = readInput('Input/input').split("\n")
highest = 0
lowest = 10000
total = 0

for seat in inputs:
    currNo = calcSeatNo(seat)
    total += currNo
    if highest < currNo:
        highest = currNo
    if lowest > currNo:
        lowest = currNo

print (total)

for val in [*range(lowest,highest+1,1)]:
    total -= val

for val in [*range(lowest,highest+1,1)]:
    print(val)

print(lowest)
print(highest)
print(abs(total))
