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
fig = plt.figure('Frodo likes this.')
from math import e

# t & y Values:
t5 = [0, 0.45, 1.1, 1.75, 2.25, 2.7]
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
for t in t_list:
    fun1 = [(t ** 2) * (e ** (-t ** 2))]
    fun1_list.append(fun1)
print(fun1_list)

fun2_list = []
for t in t_list:
    fun2 = [(t ** 4) * (e ** (-t ** 2))]
    fun2_list.append(fun2)
print(fun2_list)

# Plots:
plt.subplot(2, 1, 1)
plt.plot(t5, y, 'ko', label='data')
plt.plot(t_list, fun1_list, 'r-',  label='t^2*exp(–t^2)')
plt.plot(t_list, fun2_list, 'b-', label='t^4*exp(–t^2)')
plt.legend(loc='upper right')
plt.title('Data and two curves vs. time')
plt.xlabel('time')
plt.ylabel('y')
plt.ylim(-.03, 1, .25)
plt.xlim(0, 3)

# second plot
plt.subplot(2, 1, 2)
plt.plot(t_list, fun1_list, 'b-',  label='t^2*exp(–t^2)')
plt.plot(t5, y, 'y-')
plt.plot(t5, y, 'y^', label='data')
plt.legend(loc='upper right')
plt.title('Data interpolation and Curve 1')
plt.xlabel('time')
plt.ylabel('y')
arrow_properties = {
    'facecolor': 'black',
    'shrink': 0.0,
    'headlength': 5,
    'width': 1
}
plt.annotate("It's closest here!", xy=(1.35, .25), xytext = (1.2, 0.1), arrowprops=arrow_properties)
plt.ylim(0, .5)
plt.xlim(1, 2)


# Plot Print:
plt.tight_layout()
plt.show()
