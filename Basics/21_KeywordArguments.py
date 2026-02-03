# An argument preceded by an indentifier
# Helps with readability
# Order of arguments doesn't matter
print("#################### Keyword Arguments #####################")
# Examples
print("-------------------- Example 1 ---------------------")
def hello(greeting, title, firstName, lastName):
    print(f"{greeting} {title}{firstName} {lastName}!")
hello("Hello", "Mr.", lastName="El-Sedawy", firstName="Ziad")
print("-------------------- Example 1 ---------------------")
print()
print("-------------------- Example 2 ---------------------")
def phoneNum(countryCode, areaCode, first, last):
    print(f"+{countryCode}-{areaCode}-{first}-{last}")
phoneNum(countryCode = 20, areaCode = 10, first = 6862, last = 2188)
print("-------------------- Example 2 ---------------------")
print("############################################################")