# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: Austin
# Chrisopher
# Reed
# Eddy
# Section: 468
# Assignment: Lab 4 - 13: Make Change
# Date: 14th Sep. 2022

# Inputs:
coeffA = int(input('Please enter the coefficient A: '))
coeffB = int(input('Please enter the coefficient B: '))
coeffC = int(input('Please enter the coefficient C: '))

print('The quadratic equation is', end=' ')

if coeffA == 0:
    if coeffB == 0:
        if coeffC == 0:
            water = 12
        elif coeffC == 1:
            print(f'1', end=' ')
        elif coeffC > 0:
            print(f'{coeffC}', end=' ')
        elif coeffC < 0:
            print(f'- {coeffC * -1}', end=' ')
    elif coeffB == 1:
        print(f'x', end=' ')
    elif coeffB > 0:
        print(f'{coeffB}x', end=' ')
    elif coeffB < 0:
        print(f'- {coeffB * -1}x', end=' ')
elif coeffA == 1:
    print('x^2', end=' ')
    if coeffB == 0:
        water = 12
    elif coeffB == 1:
        print(f'+ x', end=' ')
    elif coeffB == -1:
        print('- x', end=' ')
    elif coeffB > 0:
        print(f'+ {coeffB}x', end=' ')
    elif coeffB < 0:
        print(f'- {coeffB * -1}x', end=' ')
elif coeffA == -1:
    print('- x^2', end=' ')
    if coeffB == 0:
        water = 12
    elif coeffB == 1:
        print(f'+ x', end=' ')
    elif coeffB == -1:
        print('- x', end=' ')
    elif coeffB > 0:
        print(f'+ {coeffB}x', end=' ')
    elif coeffB < 0:
        print(f'- {coeffB * -1}x', end=' ')
elif coeffA > 0:
    print(f'{coeffA}x^2', end=' ')
    if coeffB == 0:
        water = 12
    elif coeffB == 1:
        print(f'+ x', end=' ')
    elif coeffB == -1:
        print('- x', end=' ')
    elif coeffB > 0:
        print(f'+ {coeffB}x', end=' ')
    elif coeffB < 0:
        print(f'- {coeffB * -1}x', end=' ')
elif coeffA < 0:
    print(f'- {coeffA * -1}x^2', end=' ')
    if coeffB == 0:
        water = 12
    elif coeffB == 1:
        print(f'+ x', end=' ')
    elif coeffB == -1:
        print('- x', end=' ')
    elif coeffB > 0:
        print(f'+ {coeffB}x', end=' ')
    elif coeffB < 0:
        print(f'- {coeffB * -1}x', end=' ')


if coeffC == 0:
    water = 12
elif coeffC == 1:
    print(f'+ 1', end=' ')
elif coeffC > 0:
    print(f'+ {coeffC}', end=' ')
elif coeffC < 0:
    print(f'- {coeffC * -1}', end=' ')

print('= 0')
