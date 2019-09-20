import math
import enter


print('Введите интеграл: ')
s = input()


def rectangle_right(args: list) -> float:
    h = (args[1]-args[0])/args[2]
    i = args[0]+h
    res = 0
    while i <= args[1]:
        res += h * enter.integral(i)
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


def double_recount(args_var):
    h1 = math.sqrt(args_var[2])
    res = 0
    while abs(res):
        h2 = h1 / 2
        res1 = 0
        res2 = 0
        tmp1 = args_var[0] + h1
        while tmp1 <= args_var[1] - h1:
            res1 += func(tmp1)
            tmp1 += h1
        res1 += (func(args_var[0]) + func(args_var[1])) / 2
        res1 *= h1
        tmp2 = args_var[0] + h2
        while tmp2 <= args_var[1] - h2:
            res2 += func(tmp2)
            tmp2 += h2
        res2 += (func(args_var[0]) + func(args_var[1])) / 2
        res2 *= h2
        h1, h2 = h2, h1
        res = res1-res2
    return res

