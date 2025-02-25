from util import input_data
from solver import solve


def main():
    matrix, vector, accuracy = input_data()
    solution, iterations_amount, matrix_norm, error_vector = solve(matrix, vector, accuracy)
    if solution is None or iterations_amount is None or matrix_norm is None or error_vector is None:
        return
    print("Решение:", solution)
    print("Количество итераций:", iterations_amount)
    print("Норма матрицы:", matrix_norm)
    print("Вектор погрешностей:", error_vector)


if __name__ == "__main__":
    main()
