# 1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого
# элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя,
# а указать явно, в программе.

list = [('2', 'hello'), 'first', 2, True, {False, 22}]

for elements in list:
    print('{} - {}'.format(elements,type(elements)))
print(f'{list} - {type(list)}')
