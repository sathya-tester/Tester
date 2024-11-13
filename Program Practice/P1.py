# count=int(input('Starts'))
# maxMarks=int(input('Ends'))

# while count>=maxMarks:
#     marks = int(input('Enter your mark'))
#
#
#     if marks >= 95 and marks <= 100:
#         print('A+')
#     elif marks >= 85 and marks <= 94:
#         print('A')
#     count+=1

num1=5
num2=2
# 2<5 --> true
print(not num2<num1)

employee=['Muthu','jeeva','Raju','Praveen','Muthu']
lst1='greens'
lst2='Greens'

print(employee)

for i in employee:
    if i._eq_('Muthu'):
         print(i)

res=lst2 is not lst1
print(res)