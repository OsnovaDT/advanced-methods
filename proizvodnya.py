########### ИМПОРТ БИБЛИОТЕК ###########
import integral
########### ИМПОРТ БИБЛИОТЕК ###########


########### ФУНКЦИИ ###########
# range для float
def frange(start, stop, step):
    while start < stop:
        yield round(start, 2)
        start += step


# Интервал
def get_interval():
    return (
        float(input('Левый интервал: ')),
        float(input('Правый интервал: '))
    )


# Точка для производной 1 степени
def get_x():
    return float(input('\nТочка для нахождения производной 1 степени: '))


# Точка для производной 2 степени
def get_x_2():
    return float(input('Точка для нахождения производной 2 степени: '))


# Массив иксов
def get_list_x(l_interval, r_interval, h):
    return [x for x in frange(l_interval, r_interval, h)]


# Массив значений функции в точке
# Для каждого икса просим ввод значения функции
def get_list_func(list_x):
    return [float(input(f'Значение функции в точке {x}: ')) for x in list_x]


# Производная 1 степени
def derivative(x_index, h, list_func):
    # f(1)
    f1 = list_func[x_index + 1]
    # f(-1)
    negative_f1 = list_func[x_index - 1]

    return f'\nПервая производная: {round((f1 - negative_f1) / (2*h), 2)}'


# Производная 2 степени
def derivative_2(x_index, h, list_func):
    # f(1)
    f1 = list_func[x_index + 1]
    # f(0)
    f0 = list_func[x_index]
    # f(-1)
    negative_f1 = list_func[x_index - 1]

    return f'Вторая производная: {round((f1 - 2*f0 + negative_f1) / h**2, 2)}'


# Выводим необходимые данные
def get_all_data():
    # Получаем интервал
    l_interval, r_interval = get_interval()
    # Получаем шаг
    h = float(input('Шаг: '))
    # Получаем точку для 1 производной
    x = get_x()
    # Получаем точку для 2 производной
    x_2 = get_x_2()

    return l_interval, r_interval, h, x, x_2


# Выдаем списки с икс и значениями функции
def get_lists(l_interval, r_interval, h):
    print()

    # Генерируем список иксов
    list_x = get_list_x(l_interval, r_interval + h, h)
    # Получаем список значений функции в точках
    list_func = get_list_func(list_x)

    return list_x, list_func


# Выводим производные
def show_derivatives(h, x, x_2, list_x, list_func):
    # Выводим производные
    print(derivative(list_x.index(x), h, list_func))
    print(derivative_2(list_x.index(x_2), h, list_func))


def main():
    # 1 Задание
    print('Задание 1\n')

    # Получаем l_interval, r_interval, h, x, x_2
    l_interval, r_interval, h, x, x_2 = get_all_data()

    list_x, list_func = get_lists(l_interval, r_interval, h)

    show_derivatives(h, x, x_2, list_x, list_func)

    # 2 Задание
    integral.main()
########### ФУНКЦИИ ###########


if __name__ == '__main__':
    main()
