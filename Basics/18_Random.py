import random
print("#################### Random #####################")
print(random.randint(1,10)) # Random integer
print(random.random()) # Random Float betweem 0 - 1
print("-----------------------------------")
options = ("Rock", "Paper", "Scissors")
print(random.choice(options)) # Random Choice From Options You Write
print("-----------------------------------")
cards = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "K", "Q", "A"]
random.shuffle(cards) # Suffle before print to prevent None
print(cards) 
print("##################################################")