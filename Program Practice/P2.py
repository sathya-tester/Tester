dataNumber=int(input('starts'))
dataMaximum=int(input('ends'))
dataEmployees = []
while dataNumber<=dataMaximum:
    datacount = int(input('Enter your number'))
    dataEmployees.append(datacount)
    employeeLength = len(dataEmployees)
    if dataMaximum == employeeLength:
        print('Successful')
    else:
        print('Unsuccessful')
    dataNumber+=1


    # # print your name 100 times
    #
    # def names(lst=None):
    #     if lst is None:
    #         lst = []
    #     name = 'raju'
    #     tl = len(lst)
    #     if tl < 100:
    #         lst.append(name)
    #         names(lst)
    #     return lst
    #
    #
    # datas = names()
    # print(datas)
    # print(len(datas))