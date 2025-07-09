def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error Cannot divide by zero."
print(divide(5,8))