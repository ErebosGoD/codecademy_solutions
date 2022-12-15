# pylint: disable=missing-docstring
def fibonacci(number):
    if number == 1 or number == 0:
        return number
    print(f"Recursive call with {number} as input")
    return fibonacci(number - 1) + fibonacci(number - 2)


fibonacci(5)
