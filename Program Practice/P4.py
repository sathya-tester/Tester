
def validatenumber():
    requiredlength = 10
    personcontact = str(input('Enter your mobile number: '))
    numberlength = len(personcontact)
    if numberlength == requiredlength:
        print('It is valid mobile number')
    elif numberlength < requiredlength:
        missingnumber = requiredlength - numberlength
        print('your missing number is', missingnumber)
    else:
        extranumber = numberlength - requiredlength
        print('You have exceeded maximum length by', extranumber)
validatenumber()



