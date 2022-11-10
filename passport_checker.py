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

userInput = input('Enter the name of the file: ')
datFile = open('scanned_passports.txt', 'r', newline='')
passports = datFile.read().split('\r\n\r')

datFile.close()



validList1=[]
hclCount=0
for i in range(len(passports)):
    passports[i]
    try:
        passports[i].index("hcl")  #if hair exist
        if len(passports[i].split())==8:
            validList1.append(passports[i].split())
            hclCount+=1
    except ValueError:
        if len(passports[i].split())==7:
            validList1.append(passports[i].split())

total_val_pass = open('valid_passports.txt', 'w')
validList1.sort() #24 and 47 dont have hcl
tot_val = 0
for g in range(len(validList1)):
    validList1[g].sort()
for y in range(len(validList1)):
    try:
        validList1[y][4].index("hcl")
        total_val_pass.write(f'{str(validList1[y])}\n')
        tot_val += 1
    except ValueError:
        if "hgt" in validList1[y][4]:
            total_val_pass.write(f'{str(validList1[y])}\n')
            tot_val +=1
        else:
            continue

print(f'There are {tot_val} valid passports')
