sets={}
Setvalue=set(sets)
num=1
while num<=10:
    data=int(input('Enter your num = '))
    Setvalue.add(data)
    tot=len(sets)
    if tot==5:
        break
    num+=1
print(sets)

#add multiple users in run time, if the user comes 10 then loop will be stopped and to find duplicate user in a list
