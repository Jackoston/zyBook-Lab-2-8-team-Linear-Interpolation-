# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: Christopher
# Austin
# Eddy
# Reed
# Section: 568
# Assignment: 4.3
# Date: 13 September 2022

paid = float(input('How much did you pay?'))
price = float(input('How much did it cost?'))
change = price-paid

penny = 0
nickel = 0
dime = 0
quarter = 0


quarter = change//.25
change = change-quarter*.25

dime = change//.10
change = change-quarter*.10

nickel = change//.05
change = change-nickel*.05

penny = change//.01
change = change-penny*.01



if quarter != 0:
    if quarter > 1:
        print(quarter, "quarters")
    else:
        print(quarter,"quarter")
if dime != 0:
    if dime > 1:
        print(dime, "dimes")
    else:
        print(dime, "dime")
if nickel != 0:
    if nickel > 1:
        print(nickel, "nickels")
    else:
        print(nickel, "nickel")
if penny != 0:
    if nickel > 1:
        print(penny, "pennys")
    else:
        print(penny, "penny")