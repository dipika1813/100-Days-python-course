# using 'f' you can acccess value of name or country 

letter = "Hey my name is {} and I am from {} "
country = "India"
name = "Harry"

print(letter.format(name,country))
# print(letter.format (country , name))  - then name{1} from {0}4

print(f"Hey my name is {name} and I am from {country} ")

price = 49.99
txt = f"for only {price:2f} dollars!"
print(txt)

print(type(f"{2*39}"))