print("######################### Pharmacy System ###########################")
# Pharmacy System
########################### Logic #############################
pharmacyInventory = {
                     "Painkillers": {
                                     "Panadol": {"price": 10, "stock": 15},
                                     "Advil": {"price": 15, "stock": 20},
                                     "Brufen": {"price": 10, "stock": 15},
                                     "Aspirin": {"price": 6, "stock": 50}},
                     "Antibiotics": {
                                     "Augmentin": {"price": 30, "stock": 10},
                                     "Zithromax": {"price": 30, "stock": 10},
                                     "Amoxil": {"price": 12, "stock": 5},
                                     "Flumox": {"price": 15, "stock": 10}},
                     "Skincare":    {
                                     "Sunblock": {"price": 5, "stock": 4},
                                     "Moisturizer": {"price": 25, "stock": 5},
                                     "Cleanser": {"price": 30, "stock": 10},
                                     "Serum": {"price": 16, "stock": 18}}
                    }
cart = []
total = 0
print("=============== Pharmacy Inventory ===============")
for category, drugs in pharmacyInventory.items():
    print(f"--------------- {category} ---------------")
    for drugName, drugInfo in drugs.items():
        print(f"{drugName:11} | Price: ${drugInfo["price"]:5.2f} | Stock: {drugInfo["stock"]}") # New Idea
print("==================================================")
while True: # I need to be confident in this
    drug = input("Select a drug to buy (q to quit): ")
    if drug.lower() == "q":
        break
    for drugs in pharmacyInventory.values():
        if drug.capitalize() in drugs:
            quantity = int(input(f"Enter the quantity of the {drug} to buy: "))
            while quantity > drugs[drug.capitalize()]["stock"]:
                print(f"Only {drugs[drug.capitalize()]["stock"]} left!")
                quantity = int(input(f"Enter the quantity of the {drug} to buy: "))
            price = drugs[drug.capitalize()]["price"]
            total += drugs[drug.capitalize()]["price"] * quantity
            drugs[drug.capitalize()]["stock"] -= quantity
            cart.append((drug.capitalize(), price, quantity)) # Only Tuples
            print(f"Added {quantity} of {drug.capitalize()} to the cart.")
            break
    else:
        print(f"Drug ({drug.capitalize()}) not found!")
###############################################################
print("#####################################################################")