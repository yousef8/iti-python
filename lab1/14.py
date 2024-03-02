def factorial(num):
    if not isinstance(num, int):
        return "Not a Number"

    if num < 0:
        return "No factorial for negative numbers"
    factorial = 1
    if num <= 1:
        return factorial

    for i in range(1, num + 1):
        factorial *= i

    return factorial


print(factorial(7))
