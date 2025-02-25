import random


def check_diagonal_dominance(matrix):
    n = len(matrix)
    for i in range(n):
        sm = 0
        for j in range(n):
            if i != j:
                sm += abs(matrix[i][j])
        if abs(matrix[i][i]) < sm:
            return False
    return True


def sort_for_diagonal_dominance(matrix):
    n = len(matrix)
    for i in range(n):
        max_row = max(range(i, n), key=lambda x: abs(matrix[x][i]))
        if max_row != i:
            matrix[i], matrix[max_row] = matrix[max_row], matrix[i]


def input_int(text, left, right):
    while True:
        try:
            num = input(text)
            if float(num) != int(num):
                raise ValueError("Число должно быть целым.")
            num = int(num)
            if not (left <= num <= right):
                raise ValueError(f"Число должно быть от {left} до {right}.")
            return num
        except ValueError as error:
            print(f"Ошибка ввода: {error}")


def input_accuracy():
    while True:
        try:
            accuracy = float(input("Введите точность: "))
            return accuracy
        except ValueError as error:
            print(f"Ошибка ввода: {error}")


def input_array(n, text):
    while True:
        try:
            arr = list(map(float, input(text).split()))
            if len(arr) != n:
                raise ValueError(f"Количество введенных элементов должно быть равно {n}.")
            return arr
        except ValueError as error:
            print(f"Ошибка ввода: {error}")


def input_matrix(n):
    matrix = [0] * n
    for i in range(n):
        print(f"{i + 1}-я строка матрицы:")
        matrix[i] = input_array(n, f"Введите {n} коэффициентов через пробел: ")
    return matrix


def read_from_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = [line.strip() for line in file.readlines() if line.strip() != ""]
        if len(lines) < 4:
            raise ValueError("Файл слишком короткий или имеет некорректный формат.")
        n = int(lines[0])
        expected_lines = n + 3
        if len(lines) != expected_lines:
            raise ValueError(f"Ожидалось {expected_lines} строк, но получено {len(lines)}.")
        matrix = [list(map(float, lines[i].split())) for i in range(1, n + 1)]
        vector = list(map(float, lines[n + 1].split()))
        if len(vector) != n:
            raise ValueError("Количество свободных членов должно совпадать с размером матрицы.")
        epsilon = float(lines[n + 2])
        return matrix, vector, epsilon
    except Exception as e:
        print("Ошибка при чтении файла:", e)
        return None, None, None


def input_data():
    print("Выберите режим чтения данных (введите 1 или 2)")
    print("1 - ввести матрицу вручную")
    print("2 - считать матрицу из файла")
    print("3 - сгенерировать рандомную матрицу")

    mode = input_int(">> ", 1, 3)
    if mode == 1:
        n = input_int("Введите размерность матрицы (от 1 до 20) ", 1, 20)
        matrix = input_matrix(n)
        vector = input_array(n, f"Введите свободный вектор ({n} элементов через пробел) ")
        accuracy = input_accuracy()
    elif mode == 2:
        while True:
            filename = input("Введите имя файла: ")
            matrix, vector, accuracy = read_from_file(filename)
            if matrix is not None and vector is not None and accuracy is not None:
                break
            else:
                print("Ошибка в файле. Попробуйте ещё раз.")
    else:
        n = input_int("Введите размерность матрицы (от 1 до 20) ", 1, 20)
        matrix, vector = generate_random_matrix_vector(n)
        print("Матрица сгенерирована со свободным вектором сгенерированы:")
        for i in range(n):
            print(" ".join(str(round(el, 2)) for el in matrix[i]), "|", round(vector[i], 2))
        accuracy = input_accuracy()
    return matrix, vector, accuracy


def generate_random_matrix_vector(size, min_val=-10, max_val=10):
    matrix = [[random.uniform(min_val, max_val) for _ in range(size)] for _ in range(size)]
    for i in range(size):
        off_diag_sum = sum(abs(matrix[i][j]) for j in range(size) if i != j)
        matrix[i][i] = off_diag_sum + random.uniform(1, 5)
    vector = [random.uniform(min_val, max_val) for _ in range(size)]
    return matrix, vector


def normalize_vector(vector):
    return list(map(lambda x: round(x, 4), vector))
