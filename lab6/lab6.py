print("Проверка запуска")
matrix = [
    [0, 2, 0],
    [4, 0, 6],
    [9, 0, 9]
]

rows = len(matrix)
cols = len(matrix[0])

print("До сдвига:")
for i in range(rows):
    print(matrix[i])

for i in range(rows):
    new_row = []

    for j in range(cols):
        if matrix[i][j] != 0:
            new_row.append(matrix[i][j])

    zeros_count = cols - len(new_row)

    for k in range(zeros_count):
        new_row.insert(0, 0)

    matrix[i] = new_row

print("После сдвига вправо:")
for i in range(rows):
    print(matrix[i])