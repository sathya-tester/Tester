from abc import ABC

class ATM (ABC):
    def totalAmount(self):
        pass

    def customerInfo(self):
        print('Choose your Mode')
        print('Withdraw')
        print('Deposit')
ATM().totalAmount()
ATM().customerInfo()
class RBI(ATM):
    def totalAmount(self):
        print(100000)
RBI().totalAmount()