# An alternative to using many 'elif' statements
#   Execute some code if a value matches a 'case'
#   Cleaner & Syntax is more readable
print("#################### Match-Case Statement #####################")
# Examples
print("-------------------- Example 1 ---------------------")
def dayOfWeek(day):
    match day:
        case 1:
            return "It's Sunday"
        case 2:
            return "It's Monday"
        case 3:
            return "It's Tuesday"
        case 4:
            return "It's Wednesday"
        case 5:
            return "It's Thursday"
        case 6:
            return "It's Friday"
        case 7:
            return "It's Saturday"
        case _: # same like else statement
            return f"{day} is not a day!"
print(dayOfWeek(2))
print(dayOfWeek(7))
print(dayOfWeek("Pizza"))
print("-------------------- Example 1 ---------------------")
print()
print("-------------------- Example 2 ---------------------")
def isWeekend(day):
    match day:
        case "Saturday" | "Friday":
            return True
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday":
            return False
        case _: # same like else statement
            return f"{day} is not a day!"
print(isWeekend("Saturday"))
print(isWeekend("Monday"))
print(isWeekend("Pizza"))
print("-------------------- Example 2 ---------------------")
print("###############################################################")