# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

sum_salary = 0
with open("file-2.txt", "r") as file:
    for cnt, line in enumerate(file, start=1):
        person = line.split(' ')
        if int(person[1]) < 20000:
            print(f'{person[0]} - зарабатывает меньше 20 тысяч рублей')
        sum_salary += int(person[1])
    print(f'avg salary = {sum_salary / cnt}')
