# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и
# премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом
# премии (get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров).


class Worker:

    __income = dict(wage=0, bonus=0)

    def __init__(self,name,surname,position,wage,bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income.update({'wage': wage, 'bonus': bonus})

    def get_data_wage(self):
        return self.__income.get('wage')

    def get_data_bonus(self):
        return self.__income.get('bonus')


class Position(Worker):
    def get_full_name(self):
      print(f'full_name: {self.name} {self.surname}')

    def get_total_income(self):
        print('total_income = ', self.get_data_wage() + self.get_data_bonus())


man=Position('Alex', 'Shved', 'admin', 10, 10)
man.get_full_name()
man.get_total_income()
