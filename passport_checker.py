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
passports = passportFile.read().split('\r\n\r')
passportFile.close()

# File Writer:
validCount = 0
with open('valid_passports.txt', 'w') as validPassports:
    for i in range(len(passports)):
        try:
            passports[i].index('hcl')
            if len(passports[i].split()) == 8:
                validPassports.write(f'{passports[i]}')
                validCount += 1
        except ValueError:
            if len(passports[i].split()) == 7:
                validPassports.write(f'{passports[i]}')
                validCount += 1

# Print:
print(f'There are {validCount} valid passports')
