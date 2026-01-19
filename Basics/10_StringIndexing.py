# Accessing elements of a sequence using [] 
#                                          [start : end : step]
#                                          start is inclusive. end is exclusive.

print("################### String Indexing ####################")
creditCard = "1234-5678-9012-3456"
print(creditCard[0])
print("-------------")
print(creditCard[5:9])
print("-------------")
print(creditCard[:4])
print("-------------")
print(creditCard[10:])
print("-------------")
print(creditCard[-2])
print("-------------")
print(creditCard[::3])
print("-------------")
print(creditCard[::-1])
print("-------------")
print()
print("----Last Digits----")
lastDigits = creditCard[-4:]
print(f"XXXX-XXXX-XXXX-{lastDigits}")
print("-------------------")
print("########################################################")
