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
sideL = float(input("Enter the side length in meters: \n"))
layers = int(input("Enter the number of layers: \n"))
area_side = 0
n = layers
# range 1- given layers
for n in range(1, layers + 1):
    # layers * 3 squares
    # where squares = side length ^2
    area_side = area_side + n * 3 * (sideL ** 2)

# area top is equivalent to area bottom of pyramid
area_top = (sqrt(3) / 4) * (layers * sideL) ** 2
# adding the two areas
area_total = area_side + area_top
print(f'You need {area_total:.2f}m^2 of gold foil to cover the pyramid')
