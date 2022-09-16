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


# inputs
paid = float(input('How much did you pay?'))
price = float(input('How much did it cost?'))
change = paid - price
print(f'You received ${change:.2f} in change. That is...')
change*=100
change= round(change,0)

# quarters and number
quarter = change//25
change = change-quarter*25

# dime and number
dime = change//10
change = change-dime*10

# nickel and number
nickel = change//5
change = change-nickel*5

# penny and number
penny = change//1
change = change-penny*1


# choosing single or plurual
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