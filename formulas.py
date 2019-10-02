import math


def func(x):
    return 3 * x**4 - x**3 + 2 * x**2 + 5


def rectangle_right(args: list) -> float:
    h = (args[1]-args[0])/args[2]
    i = args[0]+h
    res = 0
    while i <= args[1]:
        res += h * func(i)
        i += h
    return res


def rectangle_left(args: list) -> float:
    h = (args[1]-args[0])/args[2]
    i = args[0]
    res = 0
    while i <= args[1]-h:
        res += h * func(i)
        i += h
    return res


def trapeze(args: list) -> float:
    h = (args[1]-args[0])/args[2]
    i = args[0] + h
    res = 0
    while i <= args[1]-h:
        res += func(i)
        i += h
    res += (func(args[0]) + func(args[1]))/2
    res *= h
    return res


def parabola(args: list) -> float:
    h = (args[1] - args[0]) / args[2]
    i = args[0] + h
    odd = 0
    even = 0
    while i <= args[1] - h:
        odd += func(i)
        i += 2 * h
    i = args[0] + 2 * h
    while i <= args[1] - 2 * h:
        even += func(i)
        i += 2 * h
    res = h / 3 * (func(args[0]) + func(args[1]) + 4 * odd + 2 * even)
    return res


"""
def double_recount(args_var):
    
"""
