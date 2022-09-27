# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: Austin
# Christopher
# Reed
# Eddy
# Section: 468
# Assignment: Lab 7 - 28: Kprekars constant
# Date: 27 September 2022

# input
cars = list(input('Enter a four-digit integer: '))
end_Number=0
iter=0
while end_Number != 6174:

    iter+=1
    cars.sort()

    asscending = "".join(cars)

    print(cars)

    cars.reverse()

    dessending = ''.join(cars)

    print(cars)

    end_Number = int(dessending) - int(asscending)
    print(end_Number)
    cars=list(str(end_Number))
