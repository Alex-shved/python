# 6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит
# информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения). Структуру нужно сформировать
# программно, т.е. запрашивать все данные у пользователя.


def menu_display():
    print('-' * 50)
    print(MENU)
    print('-' * 50)
    return 0


def error_display():
    print("Введенные данные не допустимы")
    print('Сделайте выбора из предлагаемых вариантов')
    return 0


def input_data(var):
    while True:
        num = input('Действие: ')
        if not num.isdigit():
            error_display()
            menu_display()
        elif int(num) < 0 or int(num) > var:
            error_display()
            menu_display()
        else:
            return int(num)


MENU = '1 - Добавить товар\n2 - Получить данные\n3 - Получить сырые данные\n0 - Выход\n'
COLUMNS = ['Название', 'Цена', 'Количество', 'Ед']
db = []
processed_data = {}
temp = {}
product = ()
index = 1
while True:
    menu_display()
    choice = input_data(3)
    if choice == 1:
        print('Создание нового товара в базе')
        temp = dict()
        for i in COLUMNS:
            temp[i] = input(f"{i} - ")
        product = (index, temp)
        index += 1
        db.append(product)
    elif choice == 2:
        for data in COLUMNS:
            detail = []
            for i in range(0, len(db)):
                detail.append(db[i][1].get(data))
            processed_data[data] = detail
        print(processed_data)
    elif choice == 3:
        for i in db:
            print(i)
    elif choice == 0:
        exit(0)
