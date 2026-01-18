print("######################### Weight Convertor ###########################")
# Weight Convertor v1
weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds? (K / L): ")
print("--------------------------------------------")
if unit == "K":
    weight *= 2.205
    unit = "Lbs."
    print(f"Your weight is {weight}{unit}")
elif unit == "L":
    weight /= 2.205
    unit = "Kgs."
    print(f"Your weight is {weight}{unit}")
else:
    print(f"{unit} is NOT a valid unit!")
print("#####################################################################")
