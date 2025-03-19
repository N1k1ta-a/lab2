import pytest
import main
def test_factorial():
    assert factorial(0) == 1

    assert factorial(1) == 1

    assert factorial(5) == 120  

    assert factorial(10) == 3628800  

    assert factorial(-5) == "нету ориц факт"

    with pytest.raises(TypeError):
        factorial(5.5)  

    with pytest.raises(TypeError):
        factorial("abc")  


    with pytest.raises(TypeError):
        factorial(None)  

    assert factorial(2) == 2