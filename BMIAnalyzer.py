# Julie Renaud
# jmrenaud2001@student.stcc.edu
# CIT 115
# 3/2/2022
# BMI Calculator


# Constants
fMETER_CONV = 39.36
fKILO_CONV = 2.2

# Title
print("Welcome to Julie's BMI Calculator\n")

# Input
sName = input("Name of person that we are calculating the BMI for: ")
nHeightInches = int(input("Supply height in inches: "))
nWeightLbs = int(input("Supply weight in pounds: "))

# Conversions
fHeightMeter = nHeightInches / fMETER_CONV
fWeightKilo = nWeightLbs / fKILO_CONV

# BMI Calculation
fBMI = fWeightKilo / (fHeightMeter * fHeightMeter)

# BMI Conditional Status
if fBMI <= 18.50:
    sStatus = "Underweight"
elif fBMI > 18.50 and fBMI <= 24.90:
    sStatus = "Normal"
elif fBMI >= 24.91 and fBMI <= 29.90:
    sStatus = "Overweight"
else:
    sStatus = "Obese"


# Output
print(sName, "'s BMI is: ", format(fBMI, ".2f"))
print("BMI finding is the subject is: ", sStatus)


