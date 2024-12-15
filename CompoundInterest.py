fPV = float(input("Enter the starting principal: "))
fR  = float(input("Enter the annual interest rate: "))/100
fT  = float(input("How many times per year is the interest compounded? "))
nM  = int(input("For how many years will the account earn interest? "))


# Calculation
fFV = fPV * (1 + fR / nM) ** (nM * fT)


# Output
print("At the end of", nM, "years you will have $", format(fFV, ",.2f"))
