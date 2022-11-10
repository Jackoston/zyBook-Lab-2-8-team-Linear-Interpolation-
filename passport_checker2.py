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


print("goo:slimbim"["goo:slimbim".index(":")+1:])

eyeColorDict={ "amb":1, "blu":1, "brn":1, "gry":1, "grn":1, "hzl":1, "oth":1}
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

