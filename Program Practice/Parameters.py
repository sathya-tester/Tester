# *args --> tuple
# **kwargs --> dict

def addition(num1,**num2):

    print(num1)
    print(num2)

addition(num1=10, n=10,b=20)

def addition(num3,*num4):
    for i in num4:
        print()

    print(num3)
    print(num4)

addition(10, 2, 7)