print("######################### Shopping Cart Program ###########################")
# Shopping Cart v1
foods = []
prices = []
total = 0
########################### Logic #############################
while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == "q":
        break
    else:
        foods.append(food)
        price = float(input(f"Enter the price of the {food}: $"))
        prices.append(price)
        total += price
print("------------------------------------------------")
print("---------- Cart ----------")
for i in range(len(prices)):
    print(f"{foods[i]}: ${prices[i]:.2f}")
print("---------- Total ----------")
print(f"Total: ${total:.2f}")
###############################################################

print("###########################################################################")