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

time1 = float(input("Enter time 1:"))
print()
pos_x1 = float(input("Enter the x position of the object at time 1:"))
print()
pos_y1 = float(input("Enter the y position of the object at time 1:"))
print()
pos_z1 = float(input("Enter the z position of the object at time 1:"))
print()

time2 = float(input("Enter time 2:"))
print()
pos_x2 = float(input("Enter the x position of the object at time 2:"))
print()
pos_y2 = float(input("Enter the y position of the object at time 2:"))
print()
pos_z2 = float(input("Enter the z position of the object at time 2:"))
print()

time_interval = (time2 - time1) / 4
time_distance_1 = time1 + time_interval
time_distance_2 = time_distance_1 + time_interval
time_distance_3 = time_distance_2 + time_interval

CHANGE_IN_X = 0
CHANGE_IN_Y = 0
CHANGE_IN_Z = 0

#new_x2 = x2 + (t2 - t2) * ((x2 - x1) / (t2 - t1))

print(f"At time {time1:.2f} seconds the object is at ("")")
print(f"At time {time_distance_1:.2f} seconds the object is at ("")")
print(f"At time {time_distance_2:.2f}seconds the object is at ("")")
print(f"At time {time_distance_3:.2f}seconds the object is at ("")")
print(f"At time {time2:.2f}seconds the object is at ("")")