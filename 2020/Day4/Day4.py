import os
import ast
import re

def readInput(pathToInput):
    fn = os.path.join(os.path.dirname(__file__), pathToInput)
    inputFile = open(fn)
    return inputFile.read()

def checkPassport(passportString, terms):
    isValid = True
    for term in terms:
        isValid = isValid and (term in passportString)
    return isValid

def checkYear(year, low, high):
    return (low <= year) and (year <= high)

def checkHeight(height):
    if height[-2:] == "cm":
        heightVal = int(height[:-2])
        return (heightVal >= 150) and (heightVal <= 193)
    elif height[-2:] == "in":
        heightVal = int(height[:-2])
        return (heightVal >= 59) and (heightVal <= 76)
    else:
        return False

def checkHair(hair):
    regex = re.compile(r"#[\da-f]{6}\b")
    return regex.match(hair)

def checkEyes(eyes):
    return eyes in ["amb","blu","brn","gry","grn","hzl","oth"]

def checkPid(pid):
    regex = re.compile(r"\d{9}\b")
    if len(pid) > 9:
        print("idajoiajsfaoijiajfsaiaojiadjiosjdaoidjioajdsaoijfioajfioajfiasjfiajsidjaiodjaoisjd")
    return regex.match(pid)

def reallyCheckPassport(passportString):
    passportString = "{\'" + passportString.replace(":","\':\'").replace(" ", "\',\'").replace("\n","\',\'") + "\'}"
    details = ast.literal_eval(passportString)

    return (checkYear(int(details["byr"]), 1920, 2002) and checkYear(int(details["iyr"]), 2010, 2020) and checkYear(int(details["eyr"]), 2020, 2030) and
    checkHeight(details["hgt"]) and checkHair(details["hcl"]) and checkEyes(details["ecl"]) and checkPid(details["pid"]))


requiredFields = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
inputs = readInput('Input/input').split("\n\n")
total = 0
totalValid = 0
totalReallyValid = 0

for pp in inputs:
    total += 1
    if checkPassport(pp, requiredFields):
        totalValid += 1
        if reallyCheckPassport(pp):
            totalReallyValid += 1
            print (totalReallyValid)
            print(pp)
            print ('*******************VALID**************************')

print(total)
print(totalValid)
print(totalReallyValid)