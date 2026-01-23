print("######################### Compound Interest Calculator ###########################")
######################### Variables ###########################
principle = 0
rate = 0
time = 0
###############################################################

########################### Logic #############################
while True:
    principle = float(input("Enter the principle amount: "))
    if principle < 0:
        print("Principle amount can't be less than zero!")
    else:
        break

while True:
    rate = float(input("Enter the interest rate: "))
    if rate < 0:
        print("Interest rate can't be less than zero!")
    else:
        break

while True:
    time = int(input("Enter the time in years: "))
    if time < 0:
        print("Time can't be less than zero!")
    else:
        break
   
finalAmount = principle* pow(1 + rate/100, time)
print("---------- Final Amount ----------")
print(f"Balance after {time} year/s: ${finalAmount:.2f}")
print("----------------------------------")
###############################################################

print("##################################################################################")