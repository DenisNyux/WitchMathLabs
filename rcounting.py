"""
В модуле содержатся функции для подсчета остаточных членов
"""
import math


def diff(x):
    return x * (12 * x**2 - 3 * x + 4)


def second_diff(x):
    return 36 * x**2 - 6 * x + 4


def fourth_diff(x):
    return 72


def max_diff(args, func):
    i = args[0]
    res = []
    while args[1] >= i:
        res.append(func(i))
        i += 0.001
    return abs(max(res))


def r_rectangle(args):
    return max_diff(args, diff)*(args[1] - args[0])**2 / (2 * args[2])


def r_trapeze(args):
    return max_diff(args, second_diff)*(args[1] - args[0])**3 / (12 * args[2]**2)


def r_parabola(args):
    return max_diff(args, fourth_diff)*(args[1] - args[0])**5 / (180 * (2 * args[2])**2)
