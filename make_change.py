# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: Christopher
# Austin
# Eddy
# Reed
# Section: 568
# Assignment: 4-13 Making Change
# Date: 15 September 2022




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
change = paid - price
print(f'You received ${change:.2f} in change. That is...')

penny = 0
nickel = 0
dime = 0
quarter = 0
dollar = 0

dollar = change//1
change = change - dollar * 1


quarter = change//.25
change = change-quarter*.25

dime = change//.10
change = change-quarter*.10

nickel = change//.05
change = change-nickel*.05

penny = change//.01
change = change-penny*.01


if dollar != 0:
    if dollar > 1:
        print(dollar, "dollars")
    else:
        print(dollar,"dollar")
if quarter != 0:
    print(quarter,"quarter")
if dime != 0:
    print()
if nickel != 0:
    print()
if penny != 0:
    print()