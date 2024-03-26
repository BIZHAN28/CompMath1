def gaussian_elimination(matrix, b):
    n = len(matrix)
    det = 1  # Определитель

    # Прямой ход
    for i in range(n):
        # Поиск максимального элемента в столбце
        max_index = i
        for j in range(i + 1, n):
            if abs(matrix[j][i]) > abs(matrix[max_index][i]):
                max_index = j

        # Обмен строк для улучшения точности
        matrix[i], matrix[max_index] = matrix[max_index], matrix[i]
        b[i], b[max_index] = b[max_index], b[i]
        
        if matrix[i][i] == 0:
            print("Был получен нулевой элемент на главной диагонали. Метод Гаусса не применим.")
            return None
        
        # Приведение матрицы к треугольному виду
        for j in range(i + 1, n):
            coef = matrix[j][i] / matrix[i][i]
            for k in range(i, n):
                matrix[j][k] -= coef * matrix[i][k]
            b[j] -= coef * b[i]

        det *= matrix[i][i]  # Обновление определителя

    if det == 0:
        print("Определитель матрицы равен 0. Система имеет бесконечное количество решений или не имеет решений.")
        return None

    # Обратный ход
    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = b[i]
        for j in range(i + 1, n):
            x[i] -= matrix[i][j] * x[j]
        x[i] /= matrix[i][i]

    return x

def residuals(matrix, b, x):
    residuals = []
    for i in range(len(matrix)):
        res = 0
        for j in range(len(matrix[0])):
            res += matrix[i][j] * x[j]
        residuals.append(res - b[i])
    return residuals
    
def input_matrix_from_keyboard():
    try:
        n = int(input("Введите размерность матрицы (n <= 20): "))
        if n <= 0 or n > 20:
            raise ValueError("Размерность матрицы должна быть в диапазоне от 1 до 20")
        
        print("Введите коэффициенты матрицы:")
        matrix = []
        for i in range(n):
            row = list(map(float, input().split()))
            if len(row) != n:
                raise ValueError("Количество элементов в строке должно быть равным размерности матрицы")
            matrix.append(row)

        print("Введите столбец свободных членов:")
        b = list(map(float, input().split()))
        if len(b) != n:
            raise ValueError("Количество элементов в столбце свободных членов должно быть равным размерности матрицы")

        return matrix, b

    except ValueError as e:
        print(f"Ошибка ввода: {e}")
        return None, None

def input_matrix_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            n = int(lines[0].strip())
            if n <= 0 or n > 20:
                raise ValueError("Размерность матрицы должна быть в диапазоне от 1 до 20")

            matrix = []
            for line in lines[1:n+1]:
                row = list(map(float, line.strip().split()))
                if len(row) != n:
                    raise ValueError("Количество элементов в строке должно быть равным размерности матрицы")
                matrix.append(row)

            b = list(map(float, lines[n+1].strip().split()))
            if len(b) != n:
                raise ValueError("Количество элементов в столбце свободных членов должно быть равным размерности матрицы")

            return matrix, b

    except FileNotFoundError:
        print("Файл не найден.")
    except ValueError as e:
        print(f"Ошибка в файле: {e}")

    return None, None
    
def main():
    print("Выберите способ ввода данных:")
    print("1. С клавиатуры")
    print("2. Из файла")
    choice = input("Введите номер: ")

    if choice == "1":
        matrix, b = input_matrix_from_keyboard()
    elif choice == "2":
        file_name = input("Введите имя файла: ")
        matrix, b = input_matrix_from_file(file_name)
    else:
        print("Неверный выбор.")
        return

    if matrix is not None and b is not None:
        # Вызов метода Гаусса
        solution = gaussian_elimination(matrix, b)

        if solution is not None:
            print("\nТреугольная матрица:")
            for row in matrix:
                print(row)

            print("\nРешение:")
            for i, value in enumerate(solution):
                print(f"x{i+1} =", value)
            print("\nВектор невязок:")
            print(residuals(matrix, b, solution))

main()
