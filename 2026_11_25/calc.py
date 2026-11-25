def divide(a: float, b: float) -> float:
    """Return a divided by b, raising ValueError if b is zero."""
    if b == 0:
        raise ValueError("除數不可為零")
    return a / b
