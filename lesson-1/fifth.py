revenue = int(input('Введите выручку - '))
costs = int(input('Введите издежки - '))
if revenue > costs:
    profit = revenue - costs
    print('выручка больше издержек, и прибыль составила - ', profit)
    print('Рентабельность выручки - ', (profit/revenue)*100, '%', sep='')
    staff = int(input('Введите количество сотрудников - '))
    print('Прибыль на одного сотрудника составила - ', profit/staff)
elif revenue < costs:
    print('Прибыль мееньше издержек, убыток составил -', costs-revenue)
else:
    print('Выручка равна издержкам')
