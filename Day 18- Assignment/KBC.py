# Create a program capable of displaying questions to the user like KBC
# use list data type to store the que and ans 
# display the final amount after Win

Questions = [["1. Which Country has the great Wall?",
             "options :" 'A: China', 
             "B: India", 
             "C: Italy", 
             "D: France",
             "ANS: A", 1000],

            ["2: Which Country is the home to Pyramids?",
             "options:" "A :India", 
             "B: Egypt", 
             "C: Greece", 
             "D:Mexico",
             "ANS: B", 2000],

            ["3: Which planet is known for Red Planet?",
             "options:" "A: Earth", 
             "B: Jupiter", 
             "C: Mars", 
             "venus",
             "ANS: C", 3000],

             ["4: Which is the largest ocean in the world?",
             "options:" "A: pacific ocean", 
             "B: Artic ocean", 
             "C:Indian ocean", 
             "D:Atlantic ocean",
             "ANS: A", 4000],

             ["5: Which country is famous for chocholates?",
             "options:" "A: India",
               "B: Switzerland", 
               "C: Russia", 
               "D: Turkey",
             "ANS: B", 5000]
]
amount = 0
for i in range(len(Questions)):
    print("Que is:", i + 1)
    print(Questions[i][0])
    print(Questions[i][1])
    print(Questions[i][2])
    print(Questions[i][3])
    print(Questions[i][4])

    user_ans = input("enter your ans :(A/B/C/D):").upper()
    if(user_ans == Questions[i][5]):
        print("Correct Ans")
        amount = Questions[i][6]

    else:
        print("Wrong Ans")
        
       

print("You Won", amount)




