########### ИМПОРТ БИБЛИОТЕК ###########
from os import system
########### ИМПОРТ БИБЛИОТЕК ###########


########### ФУНКЦИИ ###########
def _clear():
    system('clear')


def _get_matrix_size():
    _clear()

    return int(input('Размерность матрицы: '))


def _create_empty_matrix(size):
    return [[0] * size for i in range(size)]


def _completion_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if (j == i) or (i == j+1) or (j == i+1):
                matrix[i][j] = int(input(f'Элемент [{i}][{j}]: '))
        _clear()

    return matrix


def _get_matrix_values(matrix_size):
    values = []

    for i in range(matrix_size):
        _clear()
        value = int(input(f'Значение правой\
части матрицы для строки {i+1}: '))

        values.append(value)

    return values


# Функция вывода матрицы с ее значениями
def _print_matrix(matrix, list_values):
    _clear()
    print('Матрица:')
    for i in range(len(matrix)):
        print(matrix[i], f'[{list_values[i]}]')


# Прямая прогонка
def direct_run_through(matrix, values):
    matrix_size = len(matrix)

    list_a, list_b, list_x = [], [], []

    a1, b1 = -matrix[0][1] / matrix[0][0], values[0] / matrix[0][0]

    list_a.append(a1)
    list_b.append(b1)

    for i in range(1, len(values) - 1):
        yi = matrix[i][i] + matrix[i][i-1]*list_a[i-1]
        ai = round(-matrix[i][i+1] / yi, 4)
        bi = round((values[i] - matrix[i][i-1]*list_b[i-1]) / yi, 4)

        list_a.append(ai)
        list_b.append(bi)

    yn = round(
        matrix[matrix_size-1][matrix_size-1]
        + matrix[matrix_size-1][matrix_size-2]
        * list_a[len(list_a)-1],
        4
    )

    bn = round(
        (values[len(values)-1]
        - matrix[matrix_size-1][matrix_size-2]
        * list_b[len(list_b)-1])
        / yn,
        4
    )

    list_b.append(bn)

    return list_a, list_b, list_x, bn


def reverse_run_through(matrix, values):
    list_a, list_b, list_x, bn = direct_run_through(matrix, values)

    list_x.append(bn)

    for i in range(len(values)-2, -1, -1):
        x = round(list_a[i]*list_x[0] + list_b[i], 4)
        list_x.insert(0, x)

    return list_x


def _func_print_x(list_x):
    print('\nЗначения для x:')

    for number, x in enumerate(list_x):
        print(f'x{number + 1} = {x}')


def main():
    matrix_size = _get_matrix_size()

    empty_matrix = _create_empty_matrix(matrix_size)

    matrix = _completion_matrix(empty_matrix)

    # Заполняем список значений матрицы
    values = _get_matrix_values(matrix_size)

    _print_matrix(matrix, values)

    list_x = reverse_run_through(matrix, values)

    # Выводим иксы
    _func_print_x(list_x)

if __name__ == '__main__':
    main()
