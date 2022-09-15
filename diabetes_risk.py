# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: Christopher
# Austin
# Eddy
# Reed
# Section: 568
# Assignment: 5.3
# Date: 13 September 2022

from math import e

# Variable inputs
sex_input = input("Enter your sex(M/F): \n")
age = int(input("Enter your age (years): \n"))
BMI_input = float(input("Enter your BMI: \n"))
hypertension_input = input("Are you on medication for hypertension (Y/N)? \n")
steroids_input = input("Are you on steroids (Y/N)? \n")
smoker_input = input("Do you smoke cigarettes (Y/N)? \n")
if smoker_input.upper() == 'N':
    Did_Smoke_input = input("Did you used to smoke (Y/N)? \n")

history_input = input("Do you have a family history of diabetes (Y/N)? \n")

# assign variable to number for equation

# sex ifs
if sex_input.upper() == 'M':  # male
    sex = 0
elif sex_input.upper() == 'F':  # female
    sex = 0.879

# BMI ifs
if BMI_input < 25:  # under 25
    BMI = 0
elif 25 <= BMI_input < 27.5:  # between 25 and 27.5
    BMI = 0.699
elif 27.5 <= BMI_input < 30:  # between 27.5 and 30
    BMI = 1.97
else:   # over 30
    BMI = 2.518

# Hypertension meds ifs
if hypertension_input.upper() == 'Y':   # on meds
    hypertension = 1.222
else:   # no meds
    hypertension = 0

# steroid meds ifs
if steroids_input.upper() == "Y":   # on steroids
    steroids = 2.191
else:   # no steroids
    steroids = 0

# Smoker ifs
if smoker_input.upper() == "Y":  # smoker
    smoker = 0.855
elif Did_Smoke_input.upper() == "N":  # non smoker
    smoker = 0
else:   # did smoke
    smoker = -0.218

# Family History Ifs:
if history_input.upper() == 'Y':    # family history pos
    both_input = input('Both parent and sibling (Y/N)? \n')
    if both_input.upper() == 'Y':   # both parent and sibling
        history = 0.753
    elif both_input.upper() == 'N':  # parent or sibling
        history = 0.728
if history_input.upper() == 'N':  # no family history
    history = 0

# Calculations
n = 6.322 + sex - (0.063 * age) - BMI - hypertension - steroids - smoker - history

risk = 100 / (1 + e ** n)

print(f'Your risk of developing type-2 diabetes is {risk:.1f}%')
