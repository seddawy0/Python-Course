print("######################### Quiz Game ###########################")
# Quiz Game V1
questions = ("1- Which is the longest river in the world? ",
             "2- Which planet is known as the (Red Planet)? ",
             "3- Which is the largest mammal in the world? ",
             "4- Who is credited with inventing the light bulb? ",
             "5- How many players are there in a standard soccer (football) team on the pitch?"
             )
questionAnswers = (("A- Amazon River", "B- Nile River", "C- Mississippi River", "D- Yangtze River"),
           ("A- Venus", "B- Jupiter", "C- Mars", "D- Saturn"),
           ("A- African Elephant", "B- Blue Whale", "C- Giraffe", "D- Great White Shark"),
           ("A- Nikola Tesla", "B- Alexander Graham Bell", "C- Thomas Edison", "D- Albert Einstein"),
           ("A- 9 players", "B- 10 players", "C- 11 players", "D- 12 players")
           )
answers = ("B","C","B","C","C")
score = 0
########################### Logic #############################
username = input("Enter your username: ")
while username == "":
    username = input("Enter your username: ")
print(f"Hello {username}! Welcome to quiz game")
print("------------------------------------------------")
YorN = input("Do you want to continue? (y/n): ")
while not YorN.lower() == "y":   
    YorN = input("Do you want to continue? (y/n): ")
    if YorN.lower() == "n":
        exit()
print("------------------- Quiz Game -------------------")
for i in range(len(questions)):
    print(f"------------------- {i+1} -------------------")
    print(questions[i])
    for answer in questionAnswers[i]:
        print(answer)
    userAnswer = input("Enter your Answer (A / B / C / D): ")
    if userAnswer.upper() == answers[i]:
        score += 1
        print(f"{userAnswer.upper()} is correct! Your score now is {score}")
    else:
        print(f"{userAnswer.upper()} is NOT correct! Your score is {score}")
        print(f"The correct answer was: {answers[i]}")
print(f"Your final score is: {score}")
print("------------------- Quiz Game -------------------")
###############################################################
print("###############################################################")