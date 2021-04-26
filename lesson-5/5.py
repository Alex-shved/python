# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

import random
sum = 0

with open("file-5.txt", "w+") as file:
    for _ in range(0, 20):
        file.write(str(random.randint(-10, 10)) + ' ')
    file.seek(0)
    for i in file.read().split():
        print(i, end=' ')
        sum += int(i)
    print(f'\nСумма всех чисел = {sum}')



