# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: Christopher
# Austin
# Eddy
# Reed
# Section: 568
# Assignment: rockets red glare
# Date: 15 September 2022

from math import sqrt
a = 1/ 7
print(a,"a")
b = a * 7
print(b,"b")

c = 2 * a;
d = 5 * a;
e = c + d;
print(e,"e")

x = sqrt(1 / 3);
print("x =", x);
y = x * x * 3;
print("x*x*3 =", y);
z = x * 3 * x;
print("x*3*x =", z);



first_stop = 0.3
second_go = 0.4
step_size = 0.1
current_increment = int(input('Enter current increment: \n'))

distance_travel = current_increment * step_size
print(distance_travel)
if distance_travel == 0.3:
    print('Stop the first stage!')
elif distance_travel == 0.4:
    print('Start the second stage!')
else:
    print('No action required at this point.')


print("\n lets try that again 'zrrp' \n")

TOL = 1e-17

print(distance_travel)
if abs(distance_travel - 0.3) < TOL:
    print('Stop the first stage!')
elif abs(distance_travel - 0.4) < TOL:
    print('Start the second stage!')
else:
    print('No action required at this point.')
# yaya now the program works, but when using e-20, the probam does not work
# pobably because the diffrence isn't that small
# The code stops working when e-17a