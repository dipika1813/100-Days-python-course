x = int(input("enter a number:"))

match x:
    case 0:
        print("x is zero.")
    
    case 1:
        print("x is one.")

    case 5:
        print("x is five.")

    case _ if(x != 90):
        print(x, "is not 90")

    case _  if(x != 80):
        print(x, " is not 80")
    
    