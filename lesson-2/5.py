# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. У пользователя
# необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.


numbers = [7, 5, 3, 3, 2]
rating_numbers = []
cnt = 0
while True:
    print('-' * 50)
    num = input("Введите натуральное число - ")
    if not num.isdigit():
        print('Попробуйте всё же ввесть натуральное число')
    else:
        num=int(num)
        break
for i in range(0, int(len(numbers))):
    if num > numbers[i]:
        numbers.insert(i, num)
        break
    elif i == int(len(numbers)-1):
        numbers.append(num)
        break
    elif numbers[i] >= num > numbers[i + 1]:
        numbers.insert(i, num)
        break
print(f'Результат: {numbers}')




