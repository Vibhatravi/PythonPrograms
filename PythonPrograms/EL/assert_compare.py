def add_numbers(a, b):
    assert isinstance(a, (int, float)), "a must be a numeric value"
    assert isinstance(b, (int, float)), "b must be a numeric value"
    return a + b


def subtract_numbers(a, b):
    assert isinstance(a, (int, float)), "a must be a numeric value"
    assert isinstance(b, (int, float)), "b must be a numeric value"
    return a - b


def multiply_numbers(a, b):
    assert isinstance(a, (int, float)), "a must be a numeric value"
    assert isinstance(b, (int, float)), "b must be a numeric value"
    return a * b


# Testing the functions

try:
    num1 = int(input("Enter the first number to perform operations: "))
    num2 = int(input("Enter the second number to perform operation: "))
    result = add_numbers(num1, num2)
    print("Addition result:", result)
except AssertionError as e:
    print("Addition Error:", str(e))

try:
    result = subtract_numbers(num1, "num2")
    print("Subtraction result:", result)
except AssertionError as e:
    print("Subtraction Error:", str(e))

try:
    result = multiply_numbers(num1 , num2)
    print("Multiplication result:", result)
except AssertionError as e:
    print("Multiplication Error:", str(e))
