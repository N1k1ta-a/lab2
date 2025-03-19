import pytest
import main

def test_is_factorial():
    assert main.factorial(0) == 1

    assert main.factorial(1) == 1

    assert main.factorial(5) == 120

    assert main.factorial(10) == 3628800

    assert main.factorial(-5) == "нету ориц факт"

    with pytest.raises(TypeError):
        main.factorial(5.5)

    with pytest.raises(TypeError):
        main.factorial("abc")

    with pytest.raises(TypeError):
        main.factorial(None)

    assert main.factorial(2) == 2


def test_is_simple():
    assert main.simple(-1) == False

    assert main.simple(0) == False

    assert main.simple(1) == False

    assert main.simple(2) == True

    assert main.simple(3) == True

    assert main.simple(7919) == True

    assert main.simple(7920) == False

    assert main.simple("abc") == False

    assert main.simple(7.5) == False

    assert main.simple(None) == False


def test_is_unique_elements():
    assert main.unique_elements([1, 2, 2, 3, 4, 4, 5]) == [1, 2, 3, 4, 5]

    assert main.unique_elements((1, 2, 2, 3, 4, 4, 5)) == [1, 2, 3, 4, 5]

    assert main.unique_elements("hello") == ['h', 'e', 'l', 'o']

    assert main.unique_elements([]) == []

    assert main.unique_elements([42]) == [42]

    assert main.unique_elements(42) == "Входные данные должны быть повторяемыми"

    assert main.unique_elements(3.14) == "Входные данные должны быть повторяемыми"

    assert main.unique_elements(None) == "Входные данные должны быть повторяемыми"

    assert main.unique_elements([1, 1, 1, 1]) == [1]

    assert main.unique_elements([1, "1", 1.0, "1"]) == [1, "1", 1.0]


