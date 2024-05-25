""" Задание на л.р. №6
Задание состоит из двух частей.
1 часть – написать программу в соответствии со своим вариантом задания. Написать 2 варианта
формирования (алгоритмический и с помощью функций Питона), сравнив по времени их выполнение.
2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение на
характеристики объектов (которое будет сокращать количество переборов)и целевую функцию для нахождения оптимального  решения.

Вариант 24. Дана квадратная матрица, состоящая из четырех равных по размерам подматриц. Сформировать все возможные
варианты данной матрицы путем последовательной замены подматриц нулевыми подматрицами.
"""

import numpy as np
import timeit
import random
import itertools

# Размер матрицы(n * n)
n = int(input())

# Количество подматриц
submatrix_size = n // 2

# Заполнение пустой матрицы
matrix_A = np.array([[0 for _ in range(n)] for _ in range(n)])

# Заполнение матрицы A рандомными числами
for r in range(n):
    for c in range(n):
        matrix_A[r][c] = random.randint(1, 5)

print('Исходная матрица:')
print(matrix_A)

# 1 Часть
# Вариант 1: Алгоритмический подход
def generate_matrix_algorithm(n, submatrix_size, matrix_A):
    # Создаем функцию для замены подматрицы нулевой матрицей
    def replace_submatrix_with_zeros(matrix, submatrix_coords):
        for coord in submatrix_coords:
            i, j = coord
            matrix[i:i + submatrix_size, j:j + submatrix_size] = 0

    def generate_all_zero_combinations(matrix, block_size, r, submatrices, temp_combination, index):
        if r == 0:
            temp_matrix = matrix.copy()
            replace_submatrix_with_zeros(temp_matrix, temp_combination)
            for row in temp_matrix:
                print(row)
            print('')
            return

        if index >= len(submatrices):
            return

        temp_combination.append(submatrices[index])
        generate_all_zero_combinations(matrix, block_size, r - 1, submatrices, temp_combination, index + 1)
        temp_combination.pop()
        generate_all_zero_combinations(matrix, block_size, r, submatrices, temp_combination, index + 1)

    submatrices = [(i, j) for i in range(0, n, submatrix_size) for j in range(0, n, submatrix_size)]
    for r in range(1, len(submatrices) + 1):
        temp_combination = []
        generate_all_zero_combinations(matrix_A, submatrix_size, r, submatrices, temp_combination, 0)




# Вариант 2: С помощью функций питона
def generate_matrix_python(n, submatrix_size, matrix_A):
    def replace_submatrix_with_zeros(matrix, submatrix_coords, submatrix_size):
        for coord in submatrix_coords:
            i, j = coord
            matrix[i:i + submatrix_size, j:j + submatrix_size] = 0

    def generate_all_zero_combinations(matrix, submatrix_size):
        submatrices = [(i, j) for i in range(0, n, submatrix_size) for j in range(0, n, submatrix_size)]

        for r in range(1, len(submatrices) + 1):
            combinations = itertools.combinations(submatrices, r)
            for combination in combinations:
                temp_matrix = np.copy(matrix)
                replace_submatrix_with_zeros(temp_matrix, combination, submatrix_size)
                for row in temp_matrix:
                    print(row)
                print('')


# Функция для измерения времени выполнения функции
def measure_time(function, n, submatrix_size, matrix_A):
    # Запуск таймера
    start_time = timeit.default_timer()
    function(n, submatrix_size, matrix_A)
    # Время выполнения функции
    return timeit.default_timer() - start_time

print("1 Часть")
print("Вывод всех возможных варинтов матрицы по алгоритмическому методу:")
print(generate_matrix_algorithm(n, submatrix_size, matrix_A))
print("Вывод всех возможных вариантов матрицы с помощью функций питона:")

# Время выполнения обеих функций
time_algorithm = measure_time(generate_matrix_algorithm, n, submatrix_size, matrix_A)
time_python = measure_time(generate_matrix_python, n, submatrix_size, matrix_A)

# Вывод времени выполнения обеих функций
print("\nВремя выполнения с использованием алгоритмического подхода:", time_algorithm)
print("Время выполнения с помощью функций Питона:", time_python)

# Функция для вычисления оптимального метода
def optimal_method():
    if time_algorithm < time_python:
        print("Алгоритмический метод быстрее.")
    elif time_algorithm > time_python:
        print("Метод с помощью функций Питона быстрее.")
    else:
        print("Оба метода выполняются с одинаковой скоростью.")

# Вызывание функции для определения оптимального метода
optimal_method()
