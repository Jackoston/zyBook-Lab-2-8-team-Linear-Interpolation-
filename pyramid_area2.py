# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: Christopher
# Austin
# Eddy
# Reed
# Section: 568
# Assignment: 6-12 Pyramid Area 2
# Date: 22 September 2022
from math import sqrt
# inputs
sideL = float(input("Enter the side length in meters: \n"))
layers = int(input("Enter the number of layers: \n"))

# area top
area_top = (sqrt(3) / 4) * (layers * sideL) ** 2

# area side
# series equation and terms
an = layers * 3 * (sideL ** 2)
a1 = 3 * (sideL ** 2)
area_side = layers * ((a1 + an) / 2)

# area total
area_total = area_side + area_top
print(f'You need {area_total:.2f}m^2 of gold foil to cover the pyramid')
