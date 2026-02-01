import random
print("######################### Number Guessing ###########################")
# Number Guessing V1
########################### Logic #############################
randomNumber = random.randint(1, 100)
score = 0
numGuesses = 0
print("------------------- Number Guessing -------------------")
while True:
    guess = input("Enter a number between 1-100 (q to quit): ")
    if guess.lower() == "q":
        break
    else:
        guess = int(guess)
        numGuesses += 1
    if guess == randomNumber:
        print(f"CORRECT! The answer was {randomNumber}")
        score += 1
        randomNumber = random.randint(1, 100)
        numGuesses = 0
        # print(f"Number of guesses: {numGuesses}. Your score is: {score}") # I don't need it here
    elif guess < randomNumber:
        print(f"{guess} is too low. Try Again!")
        # print(f"Number of guesses: {numGuesses}. Your score is: {score}") # I don't need it here
    else:
        print(f"{guess} is too high. Try Again!")
        # print(f"Number of guesses: {numGuesses}. Your score is: {score}") # I don't need it here

    print(f"Number of guesses: {numGuesses}. Your score is: {score}") # Only one time
print(f"Your final score is: {score}") 
print("------------------- Number Guessing -------------------")
###############################################################
print("#####################################################################")