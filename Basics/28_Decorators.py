# A function that extends the behavior of another function
# w/o modifying the base function
# Pass the base function as an argument to the decorator


print("#################### Decorators #####################")
def add_sprinkles(func): # func is an argument for the base function
    def wrapper(*args, **kwargs): # We added this internal function to only start the code when we start the base function only
        print("*You added sprinkles 🧁*")
        func(*args, **kwargs) # We added the *args, **kwargs to accept any argument from the base function without error
    return wrapper
def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("*You added fudge 🍫*")
        func(*args, **kwargs)
    return wrapper

@add_sprinkles
@add_fudge
def get_icecream(flavor):
    print(f"Here is your {flavor} icecream 🍨")

get_icecream("chocolate")
print("#####################################################")