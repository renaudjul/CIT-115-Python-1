# Julie Renaud
# jmrenaud2001@student.stcc.edu
# CIT 115
# 4/9/2022
# Compound Interest w/ Loops



# Input validator function
def promptUserInput(sPrompt, nMin, sDataType):
    nInput = nMin - 1
    while nInput < nMin:
        try:
            if sDataType == "float":
                nInput = float(input(sPrompt))
            else:
                nInput = int(input(sPrompt))

            if nInput < nMin and nMin == 0:
                print("\nGoal must be 0 or greater. Try again." )
            if nInput< nMin and (nMin == 0.01 or nMin == 1):
                print( "\nInput must be a positive numeric value. Try again." )

        except ValueError:
            print( "Input must be a numeric value" )
        except :
            print( "Unexpected error. Program will end." )
            exit()
    return nInput


# Monthly Balance function
def monthlyBalanceLoop(nNumberOfMonths, fDeposit, fMonthlyInterestRate):
    for iNumberOfMonths in range( 1, nNumberOfMonths + 1 ) :
        fDeposit += fDeposit * fMonthlyInterestRate
        print( f"\nMonth: {iNumberOfMonths : <4}     Account Balance is: ${fDeposit : ,.2f}" )


# Monthly Interest Rate function
def calculateMonthlyInterest(fInterestRate):
    return fInterestRate / 12


# Months to Hit Goal function
def monthsTillGoal(fDeposit, fGoal, fMonthlyInterestRate):
    iCountMonthsGoal = 0
    while fDeposit <= fGoal :
        iCountMonthsGoal += 1
        fDeposit += fDeposit * fMonthlyInterestRate
    print( f"\nIt will take: {iCountMonthsGoal} months to reach the goal of ${fGoal : ,.2f}" )


# main function
def main():
        # Calls Input validator function for each variable
        fDeposit = promptUserInput( "\nWhat is the original deposit (positive value): ", 0.01, "float" )
        fInterestRate = (promptUserInput( "\nWhat is the interest rate (positive value): ", 0.01, "float" )) / 100
        nNumberOfMonths = promptUserInput( "\nWhat is the number of months (positive value): ", 1, "int" )
        fGoal = promptUserInput( "\nWhat is the goal amount (can enter 0 but not negative): ", 0, "float" )

        # Calls monthly interest rate function
        fMonthlyInterestRate = calculateMonthlyInterest(fInterestRate)

        # Calls Monthly Balance function
        monthlyBalanceLoop(nNumberOfMonths, fDeposit, fMonthlyInterestRate)


        # Calls Months to Hit Goal function if > 0
        if fGoal > 0 :
            monthsTillGoal( fDeposit, fGoal, fMonthlyInterestRate )


main()