# Slot Machine V1
########################### Logic #############################
from random import choices
from time import sleep
def balanceSystem(currentBalance):
    print(f"Current balance: ${currentBalance:.2f}")
    betAmount = int(input("Enter your bet amount: $"))
    while betAmount > currentBalance:
        print(f"You only have ${currentBalance:.2f}")
        betAmount = int(input("Enter your bet amount: $"))
    return currentBalance, betAmount

def spinningSystem():
    symbols = ("🍒", "🍋", "🍉", "⭐", "🔔")
    slotMachine = choices(symbols ,k=3)
    print("Spinning........")
    sleep(2)
    print()
    print("***************")
    print(" |".join(f" {symbol}" for symbol in slotMachine)) # join() was a new func for me
    print("***************")
    return slotMachine

def slotmachineSystem():
    currentBalance = 100
    while True:
        print("*********************************")
        currentBalance, betAmount = balanceSystem(currentBalance)
        slotMachine = spinningSystem()
        match slotMachine:
            case ("🍒", "🍒", "🍒") | ("🍋", "🍋", "🍋") |("🍉", "🍉", "🍉") |("⭐", "⭐", "⭐") |("🔔", "🔔", "🔔"):
                     currentBalance -= betAmount
                     winBalance = 10 * betAmount
                     currentBalance += winBalance
                     print(f"YOU WON ${winBalance}!!!!")
            case _:
                print(f"Sorry, You lost this round!")
                currentBalance -= betAmount
        spinLoop = input("Do you want to spin again? (Y/N): ").upper()
        if spinLoop == "N":
            print(f"Game over! Your final balance is {currentBalance}")
            break
        
###############################################################
if __name__ == "__main__":
    
    print("*********************************")
    print("           Slot Machine          ")
    print("*********************************")
    print("Welcome to the slot machine 🎰")
    print("Symbols: 🍒 🍋 🍉 ⭐ 🔔")
    slotmachineSystem()
    print("*********************************")
