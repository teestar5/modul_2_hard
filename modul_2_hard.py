

print('Введите целое число от 3 до 20 ')
a = int(input())

for i in range(1, 21):
    for j in range(i+1, a):
        if ((i + j) % a == 0 or a % (i + j) == 0):
            print(i, j, end=" ")
            print(f"Пара чисел, сумма которых кратна {a}: {(i, j)}")


