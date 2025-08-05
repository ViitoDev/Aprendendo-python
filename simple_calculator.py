def addition (a,b):
    return a + b

def subtraction (a,b):
    return a - b

def multiplication (a,b):
    return a * b

def division (a,b):
    if b == 0:
        return "Error, can't be divided per 0"
    return a / b

print("-=-=(Simple calculator)=-=-")
print("choose the operation:")
print("1. Addition")
print("2. Subtraction")
print("3. multiplication")
print("4. division")

operation = input("Type the number of you operarion: ")
a = int(input("Type your first number: "))
b = int(input("Type your second number: "))

if operation == "1":
    result = addition(a,b)

elif operation == "2":
    result = subtraction(a,b)

elif operation == "3":
    result = multiplication(a,b)

elif operation == "4":
    result = division(a,b)

else:
    result = "Invalid operation"

print("Result: ", result)