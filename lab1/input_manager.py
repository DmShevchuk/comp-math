import random
from lab1.constants import CALCULATION_ACCURACY


def get_matrix_from_user_input() -> list:
    print("Введите 1 для ручного ввода")
    print("Введите 2 для ввода из файла")
    print("Введите 3 для создания случайной матрицы")
    input_mode = input(">>")
    if input_mode == "1":
        return get_matrix_from_console()
    if input_mode == "2":
        filename = input("Введите имя файла:")
        return get_matrix_from_file(filename)
    if input_mode == "3":
        return get_random_matrix()


def get_matrix_from_console() -> list:
    rows = int(input("Введите размерность матрицы: "))
    print(f"Введите матрицу размера {rows}x{rows + 1}:")
    matrix = []
    for i in range(rows):
        row = list(map(float, input().split()))
        if len(row) != rows + 1:
            raise ValueError("Неверное количество чисел!")
        matrix.append(row)
    return matrix


def get_matrix_from_file(filename: str) -> list:
    print("Считанная матрица:")
    with open(filename, 'r') as f:
        lines = f.readlines()
        matrix = []
        for line in lines:
            row = list(map(float, line.strip().split()))
            print(row)
            matrix.append(row)
    return matrix


def get_random_matrix() -> list:
    min_matrix_size = 3
    max_matrix_size = 21
    min_matrix_element = -100
    max_matrix_element = 100
    n = random.randint(min_matrix_size, max_matrix_size)
    matrix = []
    print(f"Случайная матрица n={n}:")
    for i in range(n):
        row = []
        for j in range(n + 1):
            element = random.uniform(min_matrix_element, max_matrix_element)
            row.append(element)
            print(f'{element:>{CALCULATION_ACCURACY + 4}.{CALCULATION_ACCURACY}f}', end=' ')
        print()
        matrix.append(row)
    return matrix
