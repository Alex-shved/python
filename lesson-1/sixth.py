#6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. Каждый день
# спортсмен увеличивал результат на 10 % относительно предыдущего. Требуется определить номер дня, на который общий
# результат спортсмена составить не менее b километров. Программа должна принимать значения параметров a и b и выводить
# одно натуральное число — номер дня.

a = float(input('Сколько пробежал за первый день - '))
b = float(input('Цель пробежки за день - '))
cnt = 1
while b > a:
    a = a+a/10
    cnt += 1
print(f'на {cnt}-й день спортсмен достиг результата — не менее {b} км.')