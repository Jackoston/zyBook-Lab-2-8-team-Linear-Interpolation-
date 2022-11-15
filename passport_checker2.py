# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Austin
#               Christopher
#               Reed
#               Eddy
# Section:      468
# Assignment:   10 - 13 Debugged Code
# Date:         Nov. 1st, 2022
file = input('Enter the name of the file: ')
allFile = open(f'{file}', 'r', newline='')
passports = allFile.read().split('\r\n\r')

allFile.close()

value_person = []
valid_passports = []
hclCount = 0
for person in passports:
    temp = person.split()
    value_person.append(temp)

for g in range(len(value_person)):
    value_person[g].sort()

ecl_list = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
# loop for every passport and every single thing in the passport
for thing in value_person:
    num_valid = 0
    for single in thing:
        try:
            # check1: if birth year is valid
            if single[:3] == 'byr' and 1920 <= int(single[4:]) <= 2005:
                num_valid += 1
        except ValueError:
            pass
        try:
            # check2: if issue year is valid
            if single[:3] == 'iyr' and 2012 <= int(single[4:]) <= 2022:
                num_valid += 1
        except ValueError:
            pass
        try:
            # check3: if expiration year is valid
            if single[:3] == 'eyr' and 2022 <= int(single[4:]) <= 2032:
                num_valid += 1
        except ValueError:
            pass
        try:
            # check4: if height is valid (cm)
            if single[:3] == 'hgt' and single[-1] == 'm' and 150 <= int(single[4:-2]) <= 193:
                num_valid += 1
        except ValueError:
            pass
        try:
            # check4: if height is valid (in)
            if single[:3] == 'hgt' and single[-1] == 'n' and 59 <= int(single[4:-2]) <= 76:
                num_valid += 1
        except ValueError:
            pass
        try:
            # check5: if eye color is valid
            if single[:3] == 'ecl' and single[4:] in ecl_list:
                num_valid += 1
        except ValueError:
            pass
        try:
            # check6: if passport ID is valid
            if single[:3] == 'pid' and len(single[4:]) == 9 and int(single[4:]):
                num_valid += 1
        except ValueError:
            pass
        try:
            # check7: if country ID is valid
            if single[:3] == 'cid' and 99 < int(single[4:]) < 1000:
                num_valid += 1
        except ValueError:
            pass
        if num_valid == 7:
            valid_passports.append(thing)


print(f'There are {len(valid_passports)} valid passports')
writing_passports = []

# put string of passport in a list writing_passports
# check for valid PID in the string
for passport in passports:
    for thing in valid_passports:
        if thing[-1] in passport:
            writing_passports.append(passport)

writing_passports[0] = writing_passports[0].lstrip()

# write string of passport into file with a \n
validFile = open('valid_passports2.txt', 'w', newline='')
for passport in writing_passports:
    validFile.write(f'{passport}\n')
