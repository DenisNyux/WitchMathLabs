import math
import formulas
import rcounting


def entering_const():
    """Функция для форматированного ввода параметров,
    необходимых при вычислении интеграла методами
    с постоянным шагом"""
    print('Введите границы интегрирования и шаг:\na = ', end='')
    a = float(input())
    print('b = ', end='')
    b = float(input())
    print('n = ', end='')
    n = float(input())
    res = [a, b, n]
    return res


def entering_var():
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
             '3) Выход': 3}
menu_constant = {'1) Метод правых частей прямоугольников': 1,
                 '2) Метод левых частей прямоугольников': 2,
                 '3) Метод трапеций': 3,
                 '4) Метод парабол': 4,
                 '5) Выход': 5}
menu_var = {'1) Метод по первому алгоритму': 1,
            '2) Метод по второму алгоритму': 2,
            '3) Выход': 3}


cond_main = 0
while cond_main != main_menu['3) Выход']:
    cond_main = cond_checker(main_menu)
    if cond_main == main_menu['1) Методы с постоянным шагом']:
        cond_const = 0
        while cond_const != menu_constant['5) Выход']:
            cond_const = cond_checker(menu_constant)
            if (cond_const > 0) & (cond_const < 5):
                arguments = entering_const()
            if cond_const == 1:
                print('\nРезультат вычисления: ', formulas.rectangle_left(arguments), ' Остаточный член:',
                      rcounting.r_rectangle(arguments), '\n')
            elif cond_const == 2:
                print('\nРезультат вычисления: ', formulas.rectangle_right(arguments), ' Остаточный член:',
                      rcounting.r_rectangle(arguments), '\n')
            elif cond_const == 3:
                print('\nРезультат вычисления: ', formulas.trapeze(arguments), ' Остаточный член:',
                      rcounting.r_trapeze(arguments), '\n')
            elif cond_const == 4:
                print('\nРезультат вычисления: ', formulas.parabola(arguments), ' Остаточный член:',
                      rcounting.r_parabola(arguments), '\n')
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
                print('\nРезультат вычисления: ', formulas.double_recount(arguments), '\n')
            elif cond_var == 2:
                print('\nРезультат вычисления: ', formulas.second_algorithm(arguments), '\n')
            elif cond_var == 3:
                pass
            else:
                pass
    elif cond_main == main_menu['3) Выход']:
        pass
    else:
        print('Ошибка, введите другое значение')
