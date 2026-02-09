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
               "/|\\"
               "/  "),
           5: (" O ",
               "/|\\",
               "/ \\")}



###############################################################
if __name__ == "__main__":
    print("***********************************************")
    print("                  Hangman Game                 ")
    print("***********************************************")
