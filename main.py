from util import input_data, normalize_vector
from solver import solve


def main():
    while True:
        matrix, vector, accuracy = input_data()
        solution, iterations_amount, matrix_norm, error_vector = solve(matrix, vector, accuracy)
        if solution is None or iterations_amount is None or matrix_norm is None or error_vector is None:
            return

        print("Решение:", normalize_vector(solution))
        print("Количество итераций:", iterations_amount)
        print("Норма матрицы:", round(matrix_norm, 4))
        print("Вектор погрешностей:", normalize_vector(error_vector))
        print()


if __name__ == "__main__":
    main()
