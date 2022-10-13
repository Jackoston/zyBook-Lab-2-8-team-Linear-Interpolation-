from math import e
t = [0, 0.45, 1.1, 1.75, 2.25, 2.7]
y = [0, 0.23, 0.4, 0.18, 0.07, 0.01]
# t^2 * e^(-t^2)
#func_1 = t** 2 * e ** (-t ** 2)
#func_2 = t** 4 * e ** (-t ** 2)

y_calc = []
t_list = []
for t in range(150):
    t /= 50
    t_list.append(t)
print(t_list)

