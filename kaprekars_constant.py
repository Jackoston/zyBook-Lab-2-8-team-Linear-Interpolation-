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
iter = 0
for i in range (0,10000):
    numList = list(str(i))
    first = int("".join(numList))
    if len(numList) != 4:
        while len(numList) != 4:
            numList.append('0')
    ending = 6174
    end_Number = 0


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
            ending = 0
            end_Number = 6174

        numList = list(str(end_Number))
print(f"Kaprekar's routine takes {iter} total iterations for all four-digit numbers")