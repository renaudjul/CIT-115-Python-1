# Julie Renaud
# jmrenaud2001@student.stcc.edu
# CIT 115
# 5/16/2022
# Password Validator



def ValidateName(sPrompt) :
    try :
        while True :
            sFullName = input( sPrompt )
            sNameList = sFullName.split()

            if len( sNameList ) < 2 :
                print( "Invalid Name Input. Must be two words." )
                continue
            break

    except ValueError :
        print( "Input value error. Try again." )
    except :
        print( "Unexpected error. Program will end." )
        exit()

    return sFullName, sNameList





def getInitials(sNameList) :
    # get initials
    sFirst = sNameList[0]
    sLast = sNameList[1]
    sInitials = (sFirst[0] + sLast[0])
    return sInitials





def ValidatePassword(sPrompt, sInitials) :
    while True :
        bIsValidPswd = True

        # prompt
        sPassword = input( sPrompt )

        # validate if not pass
        bIsStartPass = IsStartPass( sPassword )
        if bIsStartPass :
            bIsValidPswd = False

        # validate length
        bIsLength = IsLength( sPassword )
        if bIsLength :
            bIsValidPswd = False

        # Index loop check
        bIsIndexLoop = IsIndexLoop( sPassword )
        if bIsIndexLoop :
            bIsValidPswd = False

        # validate if isInitials
        if sInitials in sPassword or sInitials.lower() in sPassword :
            print( "Password must not contain user initials." )
            bIsValidPswd = False

        # validate no repeat chars
        bIsRepeatChar = IsRepeatChar( sPassword )
        if bIsRepeatChar :
            bIsValidPswd = False

        if bIsValidPswd :
            print( "Password is valid and OK to use." )
            break





def IsStartPass(sPassword) :
    if sPassword.startswith( "Pass" ) or sPassword.startswith( "pass" ) :
        print( "Password can’t start with Pass. Try Again." )
        return True
    return False





def IsLength(sPassword) :
    if len( sPassword ) < 8 or len( sPassword ) > 12 :
        print( "Password must be between 8 and 12 characters. Try Again." )
        return True
    return False





def IsIndexLoop(sPassword) :
    sUpperStr = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sLowerStr = "abcdefghijklmnopqrstuvwxyz"
    sNumStr = "0123456789"
    sSpecialCharStr = "!@#$%^"
    nUpper = 0
    nLower = 0
    nNum = 0
    nSpcChar = 0
    bIsValid = True

    # Index Check loop
    for i in sPassword :

        if i in sUpperStr :
            nUpper += 1
        if i in sLowerStr :
            nLower += 1
        if i in sNumStr :
            nNum += 1
        if i in sSpecialCharStr :
            nSpcChar += 1

    # loop result validation
    # validate if 1 uppercase
    if nUpper == 0 :
        print( "Password must contain at least 1 uppercase letter." )
        bIsValid = False
    nUpper = 0

    # validate if 1 lowercase
    if nLower == 0 :
        print( "Password must contain at least 1 lowercase letter." )
        bIsValid = False
    nLower = 0

    # validate if 1 numeric
    if nNum == 0 :
        print( "Password must contain at least 1 number. Try Again." )
        bIsValid = False
    nNum = 0

    # validate if 1 special char
    if nSpcChar == 0 :
        print( "Password must contain at least 1 of these special characters: ! @ # $ % ^." )
        bIsValid = False
    nSpcChar = 0

    if bIsValid == False :
        return True
    return False





def IsRepeatChar(sPassword):
    while True:
        sRepeat = ""
        for i in sPassword :
            count = sPassword.upper().count(i)
            if count > 1:
                if i not in sRepeat:
                    sRepeat += i

        if sRepeat != "" :
            print("These characters appears more than once: ")
            for i in sRepeat :
                count = sPassword.upper().count( i )
                if count > 1 :
                    print( f"{i}: {count} times" )
                    sRepeat = sRepeat.replace( i, "" )
            return True
        return False





def GoAgain(sPrompt) :
    sInput = input( sPrompt ).upper()

    if sInput == "Y" :
        return True
    return False





def main() :
    while True :
        # validate name input & gets NameList
        sFullName, sNameList = ValidateName( "\nEnter full name such as 'John Smith': " )

        # gets initials
        sInitials = getInitials( sNameList )

        # get and validate new password
        ValidatePassword( "Enter new password: ", sInitials )

        if GoAgain( "Would you like to restart the program? [Y / N]: " ) :
            continue
        break

main()
