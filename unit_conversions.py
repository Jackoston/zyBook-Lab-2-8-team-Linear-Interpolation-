# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: Christopher
# Austin
# Eddy
# Reed
# Section: 568
# Assignment: 3-15 Unit Conversions Lab
# Date: 6 September 2022

x=float(input("Please enter the quantity to be converted:" ))

#A
pound_to_newtons=x*4.44822
print(f"{x:.2f} pounds force is equivalent to {pound_to_newtons:.2f} Newtons")

#B
meters_to_feet = (float(x * 3.28084))
final_meters_to_feet = (f'{x:.2f} meters is equivalent to {meters_to_feet:.2f} feet')
print(final_meters_to_feet)

#C
atmosphere_to_kilopascal= x*101.325
print(f'{x:.2f} atmospheres is equivalent to {atmosphere_to_kilopascal:.2f} kilopascals')

#D
btu_hour = x * 3.41
print(f'{x:.2f} The BTU/h is {btu_hour:.2f}')

#E
liters_to_gallons = (float(x * 15.850323141489))
final_liters_to_gallons = (f'{x:.2f} liters per second is equivalent to {liters_to_gallons:.2f} US gallons per minute')
print(final_liters_to_gallons)

#F
degrees_fahrenheit = float((x * 1.8) + 32)
print(f'{x:.2f} degrees is equivalent to {degrees_fahrenheit:.2f} degrees')
