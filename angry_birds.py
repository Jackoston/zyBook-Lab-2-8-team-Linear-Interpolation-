# --------------------------------------- IMPORTS STATEMENTS----------------------------------------
# (Put the necessary import statements first)

import random
from math import radians, tan, cos
import matplotlib.pyplot as plt

# -------------------------------------- FUNCTION DEFINITIONS---------------------------------------
# (Then put any function definitions; I've done a couple already!—don't change mine.)


def trajectory_y(x, g, vo, angle):
    """Returns (y-value) of the trajectory for a given x-val, gravity, initial velocity,and angle."""
    angle = radians(angle)
    return (x*tan(angle))-(g*x**2)/(2*(vo**2)*cos(angle)**2)


def trajectory(gravity, velocity, angle):
    x_vals = []
    y_vals = []
    for x in range(1001):
        x_vals.append(x)
    for x in x_vals:
        y = trajectory_y(x, gravity, velocity, angle)
        y_vals.append(y)
    return x_vals, y_vals


def bird_picker():
   bird_type = {'Red': 'r,s',
            'Chuck': 'y,s',
            'Bomb': 'k,l',
            'Terence': 'r,l'
            }
   while True:
      print('Birds: Red = red, small bird; Chuck = yellow, small bird; Bomb = black, large bird; Terence = red, large bird')
      bird = input('Pick a bird: ')
      if bird in bird_type:
         return bird_type[bird]
      else:
         print('Bad Input')


def planet_picker():
   gravity = {'Earth': 9.807,
              'Mars': 3.711,
              'Moon': 1.625,
              'Jupiter': 24.79
              }
   while True:
      print('Planets: Earth = 9.807 m/s2, Mars = 3.711 m/s2, Moon = 1.625 m/s2, Jupiter = 24.79 m/s2')
      planet = input('Pick a planet: ')
      if planet in gravity:
         return gravity[planet]
      else:
         print('Bad input')

            
def get_guesses():
    velocity = float(input('Enter velocity (m/s): '))
    angle = float(input('Enter angle (degrees): '))
    return velocity, angle


def birds_plot(x_vals, y_vals, target, bird, hit=False):
    if bird[-1] == 's':
        size = 2
    else:
        size = 5
    if hit:
        plt.plot(target[0], target[1], 'rx', markeredgewidth=20)
    else:
        plt.plot(target[0], target[1], 'o', color='limegreen', markersize=target[-1]/2)

    plt.plot(x_vals, y_vals, f'{bird[0]}--', linewidth=size)
    plt.show()


def hit(x_vals, y_vals, target):
    TOL = 5
    x = int(target[0])
    y = y_vals[x+1]
    if target[1] - TOL <= y <= target[1] + TOL:
        return True
    else:
        return False


def get_basics():
    """Takes user selections for active bird and planet. Returns (bird, planet). 'Bird' includes
      name, color and size. 'Planet' includes name and gravity. """
    a = bird_picker()                                  # Runs fn to provide bird menu
    b = planet_picker()                                # Runs fn to provide planet menu
    return a, b


# ------------------------------------------ MAIN PROGRAM ------------------------------------------
# (Then our Main Program)

# Sets up loop so user can repeat the game as many times as desired ('y' to continue, 'n' to quit)
pig_counter = 0
again = 'y'
while again == 'y':

    # Program will pick a random distance (x from 10-1000), height (y from 0-50) and size of a target
    target = (random.randint(10, 1000), random.randint(0, 50), random.randint(10, 50))
    print(target)
    # Takes initial guesses
    bird, g = get_basics()                           # Runs fn to get bird and planet information
    v_guess, theta_guess = get_guesses()             # Runs fn to get velocity and angle guesses

    # Loops guesses until bird hits target
    x, y = trajectory(g, v_guess, theta_guess)       # Create current x- and y- value lists
    while not hit(x, y, target):                     # Program cycles until throw hits the target
        birds_plot(x, y, target, bird)               # Plots trajectory & target if miss
        v_guess, theta_guess = get_guesses()         # Gets updated guesses from user
        x, y = trajectory(g, v_guess, theta_guess)   # Creates updated lists of x- and y-values

    # Handles winning case and asks if user would like to play again
    print('Yay!')
    pig_counter += 1
    birds_plot(x, y, target, bird, True)
    again = input('Would you like to play again? (y/n)')
    while again not in {'y', 'n'}:
        again = input('Please type either y or n only. Would you like to play again? (y/n)')

# Exiting when user decides to quit
print(f'\nThanks for playing! You popped {pig_counter} pig(s) today!')
