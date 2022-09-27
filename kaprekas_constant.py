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
numList = list(input('Enter a four-digit integer: '))
end_Number = 0
iter = 0
first = int("".join(numList))
print(first, end=' > ')
while end_Number != 6174:

    iter += 1
    numList.sort()

    asscending = "".join(numList)

    numList.reverse()

    deccending = ''.join(numList)

    end_Number = int(deccending) - int(asscending)
    if end_Number != 6174:
        print(end_Number, end=' > ')
    else:
        print(end_Number)
    numList = list(str(end_Number))
print(f"{first} reaches 6174 via Kaprekar's routine in {iter} iternations")
