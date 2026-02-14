# An event that interrupts the flow of a program
# (ZeroDivisionError, TypeError, ValueError) and not only those
# 1.try, 2.except, 3.finally


print("#################### Exception #####################")
try:
    number = int(input("Enter a number: "))
    print(1 / number)
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("You can only enter numbers!")
except Exception: # All exceptions
    print("Something went wrong! Please try again")
finally:
    print("Do some clean up")
print("####################################################")
