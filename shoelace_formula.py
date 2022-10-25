# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: Austin
# Christopher
# Reed
# Eddy
# Section: 468
# Assignment: Lab 9 - 15: Shoelace formula
# Date: 25 October 2022


def getpoints(nums):
    list1 = nums.split()
    listxy = []
    for pair in list1:
        point = pair.split(',')
        point[0] = int(point[0])
        point[1] = int(point[1])
        listxy.append(point)
    return listxy





# main code
point_int = input('Please enter the vertices: ')


print(getpoints(point_int))