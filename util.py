

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

# def read_from_file(filename):


def input_data():
    print("Выберите режим чтения данных (введите 1 или 2)")
    print("1 - ввести матрицу вручную")
    print("2 - считать матрицу из файла")

    mode = input_int(">> ", 1, 2)
    if mode == 1:
        n = input_int("Введите размерность матрицы (от 1 до 20) ", 1, 20)
        matrix = input_matrix(n)
        vector = input_array(n, f"Введите свободный вектор ({n} элементов через пробел) ")
        accuracy = input_accuracy()
    # else:
    #     while True:
    #         filename = input("Введите имя файла: ")
    #         matrix, vector, accuracy = read_from_file(filename)
    #         if matrix is not None and vector is not None and accuracy is not None:
    #             break
    #         else:
    #             print("Ошибка в файле. Попробуйте ещё раз.")
    return matrix, vector, accuracy
