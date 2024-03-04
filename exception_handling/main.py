def divide_by(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 0

print(divide_by(40, 0))
