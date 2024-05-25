import numpy as np
import timeit
import random


# 2 Часть. Ограничение - сумма элементов подматрицы должна быть меньше или равно определенному значению.

# Размер матрицы(n * n)
n = int(input())

# Пороговая сумма значений элементов подматрицы
threshold_sum = int(input())

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


def generate_matrix_algorithm_with_constraint(n, submatrix_size, matrix_A, threshold_sum):
    def replace_submatrix_with_zeros(matrix, submatrix_coords):
        for coord in submatrix_coords:
            i, j = coord
            submatrix_sum = matrix[i:i + submatrix_size, j:j + submatrix_size].sum()
            if submatrix_sum <= threshold_sum:
                matrix[i:i + submatrix_size, j:j + submatrix_size] = 0

    def generate_all_zero_combinations(matrix, block_size, r, submatrices, temp_combination, index):
        if r == 0:
            temp_matrix = matrix.copy()
            submatrix_values = [temp_matrix[i:i + block_size, j:j + block_size].sum() for i, j in temp_combination]
            if all(value <= threshold_sum for value in submatrix_values):
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

    print("\nВывод результов с ограничениями:")
    for r in range(1, len(submatrices) + 1):
        temp_combination = []
        generate_all_zero_combinations(matrix_A, submatrix_size, r, submatrices, temp_combination, 0)


generate_matrix_algorithm_with_constraint(len(matrix_A), submatrix_size, matrix_A, threshold_sum)
# Время выполнения функции с ограничениями.
time_generate_matrix_algorithm_with_constraint = timeit.timeit(lambda: generate_matrix_algorithm_with_constraint, number=1)
print('Время выполнения с ограничением:', time_generate_matrix_algorithm_with_constraint)
