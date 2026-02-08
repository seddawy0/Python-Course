# Banking Program V1
########################### Logic #############################
def displayMenu():
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

def bankSystem():
    balance = 0
    while True:
        print("***********************************************")
        displayMenu()
        userInput = input("Enter you choice (1-4): ")
        match userInput:
            case "4":
                print("Thank you for using the Banking System 👋")
                break
            case "3":
                withdraw = float(input("Enter an amount to withdraw: "))
                if withdraw > balance:
                    print(f"You only have ${balance:.2f} in your bank account")
                else:
                    balance -= withdraw
                    print(f"You have successfully withdrawn ${withdraw:.2f} from your bank account")
            case "2":
                deposit = float(input("Enter an amount to be deposited: "))
                if deposit <= 0:
                    print("Please enter a valid amount")
                else:
                    balance += deposit
                    print(f"You have successfully deposited ${deposit:.2f} to your bank account")
            case "1":
                print(f"Your balance is: ${balance:.2f}")
            case _:
                print(f"{userInput} is not valid")
###############################################################
if __name__ == "__main__":
    print("***********************************************")
    print("                 Banking Program               ")
    bankSystem()
    print("***********************************************")
