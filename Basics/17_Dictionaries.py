# A collection of {key:value} pairs
#                 Ordered and Changeable. No Duplicates
print("#################### Dictionaries #####################")
capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}
print(capitals)
print(capitals.get("USA"), capitals.get("Russia"))
if capitals.get("Egypt"):
    print("That capital exists")
else:
    print("That capital doesn't exist")
capitals.update({"Egypt": "Cairo",
                            "Germany": "Berlin",
                            "USA": "Detroit"})
capitals.pop("China") # Remove 
print(capitals)
capitals.popitem() # Remove the last one
print(capitals)
print("-------------------------------------------------------")
keys = capitals.keys()
print(keys) # Print the Keys of the dictionary {keys} as a list
values = capitals.values() 
print(values) # Print the Values of the dictionary {values} as a list
items = capitals.items()
print(items) # Print the items of the dictionary {keys:values} as a 2d list of tuples
print("-------------------------------------------------------")
for key in capitals.keys():
    print(key)
print("-------------------------------------------------------")
for value in capitals.values():
    print(value)
print("-------------------------------------------------------")
for key, value in capitals.items():
    print(f"{key}: {value}")
print("#######################################################")