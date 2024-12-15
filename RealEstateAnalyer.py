# Julie Renaud
# jmrenaud2001@student.stcc.edu
# CIT 115
# 5/14/2022
# Real Estate Analyzer

import math


def getFloatInput(sPrompt) :
    fInput = -0.99
    while fInput < 0.1 :

        try :
            fInput = float( input( sPrompt ) )

            if fInput < 0.1 :
                print( "\nInput a number that is greater than 0. Try again." )

        except ValueError :
            print( "\nInput must be a numeric value. Try again." )
        except :
            print( "\nUnexpected Error in getFloatInput(). Program will end." )
            exit()

    return fInput





def getMedian(fPropertySalesList) :
    nMod = len( fPropertySalesList ) % 2
    fDivByTwo = len( fPropertySalesList ) / 2

    if nMod == 1 :
        return getOddMedian( fPropertySalesList, fDivByTwo )

    if nMod == 0 :
        return getEvenMedian( fPropertySalesList, fDivByTwo )

    return -1





def getOddMedian(fPropertySalesList, fDivByTwo) :
    nMedIndex = math.ceil( fDivByTwo ) - 1

    i = 0
    while i <= fPropertySalesList[nMedIndex] :

        if i == nMedIndex :
            fMedian = fPropertySalesList[i]
            return fMedian

        i += 1

    return -1





def getEvenMedian(fPropertySalesList, fDivByTwo) :
    try :
        nIndexMax = int( fDivByTwo )
        nIndexMin = int( fDivByTwo - 1 )


        i = 0
        while i < fPropertySalesList[nIndexMax] :
            if i == nIndexMin :
                fMedMin = fPropertySalesList[i]

            if i == nIndexMax :
                fMedianMax = fPropertySalesList[i]

            i += 1
            

        return (fMedMin + fMedianMax) / 2

    except :
        raise SystemExit( "Error in getEvenMedian()" )

    return -1






def getOutput(fMedian, fSortedList) :
    print( "\n" )
    count = 1
    i = 0
    while i < len( fSortedList ) :
        print( f"Property {count}  ${fSortedList[i] : ,.2f}" )
        count += 1
        i += 1

    print( f"\nMinimum:    ${min( fSortedList ): ,.2f}" )
    print( f"Maximum:    ${max( fSortedList ) : ,.2f}" )
    print( f"Total:      ${sum( fSortedList ) : ,.2f}" )
    print( f"Average:    ${sum( fSortedList ) / len( fSortedList ) : ,.2f}" )
    print( f"median:     ${fMedian : ,.2f}" )
    print( f"Commission: ${sum( fSortedList ) * .03: ,.2f}" )






def main() :
    fPropertySalesList = []
    sChoice = ""

    while sChoice != "N" :

        try :
            fSalesInput = getFloatInput( "\nEnter Property Sales Value: " )

            fPropertySalesList.append( fSalesInput )

            

            while sChoice != "N" :
                sChoice = input( "\nEnter Another Value? Y or N: " ).upper()


                if sChoice != "Y" and sChoice != "N" :
                    print( "\nEnter Y or N. Try Again." )
                    continue


                if sChoice == "Y" :
                    break


                if sChoice == "N" :
                    fSortedList = sorted( fPropertySalesList, key=float )

                    fMedian = getMedian( fSortedList )

                    if fMedian == -1 :
                        print( "Error on getMedian() return == -1" )
                        exit()

                    getOutput( fMedian, fSortedList )

                    

        except ValueError :
            print( "\nInput Value Error. Try again." )
        except :
            print( "\nUnexpected Error in Main(). Program will end." )
            exit()


main()
