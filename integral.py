########### ИМПОРТ БИБЛИОТЕК ###########
from math import cos

from scipy.misc import derivative
########### ИМПОРТ БИБЛИОТЕК ###########


########### ПЕРЕМЕННЫЕ ###########
# Интервал
a, b = 4, 5
########### ПЕРЕМЕННЫЕ ###########


########### ФУНКЦИИ ###########
# range для float
def frange(start, stop, step):
    while start < stop:
        yield round(start, 2)
        start += step


# Функция интеграла
def func_x(x): 
    return 7 * cos(4*x)


### ПОЛУЧАЕМ ДАННЫЕ ###
def get_h(a, b, n):
    return round((b-a) / n, 2)


# Массив иксов
def get_list_x(a, b, h):
    return [x for x in frange(a, b, h)]


# Массив значений функции в точке (для каждого x вычисляем значение в точке)
def get_list_func(list_x): 
    return [round(func_x(x), 4) for x in list_x]


### ПОЛУЧАЕМ ИНТЕГРАЛ ###
# Формула левых прямоугольников
def get_integral_left_rect(h, list_func):
    return round(h * sum([y for y in list_func[:len(list_func) - 1]]), 4)


# Формула правых прямоугольников
def get_integral_right_rect(h, list_func):
    return round(h * sum([y for y in list_func[1:]]), 4)


# Формула центральных прямоугольников
def get_integral_center_rect(h, list_func):
    return round(h * sum([y for y in list_func]), 4)


# Формула погрешности интеграла для формулы центральных прямоугольников
def get_inaccuracy_center_rect(max_value, a, b, h):
    return round((b - a) / 24 * h**2 * max_value, 4)


# Формула трапеций
def get_integral_trapeze(a, b, h, func_x):
    value = 0
    for i in frange(a, b, h):
        value += (h/2) * (func_x(a)+func_x(b))
    return round(value, 4)


# Формула погрешности интеграла для формулы трапеций
def get_inaccuracy_integral_trapeze(a, b):
    return round((b-a)**3 / 6, 2)


# Формула производной 2 степени
def get_derivative(value, func_x):
    return round(derivative(func_x, value, dx=1e-6, n=2), 4)


### ФУНКЦИИ ВЫВОДА ВСЕХ ДАННЫХ И ИНТЕГРАЛОВ ###
# Все получаемые данные
def get_all_data():
    # Число иксов
    n = int(input('n: '))

    # Шаг
    h = get_h(a, b, n)

    # Список иксов
    list_x = get_list_x(a, b + h, h)

    # Список значений в точках функции
    list_func = get_list_func(list_x)

    return n, h, list_x, list_func


# Выдаем интеграл по формулам прямоугольников
def show_integral_rect(h, list_func):
    # Значение интеграла по формуле левых прямоугольников
    integral_left_rect = get_integral_left_rect(h, list_func)
    # Значение интеграла по формуле правых прямоугольников
    integral_right_rect = get_integral_right_rect(h, list_func)
    # Значение интеграла по формуле центральных прямоугольников
    integral_center_rect = get_integral_center_rect(h, list_func)

    # Погрешность
    # max_value - сравниваем значение производной 2 степени
    # для 2 точек - левого и правого интервала
    max_value = max(get_derivative(a, func), get_derivative(b, func))
    integral_center_rect_inaccuracy = get_inaccuracy_center_rect(
        max_value, a,
        b, h
    )

    print(f'\nЗначение интеграла по формуле левых прямоугольников:\
        {integral_left_rect}')
    print(f'Значение интеграла по формуле правых прямоугольников:\
        {integral_right_rect}')
    print(f'Значение интеграла по формуле центральных прямоугольников:\
        {integral_center_rect} +- {integral_center_rect_inaccuracy}')


# Выдаем интеграл по формуле трапеции
def show_integral_trapeze(list_func, h):
    # Значение интеграла по формуле трапеций
    integral_trapeze = get_integral_trapeze(a, b, h, func)
    # Погрешность
    integral_trapeze_inaccuracy = get_inaccuracy_integral_trapeze(a, b)

    print(f'Значение интеграла по формуле трапеций: \
        {integral_trapeze} +- {integral_trapeze_inaccuracy}')


def main():
    print('\nЗадание 2\n')

    # Получаем n, h, list_x, list_func
    n, h, list_x, list_func = get_all_data()

    print(cos(16))

    # Интеграл по формуле прямоугольников
    show_integral_rect(h, list_func)

    # Интеграл по формуле трапеции
    show_integral_trapeze(list_func, h)
########### ФУНКЦИИ ###########

if __name__ == '__main__':
    main()
