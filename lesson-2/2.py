# 2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами
# 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка
# элементов необходимо использовать функцию input().


list_elem = []
cnt = 0
while not list_elem:
    print('-' * 50)
    string_elem = input("Введите  элементы списка разделенные пробелом - ")
    list_elem = string_elem.split()
    if not list_elem:
        print('Вы ничего не ввели, повторите попытку\n')
print(f'\nНачальныее данные: {list_elem}')
while cnt < len(list_elem) - 1:
    buf = list_elem[cnt]
    list_elem[cnt] = list_elem[cnt+1]
    list_elem[cnt+1] = buf
    cnt += 2
print(f'Итоговые данные: {list_elem}')
exit(0)
