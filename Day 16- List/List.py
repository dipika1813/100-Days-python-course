#lists are ordered collection of data items
l = [3, 4, 5]
print(l)
print(type(l))


marks = [89, 80, 99, "dipika"]
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])

print(marks[-3]) #negative index
print(marks[len(marks)-3])  #positive index
print(marks[4-3])   #positive index
print(marks[1])  #positive index

if "dipika" in marks:
    print('Yes')
else:
    print('No')


#same thing apply for String
# if "ika" in "dipika":
#     print("yes")


# Slicing
print(marks[1:4])
print(marks[1:4:2])