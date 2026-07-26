l = [1,2,7,6,2]
print(l)
l.append(8)  #adds the element
print(l)

l.sort()  #assending order
print(l)

l.sort(reverse=True)  #decending order
print(l)

l.reverse()  #reverse the list
print(l)

print(l.index(2))  #give index of value 2

print(l.count(2)) #how many times repeted

# m = l.copy()
# m[0] = 0
# print(l)



l.insert(1, 87)
print(l)

m = [900, 1000, 2112]  
l.extend(m)  # m inserted at the end of l 
print(l)

#OR
m = [900, 1000, 2112]  
k = l + m
print(k)
