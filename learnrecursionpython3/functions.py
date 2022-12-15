# pylint: disable=missing-docstring

def sum_to_one_iterative(number):
    # function that replicates what happens in a callstack during recursion
    result = 1
    call_stack = []
    while number != 1:
        execution_context = {"number_value": number}
        call_stack.append(execution_context)
        number -= 1
        print(call_stack)
    print("BASE CASE REACHED")
    while len(call_stack) != 0:
        return_value = call_stack.pop()
        result += return_value["number_value"]
        print(call_stack)
    return result, call_stack


def sum_to_one_recursion(number):
    if number == 1:
        return number
    print(f"Recursing with input: {number}")
    return number + sum_to_one_recursion(number - 1)


def factorial(number):
    # Base case, if the number is less than 2 just return it
    if number < 2:
        return number
    # return the current input number times the result of return value of factorial() with number -1
    return number * factorial(number-1)


print(factorial(12))
# sum_to_one_recursion(7)
