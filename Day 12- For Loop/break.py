# break Statement - terminate the loop after break 
 
i = 0
while(i <= 5):
    if i == 3:
        break #terminate
    else:
        print(i)
    i += 1


# continue statement - terminate the current iteration & continue execution

i = 0
while(i <= 5):
    if i == 3:
        # i += 1
        continue #skip
    print(i)
    i += 1  