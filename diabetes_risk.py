
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

sex_input=input("Enter your sex(M/F):")
age=int(input("Enter your age (years):"))
BMI_input=input("Enter your BMI:")
hypertension_input =input("Are you on medication for hypertension (Y/N)?")
steroids_input =input("Are you on steroids (Y/N)?")
smoker_input=input("Do you smoke cigarettes (Y/N)?")
Did_Smoke_input= input("Did you used to smoke (Y/N)?")
history_input=input("Do you have a family history of diabetes (Y/N)?")

# Variable inputs






#asign variable to number for equation

# sex ifs
if sex_input.upper() == 'M':
    sex = 0
elif sex_input.upper() == 'F':
    sex = 0.879

#BMI ifs
if BMI_input < 25:
    BMI = 0
elif 25 <= BMI_input <27.5:
    BMI = 0.699
elif 27.5 <= BMI_input < 30:
    BMI = 1.97
else:
    BMI = 2.518
if smoker_input.upper()=="Y":
    smoke=0.855;

#Calculations
#n = 6.322 + sex – (0.063 * age) – BMI – hypertension – steroids – smoker – history



# risk = 100 / (1+en)