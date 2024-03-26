def gaussian_elimination(matrix, b):
    n = len(matrix)
    det = 1  # ������������

    # ������ ���
    for i in range(n):
        
        if matrix[i][i] == 0:
            print("��� ������� ������� ������� �� ������� ���������. ����� ������ �� ��������.")
            return None
        
        # ���������� ������� � ������������ ����
        for j in range(i + 1, n):
            coef = matrix[j][i] / matrix[i][i]
            for k in range(i, n):
                matrix[j][k] -= coef * matrix[i][k]
            b[j] -= coef * b[i]

        det *= matrix[i][i]  # ���������� ������������

    if det == 0:
        print("������������ ������� ����� 0. ������� ����� ����������� ���������� ������� ��� �� ����� �������.")
        return None

    # �������� ���
    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = b[i]
        for j in range(i + 1, n):
            x[i] -= matrix[i][j] * x[j]
        x[i] /= matrix[i][i]

    return x