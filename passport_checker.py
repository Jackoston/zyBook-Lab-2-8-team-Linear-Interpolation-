# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Austin
#               Christopher
#               Reed
#               Eddy
# Section:      468
# Assignment:   10 - 13 Debugged Code
# Date:         Nov. 8th, 2022

# User Input:
userInput = input('Enter the name of the file: ')
passportFile = open(userInput, 'r', newline='')
passport = passportFile.read().split('\r\n\r')
passportFile.close()

# File Writer:
validCount = 0
with open('valid_passports.txt', 'w', newline='') as validPassports:
    for i in range(len(passport)):
        try:
            passport[i].index('hcl')
            if len(passport[i].split()) == 8:
                validPassports.write(f'{passport[i]}\n')
                validCount += 1
        except ValueError:
            if len(passport[i].split()) == 7:
                validPassports.write(f'{passport[i]}\n')
                validCount += 1

# Print:
print(f'There are {validCount} valid passports')
