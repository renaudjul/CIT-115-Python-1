# Julie Renaud
# jmrenaud2001@student.stcc.edu
# CIT 115
# 3/9/2022
# Grade Analyzer


# variable
sGrade = ""


# Inputs
sName = input("Name of person that we are calculating the grades for: ")
nTest1 = int(input("Test 1: "))
nTest2 = int(input("Test 2: "))
nTest3 = int(input("Test 3: "))
nTest4 = int(input("Test 4: "))
sChoice = str(input("Do you wish to drop the lowest grade? Y or N: ")).upper()


# Checks if all tests are > 0
if nTest1 < 0 or nTest2 < 0 or nTest3 < 0 or nTest4 < 0:
    raise SystemExit("Test scores must be greater than Zero.")


# Checks Choice if Y or N
if sChoice != "Y" and sChoice != "N":
    raise SystemExit("Enter Y or N to Drop the Lowest Grade.")


# Choice == N (Averages all tests)
if sChoice == "N":
    print("\nYour lowest grade will Not be dropped.\n")
    fAverage = (nTest1 + nTest2 + nTest3 + nTest4) / 4


# Choice == Y (subtracts lowest test from average)
if sChoice == "Y":
    print("\nYour lowest grade Will be dropped.")

    if nTest1 < nTest2:
        if nTest1 < nTest3:
            if nTest1 < nTest4:
                fAverage = (nTest2 + nTest3 + nTest4) / 3
                print("Test 1 was dropped.\n")
    elif nTest2 < nTest1:
        if nTest2 < nTest3:
            if nTest2 < nTest4:
                fAverage = (nTest1 + nTest3 + nTest4) / 3
                print("Test 2 was dropped.\n")
    elif nTest3 < nTest1:
        if nTest3 < nTest2:
            if nTest3 < nTest4:
                fAverage = (nTest1 + nTest2 + nTest4) / 3
                print("Test 3 was dropped.\n")
    else:
        fAverage = (nTest1 + nTest2 + nTest3) / 3
        print("Test 4 was dropped.\n")


# Determines averages letter grade
if fAverage >= 97.0:
    sGrade = "A+"
elif fAverage >= 94.0 and fAverage <= 96.9:
    sGrade = "A"
elif fAverage >= 90.0 and fAverage <= 93.9:
    sGrade = "A-"
elif fAverage >= 87.0 and fAverage <= 89.9:
    sGrade = "B+"
elif fAverage >= 84.0 and fAverage <= 86.9:
    sGrade = "B"
elif fAverage >= 80.0 and fAverage <= 83.9:
    sGrade = "B-"
elif fAverage >= 77.0 and fAverage <= 79.9:
    sGrade = "C+"
elif fAverage >= 74.0 and fAverage <= 76.9:
    sGrade = "C"
elif fAverage >= 70.0 and fAverage <= 73.9:
    sGrade = "C-"
elif fAverage >= 67.0 and fAverage <= 69.9:
    sGrade = "D+"
elif fAverage >= 64.0 and fAverage <= 66.9:
    sGrade = "D"
elif fAverage >= 60.0 and fAverage <= 63.9:
    sGrade = "D-"
else:
    sGrade = "F"


# # Output
print(f"{sName}'s test average is: {fAverage :.1f}")
print(f"Letter Grade for the test average is: {sGrade}")
