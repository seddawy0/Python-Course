print("######################### Pharmacy System ###########################")
# Pharmacy System V2.0
########################### Logic #############################
pharmacyInventory = {
                     "Painkillers": {
                                     "Panadol Extra": {"price": 10, "stock": 15},
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

def displayInventory(inventory):
    for category, drugs in inventory.items():
        print(f"--------------- {category} ---------------")
        for drugName, drugInfo in drugs.items():
            print(f"{drugName:11} | Price: ${drugInfo['price']:5.2f} | Stock: {drugInfo['stock']}")
print("============== Pharmacy Inventory =============")
displayInventory(pharmacyInventory)
print("===============================================")
print()
def processPurchasing():
    cart = []
    total = 0
    while True: # I need to be confident in this
        drug = input("Select a drug to buy (q to quit): ")
        if drug.lower() == "q":
            break
        drug = drug.title()
        for drugs in pharmacyInventory.values():
            if drug in drugs:
                quantity = int(input(f"Enter the quantity of the {drug} to buy: "))
                while quantity > drugs[drug]["stock"]:
                    print(f"Only {drugs[drug]['stock']} left!")
                    quantity = int(input(f"Enter the quantity of the {drug} to buy: "))
                price = drugs[drug]["price"]
                total += drugs[drug]["price"] * quantity
                drugs[drug]["stock"] -= quantity
                cart.append((drug, price, quantity)) # Only Tuples
                print(f"Added {quantity} of {drug} to the cart.")
                break
        else:
            print(f"Drug ({drug}) not found!")
    return cart, total
print("===============================================")
cart, total = processPurchasing()
print("===============================================")
print()
def displayRecipt(cart, total):
    for drugName, drugPrice, drugQuantity in cart:
        print(f"{drugName:11} | Price: ${drugPrice:5.2f} | Quantity: {drugQuantity}")
    print(f"The total price is:  ${total:5.2f}")
print("=============== Pharmacy Recipt ===============")
displayRecipt(cart, total)
print("===============================================")
###############################################################
print("#####################################################################")