# Julie Renaud
# jmrenaud2001@student.stcc.edu
# CIT 115
# 5/2/2022
# Paint Job Calculating App


import math

# Input Validator Function
def getFloatInput(sPrompt) :
    nInput = 0
    while nInput < 0.1:
        try :
            nInput = float( input( sPrompt ) )

            if nInput < 0.1 :
                print( "\nInput must be a positive numeric value. Try again." )

        except ValueError :
            print( "\nInput must be a numeric value. Try again." )
        except :
            print( "\nUnexpected error. Program will end." )
            exit()

    return nInput



# Calculates Gallons of Paint needed
def getGallonsOfPaint(fWallSqrFt, fFeetPerGallon):
    return math.ceil(fWallSqrFt / fFeetPerGallon)



# Calculates Labor Hours needed
def getLaborHours(fLaborHoursPerGallon,iTotalGallons):
    return fLaborHoursPerGallon * iTotalGallons



# Calculates labor costs
def getLaborCost(fLaborHours, fLaborChargePerHour):
    return fLaborHours * fLaborChargePerHour



def getPaintCost(iTotalGallons, fPaintPrice):
    return iTotalGallons * fPaintPrice



def getSalesTax(fLaborCost, fPaintCost, sState):
   
        if sState == "CT" :
            fTaxRate = .06
        elif sState == "MA" :
            fTaxRate = .0625
        elif sState == "ME" :
            fTaxRate = .085
        elif sState == "NH" :
            fTaxRate = .0
        elif sState == "RI" :
            fTaxRate = .07
        elif sState == "VT" :
            fTaxRate = .06
        else :
            fTaxRate = 0.0

        return (fLaborCost + fPaintCost) * fTaxRate



def taxRateTotal(fLaborCost, fPaintCost, fSalesTax):
    return (fLaborCost + fPaintCost) * fSalesTax



def showCostEstimate(iTotalGallons, fLaborHours, fLaborCost, fPaintCost, fSalesTax, sLastName):
    # Prints to command line
    print( f"\nGallons of paint needed: {iTotalGallons}" )
    print( f"Hours of labor needed: {fLaborHours}" )
    print( f"Paint charges: ${fPaintCost : ,.2f}" )
    print( f"Labor charges: ${fLaborCost : ,.2f}" )
    print( f"Tax: ${fSalesTax : ,.2f}" )
    print(f"Total cost: ${fLaborCost + fPaintCost + fSalesTax : ,.2f}")

    # creates unique file name
    sFileName = f"{sLastName}_PaintJobOutput.txt."

    # Creates new file & writes to it w/ auto close
    with open(f"{sFileName}", "w" ) as file:
        print( f"file: {sFileName} was created." )
        file.write(f"Gallons of paint needed: {iTotalGallons}\n")
        file.write(f"Hours of labor needed: {fLaborHours}\n" )
        file.write(f"Paint charges: ${fPaintCost : ,.2f}\n" )
        file.write(f"Labor charges: ${fLaborCost : ,.2f}\n" )
        file.write(f"Tax: ${fSalesTax : ,.2f}\n" )
        file.write(f"Total cost: ${fLaborCost + fPaintCost + fSalesTax : ,.2f}\n")





def main():
    # Calls validation function for each input prompt
    fWallSqrFt = getFloatInput( "Enter wall space in square feet: " )
    fPaintPrice = getFloatInput( "Enter paint price per gallon: " )
    fFeetPerGallon = getFloatInput( "Enter feet per gallon: " )
    fLaborHoursPerGallon = getFloatInput( "How many labor hours per gallon: " )
    fLaborChargePerHour = getFloatInput( "Labor charge per hour: " )


    # Customer Info
    sState = input( "State job is in: " ).upper()
    sLastName = input( "Customer Last Name: ")


    # Call all "get" functions & assign to variables
    iTotalGallons = getGallonsOfPaint( fWallSqrFt, fFeetPerGallon )

    fLaborHours = getLaborHours(fLaborHoursPerGallon,iTotalGallons)

    fLaborCost = getLaborCost(fLaborHours, fLaborChargePerHour)

    fPaintCost = getPaintCost(iTotalGallons, fPaintPrice)

    fSalesTax = getSalesTax(fLaborCost, fPaintCost, sState)

    showCostEstimate(iTotalGallons, fLaborHours, fLaborCost, fPaintCost, fSalesTax, sLastName)


main()
