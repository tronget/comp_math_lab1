from util import *


def solve(matrix, vector, accuracy):
    if not check_diagonal_dominance(matrix):
        sort_for_diagonal_dominance(matrix)
        if not check_diagonal_dominance(matrix):
            print("Невозможно найти решение матрицы!")
            return None, None, None, None
    n = len(vector)
    prev_approximation = [vector[i] / matrix[i][i] for i in range(n)]
    error_vector = [accuracy] * n
    iterations_amount = 0
    while any(x >= accuracy for x in error_vector):
        iterations_amount += 1
        approximation = [0] * n
        for i in range(n):
            sm = vector[i]
            for j in range(n):
                if i != j:
                    sm -= matrix[i][j] * prev_approximation[j]
            approximation[i] = sm / matrix[i][i]
        error_vector = [abs(approximation[k] - prev_approximation[k]) / abs(approximation[k]) for k in range(n)]
        prev_approximation = approximation.copy()

    matrix_norm = max(sum(abs(value) for value in row) for row in matrix)
    return prev_approximation, iterations_amount, matrix_norm, error_vector
