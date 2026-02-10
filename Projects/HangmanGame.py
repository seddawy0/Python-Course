# Hangman Game
########################### Logic #############################
import random
secretWords = ["Python", "Software", "Program", "Computer", "Algorithm",
               "Database", "Pharmacy", "Hospital", "Developer", "Internet",
               "Keyboard", "Monitor", "Language", "Variable", "Function",
               "Butterfly", "Galaxy", "Mystery", "Network", "Security"]
dashes = []
hangManArt = {
            0: ("   ",
               "   ",
               "   "),
            1: (" O ",
               "   ",
               "   "),
           2: (" O ",
               "/| ",
               "   "),
           3: (" O ",
               "/|\\",
               "   "),
           4: (" O ",
               "/|\\",
               "/  "),
           5: (" O ",
               "/|\\",
               "/ \\")}

def main():
    loser = 0
    secretWord = random.choice(secretWords).upper()
    dashes = ["_" for char in secretWord]
    while True:
        print("***********************************************")
        userAnswer = input("Enter a letter: ").upper()
        if not len(userAnswer) == 1:
            print("*************************************")
            print("You can't enter more than one letter!")
            continue
        if loser >= 4:
            for row in hangManArt[5]:
                print(row)
            print("Game over! You lost")
            break
        elif userAnswer not in secretWord:
            loser += 1
            for row in hangManArt[loser]:
                print(row)
        else:
            for row in hangManArt[loser]:
                print(row)
        for i in range(len(secretWord)):
            # if userAnswer in secretWord:
            #     dashIndex = secretWord.index(userAnswer) # index() used for only the first index of the char not all 
            #     dashes[dashIndex] = userAnswer
            if secretWord[i] == userAnswer: # This will check for every letter in the secretWord 
                dashes[i] = userAnswer # This will replace the dashes with the right letter
        if "_" not in dashes:
            print("You won! Congratulations.")
            print(f"The word was: {secretWord}")
            break
        # dashes = ("".join(dash for dash in dashes))  It will make the list a string !
        print(" ".join(dash for dash in dashes))  #     I need to do it only on the print

###############################################################
if __name__ == "__main__":
    print("***********************************************")
    print("                  Hangman Game                 ")
    main()
    print("***********************************************")
