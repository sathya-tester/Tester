colours = {1, 2, '3'}
country = {'3', 4, 5}

# print(colours)
# print(country)
#
# country.add('Nepal')
# print(country)
#
# country.pop()
# print(country)
#
# country.remove('US')
# print(country)
#
# country.discard('Nepal')
# print(country)
#
# country.update(colours)
# print(country)
#
# country.union(colours)
# print(country)
#
# country.difference_update(colours)
# print(country)

Save = colours.symmetric_difference_update(country)
print(Save)

# colours.symmetric_difference(country)
# print(colours)