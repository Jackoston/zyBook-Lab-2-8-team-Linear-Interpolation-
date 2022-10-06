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
first = int("".join(numList))
print(first, end=' > ')
if len(numList) != 4:
    while len(numList) != 4:
        numList.append('0')
ending = 6174
end_Number = 0
iter = 0

while end_Number != 6174:
    if len(numList) != 4:
        while len(numList) != 4:
            numList.append('0')
    iter += 1
    numList.sort()

    asscending = "".join(numList)

    numList.reverse()

    deccending = ''.join(numList)

    end_Number = int(deccending) - int(asscending)
    if asscending == deccending:
        print('0')
        ending = 0
        end_Number = 6174
    elif end_Number != 6174:
        print(end_Number, end=' > ')
    else:
        print(end_Number)
    numList = list(str(end_Number))
print(f"{first} reaches {ending} via Kaprekar's routine in {iter} iterations")
