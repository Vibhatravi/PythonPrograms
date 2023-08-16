class InvalidValueError(Exception):
    pass


def calculate_square_root(num):
    assert num >= 0, "Input must be a non-negative number"
    return num ** 0.5

while True:
    try:
        n = float(input("Enter the Number to find its square root: "))
        result = calculate_square_root(n)
        print(result)
    except InvalidValueError as e:
        print("An error occurred:", str(e))
