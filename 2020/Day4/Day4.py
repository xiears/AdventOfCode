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
        isValid = isValid & (term in passportString)
    return isValid

def checkYear(year, low, high):
    return (low <= year) & (year <= high)

def checkHeight(height):
    if height[-2:] == "cm":
        heightVal = int(height[:-2])
        return (heightVal >= 150) & (heightVal <= 193)
    elif height[-2:] == "in":
        heightVal = int(height[:-2])
        return (heightVal >= 59) & (heightVal <= 76)
    else:
        return False

def checkHair(hair):
    return re.match("#\\d{6}", hair)

def checkEyes(eyes):
    return eyes in ["amb","blu","brn","gry","grn","hzl","oth"]

def checkPid(pid):
    return re.match("\\d{9}", pid)

def reallyCheckPassport(passportString):
    passportString = "{\'" + passportString.replace(":","\':\'").replace(" ", "\',\'").replace("\n","\',\'") + "\'}"
    details = ast.literal_eval(passportString)

    return (checkYear(details["byr"], 1920, 2002) & checkYear(details["iyr"], 2010, 2020) & checkYear(details["eyr"], 2020, 2030) &
    checkHeight(details["hgt"]) & checkHair(details["hcl"]) & checkEyes(details["ecl"]) & checkPid(details["pid"]))


requiredFields = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
inputs = readInput('Input/allValid').split("\n\n")
totalValid = 0
totalReallyValid = 0

for pp in inputs:
    if checkPassport(pp, requiredFields):
        totalValid += 1
    if reallyCheckPassport(pp):
        totalReallyValid += 1
    
print(totalValid)