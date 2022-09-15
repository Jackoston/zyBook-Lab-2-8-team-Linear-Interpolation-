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
change*=100
change= round(change,0)


penny = 0
nickel = 0
dime = 0
quarter = 0


quarter = change//25
change = change-quarter*25


dime = change//10
change = change-dime*10


nickel = change//5
change = change-nickel*5

penny = change//1
change = change-penny*1



if quarter != 0:
    if quarter > 1:
        print(int(quarter), "quarters")
    else:
        print(int(quarter),"quarter")
if dime != 0:
    if dime > 1:
        print(int(dime), "dimes")
    else:
        print(int(dime), "dime")
if nickel != 0:
    if nickel > 1:
        print(int(nickel), "nickels")
    else:
        print(int(nickel), "nickel")
if penny != 0:
    if penny > 1:
        print(int(penny), "pennies")
    else:
        print(int(penny), "penny")