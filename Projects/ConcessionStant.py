print("######################### Concession Stand Program ###########################")
# Concession Stand Program
########################### Logic #############################
menu = {" Food ":  {"Hotdog" : 3,
                    "Natchos" : 3,
                    "Pizza slice" : 2.5},
        "Snacks": {"Popcorn": 1.5,
                   "Chips": 2,
                   "Icecream" : 2},
        "Drinks": {"Water" : 1,
                   "Soda" : 2,
                   "Coffee" : 2.5}}
cart = []
total = 0
print("========== MENU ==========")
for group, items in menu.items(): # Group means keys (Food, Snacks, Drinks), Items means dictionary
    print(f"---------- {group} ----------")
    for food, price in items.items():
        print(f"{food:11}: ${price:.2f}")
print("==========================")

while True:
    clientItem = input("Select an item (q to quit): ").lower()
    if clientItem == "q":
        break
    for category in menu.values():
        if clientItem.capitalize() in category:
            cart.append((clientItem.capitalize(), category[clientItem.capitalize()]))
            total += category[clientItem.capitalize()]
            print(f"Added {clientItem.capitalize()} to your cart.")
            break
    else:
        print("Sorry, we don't have that item.")
print("========== Your Recipt ==========")
for item, price in cart:
    print(f"{item:11}: ${price:.2f}")
print("=================================")
print(f"Total      : ${total:.2f}")
###############################################################
print("##############################################################################")