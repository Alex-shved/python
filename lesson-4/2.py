# 2. Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].

import random

my_random_list = [random.randint(random.randint(0, 20), random.randint(20, 40)) for el in range(0, 20)]
print(my_random_list)
my_new_list = [my_random_list[num] for num in range(1, len(my_random_list)) \
               if my_random_list[num] > my_random_list[num - 1]]
print(my_new_list)
