import math
from formulas import *
from rcounting import *
from prettytable import PrettyTable


def input_table():
    print('Введите границы интегрирования, шаг и точность:\na = ', end='')
    a = float(input())
    print('b = ', end='')
    b = float(input())
    print('n = ', end='')
    n = float(input())
    print('ε = ', end='')
    e = float(input())
    res = [a, b, n, e]
    return res


def intergral_table(args):
    left_parts = [str(round(rectangle_left([args[0], args[1], args[2]]), 5)) + ', R = ' + str(round(r_rectangle(
        [args[0], args[1], args[2]]), 5))]
    right_parts = [str(round(rectangle_right([args[0], args[1], args[2]]), 5)) + ', R = ' + str(round(r_rectangle(
        [args[0], args[1], args[2]]), 5))]
    trap = [str(round(trapeze([args[0], args[1], args[2]]), 5)) +
            ', R = ' + str(round(r_trapeze([args[0], args[1], args[2]]), 8))]
    par = [str(round(parabola([args[0], args[1], args[2]]), 5)) +
           ', R = ' + str(round(r_parabola([args[0], args[1], args[2]]), 8))]
    first = [str(round(double_recount([args[0], args[1], args[3]]), 5))]
    sec = [str(round(second_algorithm([args[0], args[1], args[3]]), 5))]
    t = PrettyTable()
    column_names = ['Прямоугольник левых частей ', 'Прямоугольник правых частей', 'Трапеция', 'Парабола',
                    'Первый алгоритм', 'Второй алгоритм']
    t.add_column(column_names[0], left_parts)
    t.add_column(column_names[1], right_parts)
    t.add_column(column_names[2], trap)
    t.add_column(column_names[3], par)
    t.add_column(column_names[4], first)
    t.add_column(column_names[5], sec)
    return t


def entering_const():
    """
    Функция для форматированного ввода параметров,
    необходимых при вычислении интеграла методами
    с постоянным шагом
    """
    print('Введите границы интегрирования и шаг:\na = ', end='')
    a = float(input())
    print('b = ', end='')
    b = float(input())
    print('n = ', end='')
    n = float(input())
    res = [a, b, n]
    return res


def entering_var():
    """
    Функция для форматированного ввода параметров,
    необходимых при вычислении интеграла методами
    с переменным шагом
    """
    print('Введите границы интегрирования и точность:\na = ', end='')
    a = float(input())
    print('b = ', end='')
    b = float(input())
    print('ε = ', end='')
    e = float(input())
    res = [a, b, e]
    return res


def cond_checker(menu: dict) -> int:
    for i in sorted(menu.keys()):
        print(i)
    cond = int(input())
    return cond


main_menu = {'1) Методы с постоянным шагом': 1,
             '2) Методы с переменным шагом': 2,
             '3) Таблица': 3,
             '4) Выход': 4}
menu_constant = {'1) Метод правых частей прямоугольников': 1,
                 '2) Метод левых частей прямоугольников': 2,
                 '3) Метод трапеций': 3,
                 '4) Метод парабол': 4,
                 '5) Выход': 5}
menu_var = {'1) Метод по первому алгоритму': 1,
            '2) Метод по второму алгоритму': 2,
            '3) Выход': 3}


cond_main = 0
while cond_main != main_menu['4) Выход']:
    cond_main = cond_checker(main_menu)
    if cond_main == main_menu['1) Методы с постоянным шагом']:
        cond_const = 0
        while cond_const != menu_constant['5) Выход']:
            cond_const = cond_checker(menu_constant)
            if (cond_const > 0) & (cond_const < 5):
                arguments = entering_const()
            if cond_const == 1:
                print('\nРезультат вычисления: ', rectangle_left(arguments), ' Остаточный член:',
                      r_rectangle(arguments), '\n')
            elif cond_const == 2:
                print('\nРезультат вычисления: ', rectangle_right(arguments), ' Остаточный член:',
                      r_rectangle(arguments), '\n')
            elif cond_const == 3:
                print('\nРезультат вычисления: ', trapeze(arguments), ' Остаточный член:',
                      r_trapeze(arguments), '\n')
            elif cond_const == 4:
                print('\nРезультат вычисления: ', parabola(arguments), ' Остаточный член:',
                      r_parabola(arguments), '\n')
            elif cond_const == 5:
                pass
            else:
                print('Ошибка, введите другое значение')
    elif cond_main == main_menu['2) Методы с переменным шагом']:
        cond_var = 0
        while cond_var != menu_var['3) Выход']:
            cond_var = cond_checker(menu_var)
            if (cond_var > 0) & (cond_var < 3):
                arguments = entering_var()
            if cond_var == 1:
                print('\nРезультат вычисления: ', double_recount(arguments), '\n')
            elif cond_var == 2:
                print('\nРезультат вычисления: ', second_algorithm(arguments), '\n')
            elif cond_var == 3:
                pass
            else:
                pass
    elif cond_main == main_menu['3) Таблица']:
        args = input_table()
        print('\n', intergral_table(args), '\n')
    elif cond_main == main_menu['4) Выход']:
        pass
    else:
        print('Ошибка, введите другое значение')
