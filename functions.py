# Functions in Python
def greet(name):
    print("Hello " + name + "!")

def add(num1, num2):
    result = num1 + num2
    return result

def is_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Calling functions
greet("Navin")
print(add(10, 20))
print(is_even(7))
print(is_even(4))
