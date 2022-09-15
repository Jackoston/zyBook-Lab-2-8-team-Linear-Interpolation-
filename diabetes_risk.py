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

# Variable Inputs:
sex_input = input("Enter your sex (M/F): ")
age = int(input("Enter your age (years): "))
BMI_input = float(input("Enter your BMI: "))
hypertension_input = input("Are you on medication for hypertension (Y/N)? ")
steroids_input = input("Are you on steroids (Y/N)? ")
smoker_input = input("Do you smoke cigarettes (Y/N)? ")

# Assign Variables w/ Number For Equation:

# Sex Ifs:
if sex_input.upper() == 'M':
    sex = 0
elif sex_input.upper() == 'F':
    sex = 0.879

# BMI Ifs:
if BMI_input < 25:
    BMI = 0
elif 25 <= BMI_input < 27.5:
    BMI = 0.699
elif 27.5 <= BMI_input < 30:
    BMI = 1.97
else:
    BMI = 2.518

# Hypertension Meds Ifs:
if hypertension_input.upper() == 'Y':
    hypertension = 1.222
else:
    hypertension = 0

# Steroid Meds Ifs:
if steroids_input.upper() == "Y":
    steroids = 2.191
else:
    steroids = 0

# Smoker Ifs:
if smoker_input.upper() == "N":
    did_smoke_input = input("Did you used to smoke (Y/N)? ")
    if did_smoke_input.upper() == 'N':
        smoker = 0
    elif did_smoke_input.upper() == 'Y':
        smoker = -0.218
elif smoker_input.upper() == "Y":
    smoker = 0.855

# Family History Ifs:
history_input = input("Do you have a family history of diabetes (Y/N)? ")
if history_input.upper() == 'Y':
    both_input = ('Both parent and sibling (Y/N)? ')
    if both_input == 'Y':
        history = 0.753
    else:
        history = 0.728
elif history_input.upper() == 'N':
    history = 0

# Calculations & Printing:
n = 6.322 + sex - (0.063 * age) - BMI - hypertension - steroids - smoker - history
risk = 100 / (1 + e ** n)
print(f"Your risk of developing type-2 diabetes is {risk:.1f}%")
