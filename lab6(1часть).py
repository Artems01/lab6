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
n = 4

# Количество подматриц
submatrix_size = n // 2

#Заполнение пустой матрицы
matrix_A = np.array([[0 for _ in range(n)] for _ in range(n)])

# Заполнение матрицы A рандомными числами
for r in range(n):
    for c in range(n):
        matrix_A[r][c] = random.randint(0, 10)

#Вариант 1: Алгоритмический подход
def generate_matrix_algorithm(n, submatrix_size, matrix_A):
    # Создаем функцию для замены подматрицы нулевой матрицей
    def replace_submatrix(matrix, submatrix_size, i, j):
        matrix[i:i+submatrix_size, j:j+submatrix_size] = 0

    # Перебираем все возможные комбинации заменяемых подматриц
    for i in range(0, n, submatrix_size):
        for j in range(0, n, submatrix_size):
            # Копируем исходную матрицу для каждой комбинации
            matrix_B = matrix_A.copy()
            # Заменяем подматрицу нулевой матрицей
            replace_submatrix(matrix_B, submatrix_size, i, j)
    return matrix_B

#Вариант 2: С помощью функций питона
def generate_matrix_python(n, submatrix_size, matrix_A):
    # Создаем функцию для формирования матрицы с нулевой подматрицей
    def create_matrix_with_zero_submatrix(matrix, submatrix_size, i, j):
        B = matrix.copy()
        B[i:i + submatrix_size, j:j + submatrix_size] = 0
        return B

    # Формируем все возможные варианты матриц с помощью itertools.product
    possible_combinations = itertools.product(range(0, n, submatrix_size), repeat=2)

    for i, j in possible_combinations:
        # Создаем матрицу для каждой комбинации
        matrix_B = create_matrix_with_zero_submatrix(matrix_A, submatrix_size, i, j)

    return matrix_B

# Функция для измерения времени выполнения функции
def measure_time(function, n, submatrix_size, matrix_A):
    # Запуск таймера
    start_time = timeit.default_timer()
    function(n, submatrix_size, matrix_A)
    # Время выполнения функции
    return timeit.default_timer() - start_time

print("1 Часть")
print("Вывод всех возможных варинтов матрицы")
print(generate_matrix_algorithm(n, submatrix_size, matrix_A))

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