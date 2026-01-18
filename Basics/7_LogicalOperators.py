# Evaluate multiple conditions (or, and, not)

print("################### OR ####################")
# At least one condition must be true
temp = 30
is_raining = True
if temp > 30 or temp < 0 or is_raining:
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is still scheduled")
print("###########################################")
print()
print("################### AND ####################")
# All conditions must be true
temp = 0
is_sunny = True
if temp >= 35 and is_sunny:
    print("It is HOT outside 🥵")
    print("It is SUNNY ☀️")
elif 35 >= temp >= 5 and is_sunny:
    print("It is WARM outside 😊")
    print("It is SUNNY ☀️")
elif temp <= 4 and is_sunny:
    print("It is COLD outside 🥶")
    print("It is SUNNY ☀️")
print("############################################")
print()
print("################### NOT ####################")
# Inverts the condition (Not False, Not True)
if temp >= 35 and not is_sunny:
    print("It is HOT outside 🥵")
    print("It is CLOUDY ☁️")
elif 35 >= temp >= 5 and not is_sunny:
    print("It is WARM outside 😊")
    print("It is CLOUDY ☁️")
else:
    print("It is COLD outside 🥶")
    print("It is CLOUDY ☁️")
print("############################################")