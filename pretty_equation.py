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

# If Statements for Postive Integers:
if coeffA > 1 and coeffB > 1 and coeffC > 1:
    print(f'The quadratic equation is {coeffA}x^2 + {coeffB}x + {coeffC} = 0')

elif coeffA == 1 and coeffB == 1 and coeffC == 1:
    print(f'The quadratic equation is x^2 + x + 1 = 0')

elif coeffA == 1 and coeffB != 1 and coeffC != 1:
    print(f'The quadratic equation is x^2 + {coeffB}x + {coeffC} = 0')
elif coeffA == 1 and coeffB == 1 and coeffC != 1:
    print(f'The quadratic equation is x^2 + x + {coeffC} = 0')
elif coeffA == 1 and coeffB != 1 and coeffC == 1:
    print(f'The quadratic equation is x^2 + {coeffB}x + 1 = 0')

elif coeffB == 1 and coeffA != 1 and coeffC != 1:
    print(f'The quadratic equation is {coeffA}x^2 + x + {coeffC} = 0')
elif coeffB == 1 and coeffA == 1 and coeffC != 1:
    print(f'The quadratic equation is x^2 + x + {coeffC} = 0')
elif coeffB == 1 and coeffA != 1 and coeffC == 1:
    print(f'The quadratic equation is {coeffA}x^2 + x + 1 = 0')

elif coeffC == 1 and coeffA != 1 and coeffB != 1:
    print(f'The quadratic equation is {coeffA}x^2 + {coeffB}x + 1 = 0')
elif coeffC == 1 and coeffA == 1 and coeffB != 1:
    print(f'The quadratic equation is x^2 + {coeffB}x + 1 = 0')
elif coeffC == 1 and coeffA != 1 and coeffB == 1:
    print(f'The quadratic equation is {coeffA}x^2 + x + 1 = 0')


elif coeffA == 0 and coeffB == 0 and coeffC == 0:
    print(f'The quadratic equation is 0')

elif coeffA == 0 and coeffB != 0 and coeffC != 0:
    print(f'The quadratic equation is {coeffB}x + {coeffC} = 0')
elif coeffA == 0 and coeffB == 0 and coeffC != 0:
    print(f'The quadratic equation is {coeffC} = 0')
elif coeffA == 0 and coeffB != 0 and coeffC == 0:
    print(f'The quadratic equation is {coeffB}x = 0')

elif coeffB == 0 and coeffA != 0 and coeffC != 0:
    print(f'The quadratic equation is {coeffA}x^2 + {coeffC} = 0')
elif coeffB == 0 and coeffA == 0 and coeffC != 0:
    print(f'The quadratic equation is {coeffC} = 0')
elif coeffB == 0 and coeffA != 0 and coeffC == 0:
    print(f'The quadratic equation is {coeffA}x^2 = 0')

elif coeffC == 0 and coeffA != 0 and coeffB != 0:
    print(f'The quadratic equation is {coeffA}x^2 + {coeffB}x = 0')
elif coeffC == 0 and coeffA == 0 and coeffB != 0:
    print(f'The quadratic equation is {coeffB}x = 0')
elif coeffC == 0 and coeffA != 0 and coeffB == 0:
    print(f'The quadratic equation is {coeffA}x^2 = 0')


elif coeffA < -1 and coeffB < -1 and coeffC < -1:
    print(f'The quadratic equation is - {abs(coeffA)}x^2 - {abs(coeffB)}x - {abs(coeffC)}')

elif coeffA < -1 and coeffB > 1 and coeffC > 1:
    print(f'The quadratic equation is - {abs(coeffA)}x^2 + {coeffB}x + {coeffC} = 0')
elif coeffA < -1 and coeffB < -1 and coeffC > 1:
    print(f'The quadratic equation is - {abs(coeffA)}x^2 - {abs(coeffB)}x + {coeffC} = 0')
elif coeffA < -1 and coeffB > 1 and coeffC < -1:
    print(f'The quadratic equation is - {abs(coeffA)}x^2 + {coeffB}x - {abs(coeffC)} = 0')

elif coeffB < -1 and coeffA > 1 and coeffC > 1:
    print(f'The quadratic equation is {coeffA}x^2 - {abs(coeffB)}x + {coeffC} = 0')
elif coeffB < -1 and coeffA < -1 and coeffC > 1:
    print(f'The quadratic equation is - {abs(coeffA)}x^2 - {abs(coeffB)}x + {coeffC} = 0')
elif coeffB < -1 and coeffA > 1 and coeffC < -1:
    print(f'The quadratic equation is {coeffA}x^2 - {abs(coeffB)}x - {abs(coeffC)} = 0')

elif coeffC < -1 and coeffA > 1 and coeffB > 1:
    print(f'The quadratic equation is {coeffA}x^2 + {coeffB}x - {abs(coeffC)} = 0')
elif coeffC < -1 and coeffA < -1 and coeffB > 1:
    print(f'The quadratic equation is - {abs(coeffA)}x^2 + {coeffB}x - {abs(coeffC)} = 0')
elif coeffC < -1 and coeffA > 1 and coeffB < -1:
    print(f'The quadratic equation is + {coeffA}x^2 - {abs(coeffB)}x - {abs(coeffC)} = 0')
