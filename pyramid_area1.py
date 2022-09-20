# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: Christopher
# Austin
# Eddy
# Reed
# Section: 568
# Assignment: 6-13 Making Change
# Date: 15 September 2022

from math import sqrt
sideL=int(input("Enter the side length in meters:"))
layers=int(input("Enter the number of layers:"))

areatotal=1
areaPrevious=0
areaTops=sqrt(3)/4*sideL
for i in range(layers+1):
    areatotal+=(sideL*layers)*sideL