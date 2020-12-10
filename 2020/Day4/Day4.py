import os

def readInput(pathToInput):
    fn = os.path.join(os.path.dirname(__file__), pathToInput)
    inputFile = open(fn)
    return inputFile.read()

def checkPassport(passportString, terms):
    isValid = True
    for term in terms:
        isValid = isValid & (term in passportString)
    return isValid


requiredFields = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
inputs = readInput('Input/input').split("\n\n")
totalValid = 0

for pp in inputs:
    if checkPassport(pp, requiredFields):
        totalValid = totalValid + 1
    
print(totalValid)