# A loop within another loop (outer, inner)
#                             outer loop:
#                                 inner loop:
print("################### Nested Loops ####################")
# Examples
print("----Example 1----")
for x in range(3):
    for y in range(1, 11):
        print(y, end=" ")
    print()
print("-----------------")
print()
print("----Example 2----")
rows = int(input("Enter the # of rows: "))
columns = int(input("Enter the # of columns: "))
symbol = input("Enter a symbol to use: ")
for row in range(rows):
    for column in range(columns):
        print(symbol, end="")
    print()
print("-----------------")
print("#####################################################")