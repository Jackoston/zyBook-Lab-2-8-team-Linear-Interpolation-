# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Austin
#               Christopher
#               Reed
#               Eddy
# Section:      468
# Assignment:   10 - 13 Debugged Code
# Date:         Nov. 15th, 2022

# As a team, we have gone through all required sections of the
# tutorial, and each team member understands the material

import numpy as np

array_a = np.arange(12).reshape(3, 4)
print(f'A = {array_a}')

print('')

array_b = np.arange(8).reshape(4, 2)
print(f'B = {array_b}')

print('')

array_c = np.arange(6).reshape(2, 3)
print(f'C = {array_c}')

print('')

array_d = array_a @ array_b @ array_c
print(f'D = {array_d}')

print('')

array_dt = array_d.T
print(f'D^T = {array_dt}')

print('')

array_e = np.sqrt(array_d) / 2
print(f'E = {array_e}')
