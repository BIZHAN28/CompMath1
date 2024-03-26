def gaussian_elimination(matrix, b):
    n = len(matrix)
    det = 1  # ������������

    # ������ ���
    for i in range(n):
        # ����� ������������� �������� � �������
        max_index = i
        for j in range(i + 1, n):
            if abs(matrix[j][i]) > abs(matrix[max_index][i]):
                max_index = j

        # ����� ����� ��� ��������� ��������
        matrix[i], matrix[max_index] = matrix[max_index], matrix[i]
        b[i], b[max_index] = b[max_index], b[i]
        
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
        n = int(input("������� ����������� ������� (n <= 20): "))
        if n <= 0 or n > 20:
            raise ValueError("����������� ������� ������ ���� � ��������� �� 1 �� 20")
        
        print("������� ������������ �������:")
        matrix = []
        for i in range(n):
            row = list(map(float, input().split()))
            if len(row) != n:
                raise ValueError("���������� ��������� � ������ ������ ���� ������ ����������� �������")
            matrix.append(row)

        print("������� ������� ��������� ������:")
        b = list(map(float, input().split()))
        if len(b) != n:
            raise ValueError("���������� ��������� � ������� ��������� ������ ������ ���� ������ ����������� �������")

        return matrix, b

    except ValueError as e:
        print(f"������ �����: {e}")
        return None, None

def input_matrix_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            n = int(lines[0].strip())
            if n <= 0 or n > 20:
                raise ValueError("����������� ������� ������ ���� � ��������� �� 1 �� 20")

            matrix = []
            for line in lines[1:n+1]:
                row = list(map(float, line.strip().split()))
                if len(row) != n:
                    raise ValueError("���������� ��������� � ������ ������ ���� ������ ����������� �������")
                matrix.append(row)

            b = list(map(float, lines[n+1].strip().split()))
            if len(b) != n:
                raise ValueError("���������� ��������� � ������� ��������� ������ ������ ���� ������ ����������� �������")

            return matrix, b

    except FileNotFoundError:
        print("���� �� ������.")
    except ValueError as e:
        print(f"������ � �����: {e}")

    return None, None
    
def main():
    print("�������� ������ ����� ������:")
    print("1. � ����������")
    print("2. �� �����")
    choice = input("������� �����: ")

    if choice == "1":
        matrix, b = input_matrix_from_keyboard()
    elif choice == "2":
        file_name = input("������� ��� �����: ")
        matrix, b = input_matrix_from_file(file_name)
    else:
        print("�������� �����.")
        return

    if matrix is not None and b is not None:
        # ����� ������ ������
        solution = gaussian_elimination(matrix, b)

        if solution is not None:
            print("\n����������� �������:")
            for row in matrix:
                print(row)

            print("\n�������:")
            for i, value in enumerate(solution):
                print(f"x{i+1} =", value)
            print("\n������ �������:")
            print(residuals(matrix, b, solution))

main()
