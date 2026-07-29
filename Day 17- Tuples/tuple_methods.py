countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")   #add item
temp.pop(3)             #remove item
temp[2] = "Finland"     #change item
countries = tuple(temp)
print(countries)


countries = ("India", "Italy", "Thailand", "Veitnam")
countries2 = ("China", "Finland", "Scotland")
tup = countries + countries2
print(tup)