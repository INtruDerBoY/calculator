def add(a: float, b: float) -> float:
    return a + b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def calculate_discount(price: float, discount_percent: float) -> float:
    # Bug: adds discount instead of subtracting it
    return price + (price * discount_percent / 100.0)
