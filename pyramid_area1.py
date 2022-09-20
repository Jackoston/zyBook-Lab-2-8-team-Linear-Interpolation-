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
sideL=float(input("Enter the side length in meters:"))
layers=int(input("Enter the number of layers:"))

areatotal=1
areaPrevious=0
areaTops=sqrt(3)/4*sideL
i=layers
for i in range(1,layers+1):
    areatotal+=3*((sideL*layers)*sideL)
    layers+1
print(areatotal)