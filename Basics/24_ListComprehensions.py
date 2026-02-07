# A concise way to create lists
#   Compact & Easier to read than traditional loops
#   [expression for value in iterable if condotion]
print("#################### List Comprehensions #####################")
# Examples
print("-------------------- Example 1 ---------------------")
# doubles = []
# for x in range(1, 11):
#     doubles.append(x * 2)
# print(doubles)
doubles = [x * 2 for x in range(1, 11)]
print(doubles)
triples = [y * 3 for y in range(1, 11)]
print(triples)
squares = [z * z for z in range(1, 11)]
print(squares)
print("-------------------- Example 1 ---------------------")
print()
print("-------------------- Example 2 ---------------------")
numbers = [1, -2, 3, -4, 5, 6, -7, 8, -9, 10]
positiveNums = [num for num in numbers if num >= 0]
print(positiveNums)
negativeNums = [num for num in numbers if num < 0]
print(negativeNums)
evenNums = [num for num in numbers if num % 2 == 0]
print(evenNums)
oddNums = [num for num in numbers if num % 2 == 1]
print(oddNums)
print("-------------------- Example 2 ---------------------")
print()
print("-------------------- Example 3 ---------------------")
grades = [86, 50, 30, 70, 76, 92, 55, 62, 71]
passGrades = [grade for grade in grades if grade >= 60]
print(passGrades)
print("-------------------- Example 3 ---------------------")
print("##############################################################")