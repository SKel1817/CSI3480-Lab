print("welcome to this lab")
print("This is a simple python program")
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"

# Test the functions
print("Addition of 5 and 3:", add(5, 3))
print("Subtraction of 5 and 3:", subtract(5, 3))
print("Multiplication of 5 and 3:", multiply(5, 3))
print("Division of 5 by 3:", divide(5, 3))
print("Division of 5 by 0:", divide(5, 0))