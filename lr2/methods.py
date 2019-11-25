def func(x, y):
    return y*(1-x)


def euler(a, b, n, x, y):
    h = (b - a) / n
    print('Шаг: ', h)
    while x <= b-h:
        print('x =', round(x, 1), end=' ')
        print('y =', y)
        y += h*func(x, y)
        x += h


def runge_kutt(a, b, n, x, y):

    def runge_changer(x, y, h):
        k = list()
        k.append(h * func(x, y))
        k.append(2 * h * func(x + h / 2, y + k[0] / 2))
        k.append(2 * h * func(x + h / 2, y + k[1] / 2))
        k.append(h * func(x + h, y + k[2]))
        return sum(k) / 6

    h = (b - a) / n
    while x <= b-h:
        print('x =', round(x, 1), end=' ')
        print('y =', y)
        y += runge_changer(x, y, h)
        x += h


def high(a, b, y, z, n):
    x = a
    h = (a-b)/n
    while x < b:
        y1 = y
        print("x = ", round(x, 5), "z = ", round(z, 5), "y = ", round(y, 5))
        y += h * z
        z -= h * (z / x + y1)
        x += h


def systemUr(a, b, x, y, z, n):
  h = (a-b)/n
  t = a
  b = float(input("Введите b "))
  x # Введите х(0)
  y = float(input("Введите y(0) "))
  z = float(input("Введите z(0) "))

  while t < b:
     print("t = ", round(t, 5), "x = ", round(x, 5), "z = ", round(z, 5), "y = ", round(y, 5))
     x0 = x
     y0 = y
     z0 = z
     x += h * (-2 * x0 + 5 * z0)
     y += h * (math.sin(t - 1) * x0 - y0 + 3 * z0)
     z += h * (-x0 + 2 * z0)
     t += h


euler(0, 1, 10, 0, 1)
runge_kutt(0, 1, 10, 0, 1)
