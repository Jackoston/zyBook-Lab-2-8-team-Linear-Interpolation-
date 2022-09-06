
# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: Christopher
# Austin
# Eddy
# Reed
# Section: 568
# Assignment: 2-8
# Date: 30 August 2022

first_time_ISS = 10
second_time_ISS = 55
first_distance_ISS = 2026
second_distance_ISS = 23026
time_ISS_want = 25
# y = y_initial + (x - x_initial) * y_final - y_initial / x_final - x_initial

distance_ISS_want = first_distance_ISS + (time_ISS_want - first_time_ISS) * (second_distance_ISS - first_distance_ISS) / (second_time_ISS - first_time_ISS)

print('Part 1:')
print(F'For t = 25 minutes, the position p =', distance_ISS_want, 'kilometers')

from math import pi

print('Part 2:')
time_ISS_want = 300
radius_ISS_earth = 6745
circumference_ISS_earth = radius_ISS_earth * 2 * pi
distance_total_ISS = first_distance_ISS + (time_ISS_want - first_time_ISS) * (second_distance_ISS - first_distance_ISS) / (second_time_ISS - first_time_ISS)
distance_away_houston = distance_total_ISS % circumference_ISS_earth

print('For t = 300 minutes, the position p =', distance_away_houston, 'kilometers')
