# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: Austin
# Christopher
# Eddy
# Reed
# Section: 468
# Assignment:  Lab 3 - 16 (Team): Still More Linear Interpolation
# Date: 8 Sep. 2022

# 1st Variables:
t1 = float(input('Enter time 1: '))  # x1
x1 = float(input('Enter the x position of the object at time 1: '))  # y1
y1 = float(input('Enter the y position of the object at time 1: '))  # y1
z1 = float(input('Enter the z position of the object at time 1: '))  # y1

# 2nd Variables:
t2 = float(input('Enter time 2: '))  # x2
x2 = float(input('Enter the x position of the object at time 2: '))  # y2
y2 = float(input('Enter the y position of the object at time 2: '))  # y2
z2 = float(input('Enter the z position of the object at time 2: '))  # y2

# Space:
print('')

# Time Calculations:
t_int = (t2 - t1) / 4
t_dist1 = t1 + t_int
t_dist2 = t_dist1 + t_int
t_dist3 = t_dist2 + t_int

# Linear Interpolation Calculation:
# 1st
new_x1 = x1 + (t1 - t1) * ((x2 - x1) / (t2 - t1))
new_y1 = y1 + (t1 - t1) * ((y2 - y1) / (t2 - t1))
new_z1 = z1 + (t1 - t1) * ((z2 - z1) / (t2 - t1))
print(f'At time {t1:.2f} seconds the object is at ({new_x1:.3f}, {new_y1:.3f}, {new_z1:.3f})')

# 2nd
new_x2 = x1 + (t_dist1 - t1) * ((x2 - x1) / (t2 - t1))
new_y2 = y1 + (t_dist1 - t1) * ((y2 - y1) / (t2 - t1))
new_z2 = z1 + (t_dist1 - t1) * ((z2 - z1) / (t2 - t1))
print(f'At time {t_dist1:.2f} seconds the object is at ({new_x2:.3f}, {new_y2:.3f}, {new_z2:.3f})')

# 3nd
new_x2 = x1 + (t_dist2 - t1) * ((x2 - x1) / (t2 - t1))
new_y2 = y1 + (t_dist2 - t1) * ((y2 - y1) / (t2 - t1))
new_z2 = z1 + (t_dist2 - t1) * ((z2 - z1) / (t2 - t1))
print(f'At time {t_dist2:.2f} seconds the object is at ({new_x2:.3f}, {new_y2:.3f}, {new_z2:.3f})')

# 4nd
new_x2 = x1 + (t_dist3 - t1) * ((x2 - x1) / (t2 - t1))
new_y2 = y1 + (t_dist3 - t1) * ((y2 - y1) / (t2 - t1))
new_z2 = z1 + (t_dist3 - t1) * ((z2 - z1) / (t2 - t1))
print(f'At time {t_dist3:.2f} seconds the object is at ({new_x2:.3f}, {new_y2:.3f}, {new_z2:.3f})')

# 5th
new_x4 = x1 + (t2 - t1) * ((x2 - x1) / (t2 - t1))
new_y4 = y1 + (t2 - t1) * ((y2 - y1) / (t2 - t1))
new_z4 = z1 + (t2 - t1) * ((z2 - z1) / (t2 - t1))
print(f'At time {t2:.2f} seconds the object is at ({new_x4:.3f}, {new_y4:.3f}, {new_z4:.3f})')
