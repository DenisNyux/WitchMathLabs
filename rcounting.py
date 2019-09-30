from formulas import func


def diff(x: float) -> float:
    accuracy = 0.1e-6
    x1 = x - accuracy
    x2 = x + accuracy
    y1 = func(x1)
    y2 = func(x2)
    return (y2 - y1) / (x1 - x2)


print(diff(5))
