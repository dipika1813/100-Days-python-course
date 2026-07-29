countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")   #add item
temp.pop(3)             #remove item
temp[2] = "Finland"     #change item
countries = tuple(temp)
print(countries)


#Concatanate two tuples:
countries = ("India", "Italy", "Thailand", "Veitnam")
countries2 = ("China", "Finland", "Scotland")
tup = countries + countries2
print(tup)

#count the number
tup = (2, 3, 4, 1, 5, 6, 5, 4)
res = tup.count(4)
print('Count of 3 in tuple is:', res)


#index()method
tup = (2, 3, 4, 1, 5, 6, 5, 4, 7, 4)
res = tup.index(4, 5, 9)
print(res)
print(len(tup))
