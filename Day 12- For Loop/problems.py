# Q1- print num from 1 to 100
number = 1
for num in range(number, 101):
    print(num)

# OR
for i in range(1, 101):
    print(i)


# Q2- numbers from 100 to 1

for i in range(100, 0, -1):
    print(i)

#Q3- Multiplication table of n:

n = int(input("enter a num"))
for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")



#Q4 - print the list- [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

list = []
for i in range(1, 11):
    list.append(i * i)

print(list)



#Q5 - Search for a num x in tuple - [1,4,9,16,25,36,49,64,81,100]

tuple = (1,4,9,16,25,36,49,64,81,100)
x = int(input("enter value of x:"))

idx = 0
for i in tuple:
    if i == x:
        print(idx)
        break
    idx += 1
else:
    print("not found")


    




