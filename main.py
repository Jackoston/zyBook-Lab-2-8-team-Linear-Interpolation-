
coeffA = int(input('Please enter the coefficient A: '))
coeffB = int(input('Please enter the coefficient B: '))
#coeffC = int(input('Please enter the coefficient C: '))

if coeffA == 0:
    water = 12
elif coeffA == 1:
    print('x^2 ', end=' ')
elif coeffA > 0:
    print(f'{coeffA}x^2', end=' ')
elif coeffA < 0:
    print(f'- {coeffA * -1}x^2', end=' ')

if coeffB == 0:
    water = 12
elif coeffB == 1:
    print(f'+ x', end=' ')
elif coeffB > 0:
    print(f'+ {coeffB}x', end=' ')
elif coeffB < 0:
    print(f'- {coeffB * -1}x', end=' ')
