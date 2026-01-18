print("######################### Calculator ###########################")
# Calculator v1
num1 = float(input("Enter the 1st number: "))
operator = input("Enter an operator (+ - * /): ")
num2 = float(input("Enter the 2nd number: "))
print("------------------------------")
if operator == "+":
    result = num1 + num2
    print(round(result, 2))
elif operator == "-":
    result = num1 - num2
    print(round(result, 2))
elif operator == "*":
    result = num1 * num2
    print(round(result, 2))
elif operator == "/":
    result = num1 / num2
    print(round(result, 2))
else:
    print(f"{operator} is NOT a valid operator!")
print("################################################################")
