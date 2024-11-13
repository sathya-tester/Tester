ticketPrice = 100
customerAge = int(input('Enter your Age: '))
if customerAge >= 18:
    print('Eligible for buying ticket')
    customerPrice = int(input('Enter your amount: '))
    if customerPrice > ticketPrice:
        print('Now select your classes')
    elif customerPrice == 100:
            print('Economy class given', economyClass)
    elif customerPrice < ticketPrice:
                returnAmount = customerPrice - ticketPrice
                print('Premium class provided', returnAmount)
    else:
        print('Not match')
else:
    print('Below 18, not eligible')

