# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: Christopher
# Austin
# Eddy
# Reed
# Section: 568
# Assignment: Week 8 Deep Plots
# Date: 13th October 2022

# Import:
import matplotlib.pyplot as plt
from math import e

# t & y Values:
t = [0, 0.45, 1.1, 1.75, 2.25, 2.7]
y = [0, 0.23, 0.4, 0.18, 0.07, 0.01]

# Line Calculation:
y_calc = []
t_list = []
for t in range(150):
    t /= 50
    t_list.append(t)
print(t_list)

# Dot Calculation:
# y(t) = t^2 exp(-t^2)
# y(t) = t^4 exp(-t^2)
fun1_list = []
for i in t:
    fun1 = [(i ** 2) * (e ** (-i ** 2))]
    fun1_list.append(fun1)
print(fun1_list)

fun2_list = []
for i in t:
    fun2 = [(i ** 4) * (e ** (-i ** 2))]
    fun2_list.append(fun2)
print(fun2_list)

# Plots:
plt.subplot(2, 1, 1)
plt.plot(t, fun1_list, 'ko')

plt.subplot(2, 1, 2)
plt.plot(t, fun2_list)

# Plot Print:
plt.show()
