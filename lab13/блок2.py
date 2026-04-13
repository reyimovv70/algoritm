import time
import numpy as np

def multiply_matrices(A, B):
    """
    Наивное умножение матриц n x n.
    Сложность: O(n^3)
    """
    n = len(A)
    # Инициализируем результирующую матрицу нулями
    C = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):          # Проход по строкам A
        for j in range(n):      # Проход по столбцам B
            for k in range(n):  # Вычисление скалярного произведения
                C[i][j] += A[i][k] * B[k][j]
    return C

# Параметры
N = 100
# Генерируем случайные матрицы для теста
matrix_a = np.random.randint(1, 10, (N, N)).tolist()
matrix_b = np.random.randint(1, 10, (N, N)).tolist()

# Замер времени
start_time = time.time()
result = multiply_matrices(matrix_a, matrix_b)
end_time = time.time()

print(f"Размер матрицы: {N}x{N}")
print(f"Время выполнения: {end_time - start_time:.4f} секунд")