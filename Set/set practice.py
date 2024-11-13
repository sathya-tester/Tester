country = {'india','uk','canada','us','australia'}
website = ['fb', 'instagram', 'snapchat', 'twitter', 'google']
print(type(country))
print(type(website))
dummy=1
print(type(dummy))
test=0.1
print(type(test))
test= True
print(type(test))
check = 'king', 'queen'
print(type(check))
print (check)
check1 = {'dollar':123}
print(type(check1))
print (check1)

website[1]='china'
print(website)
website.remove('twitter')
print(website)
print (len(website))
index = website.index('china')
print(index)


country=['India','Japan','China','America','India','Malaysia']
#         0      1          2           3       4
website=['fb','insta','tiktok','snapchat','youtube','amazon']

print(len(country))


# print(len(country))

#  How to find Index?
#  Index=length-1
#  index=5-1 = 4
#  index starts from 0 to index value


returnValue=country.count('Japan')
print(returnValue)

#  It will used to remove the value from a list using index
removeVal=country.pop(2)
print(removeVal)
print(country)


# It will remove the value from a list
country.remove('Japan')
print(country)

country.clear()
#  It will insert the new data in a exisiting list
country.append('UK')
print(country)

#  insert the value based on index range
country.insert(1,'Australia')
print(country)

#  Ascending Order
country.sort()
print(country)

country.reverse()
print(country)



duplCopy=country.copy()
print(duplCopy)

country.extend(website)
print(country)

country[0]='Netherland'
print(country)