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

allFile = open('scanned_passports.txt', 'r', newline='')
passports = allFile.read().split('\r\n\r')

allFile.close()

eyeColorDict={ "amb":1, "blu":1, "brn":1, "gry":1, "grn":1, "hzl":1, "oth":1}
value_person = []

hclCount = 0
for person in passports:
    temp = person.split()
    value_person.append(temp)

for g in range(len(value_person)):
    value_person[g].sort()

for index in value_person:

# tier1, passport ID
tier1 = []
for i in value_person:
    if i[-1][:3] == 'pid' and i[-1][4] == '0' and len(i[-1]) == 13:
        tier1.append(i)
for t in range(len(tier1)):
    print(tier1[t])


# tier2, eye color
print("goo:slimbim"["goo:slimbim".index(":")+1:])

eyr="amb"
pid="791118269"
hgt="hgt:183cm"
hgtbool=
eyr="2022"
if len(pid)==9 and pid.index("0")!=0:
    try:
        if eyeColorDict.get(eyr)==1:
            if hgt[-2:-1]=="in"or hgt[-2:-1]=="cm":
                try:
                    hieghtNum=int(hgt[0:hgt.index("cm")])
                except:
                    hieghtNum=int(hgt[0:hgt.index("in")])
                if int(eyr)>=2022 and int(eyr)<=2032:
                    print("cows go moo")
    except:
        print("you stupid :P")

#wbigwbibgwigwibgwibogew