import pytest
from app.calculator import add, subtract, multiply, divide, calculate


class TestBasicOperations:
    def test_add(self):
        assert add(2, 3) == 5

    def test_add_negative(self):
        assert add(-1, 1) == 0

    def test_subtract(self):
        assert subtract(10, 4) == 6

    def test_multiply(self):
        assert multiply(3, 4) == 12

    def test_divide(self):
        assert divide(10, 4) == 2.5

    def test_divide_by_zero(self):
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(10, 0)


class TestCalculate:
    def test_calculate_add(self):
        assert calculate("add", 1, 2) == 3

    def test_calculate_subtract(self):
        assert calculate("subtract", 5, 3) == 2

    def test_calculate_multiply(self):
        assert calculate("multiply", 2, 3) == 6

    def test_calculate_divide(self):
        assert calculate("divide", 9, 3) == 3

    def test_calculate_unknown_operation(self):
        with pytest.raises(ValueError, match="Unknown operation"):
            calculate("power", 2, 3)
