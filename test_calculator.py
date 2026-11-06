import pytest
from calculator import add, divide, calculate_discount


def test_add():
    assert add(2, 3) == 5


def test_calculate_discount():
    # A $100 item with 20% discount should cost $80, but returns $120 due to bug
    final_price = calculate_discount(100.0, 20.0)
    assert final_price == 80.0
