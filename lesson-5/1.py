# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка


with open("file-2.txt", "w") as file:
    print('Введиье текст для записи в файл, для завершения введите пустую строку ')
    while True:
        text = input()
        if text == '':
            break
        else:
            file.write(text + '\n')
