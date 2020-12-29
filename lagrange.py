########### ИМПОРТ БИБЛИОТЕК ###########
from math import cos

import numpy as np
import matplotlib.pyplot as plt
########### ИМПОРТ БИБЛИОТЕК ###########


########### ФУНКЦИИ ###########
def func_x(x):
    return 5*cos(x) - x/2


def get_l(x, n, xn, x_list):
    l = 1
    temp = x_list[:]
    temp.remove(xn)
    for i in temp:
        l *= (x - i)/(xn - i)
    return round(l, 5)


def get_chart_func(x_list, func_x_list, interval_left, interval_right):
    fig, ax = plt.subplots()

    x = np.linspace(intget_lerval_left, interval_right, 100)
    y = 5 * np.cos(x) - x / 2
    ax.plot(x, y)

    ax.plot(x_list, func_x_list)

    plt.show()


def main():
    interval_left = int(input('Левая точка диапозона: '))
    interval_right = int(input('Правая точка диапозона: '))

    n = int(input('n: '))

    x_list = np.linspace(
        interval_left,
        interval_left + n + 1,
        100
    )
    x_list = list(x_list)

    x = float(input('x: '))

    # Считаем f для всех x
    func_x_list = [round(func_x(i), 5) for i in x_list]

    # Считаем l для всех x
    list_l = [get_l(x, n, xn, x_list) for xn in x_list]

    # Считаем L
    L = 0
    for number, l in enumerate(list_l):
        L += l * func_x_list[number]
    print('\nL = ', round(L, 5))

    question = int(input('Показать график функции?: '))

    get_chart_func(
        x_list, func_x_list,
        interval_left, interval_right
    )
########### ФУНКЦИИ ###########


if __name__ == '__main__':
    main()
