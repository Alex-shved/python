# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

with open("file-2.txt", "r") as file:
    for cnt, line in enumerate(file, start=1):
        words = int(line.count(' ') + 1)
        print(f'{cnt} строка: {words} слов(а|о)')
    print(f'Всего {cnt} строк(и)')


