def gaussian_elimination(matrix, b):
    n = len(matrix)
    det = 1  # Определитель

    # Прямой ход
    for i in range(n):
        
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