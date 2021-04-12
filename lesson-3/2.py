# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

#P.S. Я не особо понимаю суть задачи


person = lambda **kwargs: kwargs


def person2(**kwargs):
    print(kwargs.items())


def person3(name, surname, birtday, city, email, phone):
    return f'Name - {name}| Surname - {surname}| Birtday - {birtday}| City - {city}| Email - {email}| Phone - {phone}'


a = input('Вводите данные в формате: Name=NAME Surname=SURNAME ... ').split(' ')
b = {}
for i in range(0,len(a)):
    b[(a[i].split('='))[0]] = a[i].split('=')[1]
print(person(**b))
person2(**b)
print(person3(name='ALEX', surname='SHVED', birtday='24.10.1992', city='Spb', email='hello@world.com', phone='+5553654'))