import math


s3 = lambda x, n: (-1) ** (n + 1) * x ** n / n
s4 = lambda x, n: (-1) ** n * x ** (2 * n + 1) / (2 * n + 1)
vals_for_exp = [0.9999998, 1.000000, 0.5000063, 0.1666674, 0.0416350, 0.0083298, 0.0014393, 0.0002040]


def homemade_exp(x, acc=7):
    res = 0
    for i in range(acc):
        res += vals_for_exp[i] * x**i
    return res

"""
def homemade_sin(x, acc=9):
    res = 0
    for i in range(1, acc, 2):
        res += vals_for_sin[i] * x**i
    return res
"""


def homemade_ln_plus_1(x, acc):
    n = 1
    res1 = 0
    res2 = s3(x, n)
    while abs(res2 - res1) >= acc:
        res1 = res2
        n += 1
        res2 += s3(x, n)
    return res2


def homemade_arctg(x, acc):
    n = 1
    res1 = 0
    res2 = x - s4(x, n)
    while abs(res2 - res1) >= acc:
        res1 = res2
        n += 1
        res2 += s4(x, n)
    return res2


def main():
    x = 0.5
    y = math.pi / 6
    print('x = {}\nexp(x) ='.format(x), homemade_exp(x))
    print('ln(x+1) =', homemade_ln_plus_1(x, 0.00001))
    print('\ny = {}\narctg(y) ='.format(x), homemade_arctg(y, 0.00001))
    print('sin(y) =', homemade_sin(y))


main()
