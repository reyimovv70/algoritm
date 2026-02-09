num = int(input("Введите целое число: "))

while num <= 0:
    print("Число не положительное:(")
    num = int(input("Введите целое число: "))

print(" положительное число;):", num)
while True:
    num = int(input("Введите число: "))

    if num > 100:
        print(" число больше 100. Программа завершена.")
        break
    else:
        print("Число должно быть больше 100.")
num = int(input("введи сумму num: "))
summa = 0
for i in range(1, num + 1):
    summa += i
print("Сумма чисел от 1 до", num, "равна", summa)
for i in range(1, 6):
    for j in range(1, 6):
       print(i * j, end=" ")
    print()