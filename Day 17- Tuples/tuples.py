# Tuples cannot be modified once it created

t = (1,) #have to use , if you use only one element in tuple


tup = ('dipika', 34, 54 ,21)
print(tup)
print(type(tup))
print(tup[2])

tup[3] = 45
print(tup)