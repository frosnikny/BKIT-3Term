import types
import pytest


def fibonacci_numbers(n: int):
    if (n <= 0):
        raise ValueError(
            "The number of Fibonacci numbers must be greater than 0")
    a = 0
    b = 1
    for _ in range(0, n):
        yield a
        a, b = b, a + b


class TestFibonacci:
    def test_numbers(self):
        a = [i for i in fibonacci_numbers(15)]
        b = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
        assert a == b

    def test_error(self):
        a = fibonacci_numbers(-1)
        with pytest.raises(ValueError):
            for i in a:
                i += 1

    def test_generator(self):
        a = fibonacci_numbers(3)
        assert isinstance(a, types.GeneratorType)
