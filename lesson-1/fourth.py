#4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл
# while и арифметические операции.

num = int(input('Введите число - '))
max_num = 0
while num >= 1:
    if max_num < num % 10:
        max_num = num % 10
    num = num // 10
print(f'Самое большое число - {max_num}')
