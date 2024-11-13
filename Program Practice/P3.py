# age = 17
# weight = 60
# def ifelse():
#     if age > 18:
#         print('he is eligible')
#     else:
#         print('Not eligible')


# Selection
# def nestedIf()

def elifcondition():
    productprice = 100
    customerprice = int(input('Enter your amount'))
    if productprice == customerprice:
        print ('Product Deliver')
    elif customerprice < productprice:
        difference = productprice - customerprice
        print ('Complete pending payment', difference)
    else:
        payableamount = customerprice - productprice
        print ('collect your balance', payableamount)
        print('collect your product')
elifcondition()