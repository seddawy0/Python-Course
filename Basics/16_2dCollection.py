# A collection or more inside another collection (Container)
print("#################### 2D Collection #####################")
groceries = [["Apple", "Banana", "Orange", "Strawberry", "Mango"],
             ["Tomato", "Carrot", "Onion", "Celery"],
             ["Meat", "Chicken", "Fish", "Turkey"]]

print(groceries)
print(groceries[0])
print(groceries[1][2])
print("-------------------------------------")
for collection in groceries: # To print all collections
    print(collection)
print("-------------------------------------")
for collection in groceries: 
    for food in collection: # To print every element inside every collection
        print(food, end=" ")
    print()
print("-------------------------------------")
print()
print("------------- Exercise --------------")
numPad = ((1, 2, 3),
          (4, 5, 6),
          (7, 8, 9),
          ("*", 0, "#"))
for row in numPad:
    for num in row:
        print(num, end=" ")
    print()
print("########################################################")