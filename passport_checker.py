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

datFile = open('scanned_passports.txt', 'r', newline='')
passports = datFile.read().split('\r\n\r')

datFile.close()

print("wow\n\r\nwow")
print(passports)
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

print(len(validList1))
print(hclCount)
validList1.sort() #24 and 47 dont have hcl
for g in range(len(validList1)):
    validList1[g].sort()
for y in range(len(validList1)):
    try:
        validList1[y][4].index("hcl")
    except ValueError:
        print(validList1[y])
        print(y)

