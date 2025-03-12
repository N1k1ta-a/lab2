def factorial(a):
    try:
        if a < 0:
            return ("нету ориц факт")
        if a < 2:
            return 1
        else: 
            return a * factorial(a - 1)

    except TypeError:
        print("арг должен быть числом")

print(factorial(4))
print(factorial(-1))
print(factorial("b"))

