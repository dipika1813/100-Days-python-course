#program to write good morning as per time 

# import time
# present_time = time.strftime('%H: %T: %S')
# present_time = int(time.strftime('%H'))

# if(4<= present_time<= 12):
#     print("good morning")

# elif(12>= present_time<= 5):
#     print("Good Afternoon sir")

# elif(5>= present_time<= 8):
#     print("good evening sir")

# else:
#     print("good night sir")


import time

name = input("Enter your name : ")
name = name.capitalize()
present_time = time.strftime("%H:%M:%S")
hour = int(time.strftime("%H"))
hour = int(input("enter hour"))

if (hour >0 and  hour < 12):
    print(f"Good morning {name}")
    print("Thanku sir ")

elif (hour > 12 and hour < 17):
    print(f"Good Afternoon {name}")
    print("Thanku sir ")

elif (hour >= 17 and hour < 0):
    print(f" Good Night  {name}")
    print("Thanku sir ")



