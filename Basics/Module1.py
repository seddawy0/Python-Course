# if __name__ == "__main__" : this script can be imported or run standalone
# Functions and classes in this module can be reused without the main block of code executing
# Good in modular, helps readability, leaves no global variables, avoid unintended execution
# Ex. library = import library for functionality
#     When running library directly, display a help page

print("This is module 1")   # A GLOBAL THING

def add(*args):
    total = 0
    for num in args:
        total += num
    return total

def mul(*args):
    total = 1
    for num in args:
        total *= num
    return total

def sub(first, *args):
    total = 0
    for num in args:
        total += num
    return first - total

def divide(first, *args):
    total = 1
    for num in args:
        total *= num
    return first / total
    
def main(): 
    print("This is module 1")
    print(add(5, 5, 5, 5))
    print(sub(100, 60, 10, -10))
    print(mul(5, 5, 2, 2))
    print(divide(100, 2, 5, 2))

if __name__ == "__main__": # If I run this module directly, it will make __name__ == __main__, so it will do any thing in func main()
                           # But if I imported this module 1 to module 2,it will make __name__ == Module1,
                                                                             # so anything in main() won't read
    main()