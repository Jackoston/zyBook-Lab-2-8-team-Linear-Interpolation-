# --------------------------------------- IMPORTS STATEMENTS----------------------------------------
# (Put the necessary import statements first)





# -------------------------------------- FUNCTION DEFINITIONS---------------------------------------
# (Then put any function definitions; I've done a couple already!—don't change mine.)

def trajectory_y(x, g, vo, angle):
   """Returns (y-value) of the trajectory for a given x-val, gravity, initial velocity,and angle."""
   angle = radians(angle)
   return (x*tan(angle))-(g*x**2)/(2*(vo**2)*cos(angle)**2)

#####
#####
#####


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