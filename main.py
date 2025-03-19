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

def simple(n):
    try:
        n = int(n)
        if n <= 1:
            return False
        if n == 2 or n == 3:
            return True
        if n % 2 == 0:
            return False
     
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    except (TypeError, ValueError):
        return False

print(simple(2))
print(simple(3))   
print(simple(4))   
print(simple(17)) 
print(simple(20)) 
print(simple("abc"))
print(simple(2.5))


def unique_elements(data):
    try:
        return list(set(data))
    except TypeError:
        return "Входные данные должны быть повторяемыми"
