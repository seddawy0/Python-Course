import random
print("######################### Rock Paper Scissors Game ###########################")
# Rock Paper Scissors Game V1
########################### Logic #############################
options = ["Rock", "Paper", "Scissors"]
bot = random.choice(options)
score = 0
questions = 0
print("------------------- Rock Paper Scissors -------------------")
while True:
    guess = input("Enter a choice (Rock - Paper - Scissors) (q to quit): ")
    if guess.lower() == "q":
        break
    elif not guess.capitalize() in options:
        print(f"{guess} is not valid!")
    elif guess.capitalize() == bot:
        print("DRAW!")
        score += 1
    elif guess.capitalize() == "Rock" and bot == "Scissors" or guess.capitalize() == "Paper" and bot == "Rock" or guess.capitalize() == "Scissors" and bot == "Paper":
        score += 1
        print("You won!")
    else:
        print("You lost!")
    questions += 1
    print(f"Player: {guess.capitalize()}.")
    print(f"Computer: {bot}.")
    bot = random.choice(options)
    print(f"You got {score} out of {questions}")
print(f"Your final score is: {score} out of {questions}") 
print("------------------- Rock Paper Scissors -------------------")
###############################################################
print("##############################################################################")