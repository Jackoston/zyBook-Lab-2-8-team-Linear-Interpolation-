# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: Christopher
# Austin
# Eddy
# Reed
# Section: 568
# Assignment: 6-11 Pyramid Area
# Date: 20 September 2022


from math import sqrt
sideL = float(input("Enter the side length in meters: "))
layers = int(input("Enter the number of layers: "))
area = 0
n = layers
for n in range(1, layers + 1):
    area = area + n * 3 * (sideL ** 2)

area_top = (sqrt(3) / 4) * (layers * sideL) ** 2
area_total = area + area_top
print(f'You need {area_total:.2f}m^2 of gold foil to cover the pyramid')
