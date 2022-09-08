# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: Christopher
# Austin
# Eddy
# Reed
# Section: 568
# Assignment: 3-16 Still More Linear Interpolation
# Date: 8 September 2022
from math import sqrt

time1 = input("Enter time 1:")
pos_x1 = input("Enter the x position of the object at time 1:")
pos_y1 = input("Enter the y position of the object at time 1:")
pos_z1 = input("Enter the z position of the object at time 1:")

time2 = input("Enter time 2:")
pos_x2 = input("Enter the x position of the object at time 2:")
pos_y2 = input("Enter the y position of the object at time 2:")
pos_z2 = input("Enter the z position of the object at time 2:")

time_interval = (time2 - time1) / 4
time_distance_1 = time1 + time_interval
time_distance_2 = time_distance_1 + time_interval
time_distance_3 = time_distance_2 + time_interval

CHANGE_IN_TIME = 0
CHANGE_IN_X = 0
CHANGE_IN_Y = 0
CHANGE_IN_Z = 0

