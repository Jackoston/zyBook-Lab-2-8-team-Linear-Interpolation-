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


# change points into list
def getpoints(nums):
    list1 = nums.split()
    listxy = []
    for pair in list1:
        point = pair.split(',')
        point[0] = int(point[0])
        point[1] = int(point[1])
        listxy.append(point)
    return listxy


# finding cross product
def cross(point1, point2):
    pos = point1[0] * point2[1]
    neg = point1[1] * point2[0]
    cross_product = pos - neg
    return cross_product


# adding up the area
def shoelace(list_of_points):
    area = 0
    for i in range(len(list_of_points) - 1):
        area += cross(list_of_points[i], list_of_points[i + 1])
    area += cross(list_of_points[-1], list_of_points[0])
    return area / 2


# main code function
def main():
    point_int = input('Please enter the vertices: ')

    list_of_values = getpoints(point_int)
    final_area = shoelace(list_of_values)
    print(f'The area of the polygon is {final_area:.1f}')


# zybook check thing
if __name__ == '__main__':
    main()
