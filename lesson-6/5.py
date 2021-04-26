# 5. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов реализовать
# переопределение метода draw. Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.


class Stationery:

    def __init__(self, title=''):
        self.title = title

    def drow(self):
        print("Запуск отрисовки.")


class Pen(Stationery):
    def drow(self):
        print(f'Запуск отрисовки {self.title}.')


class Pencil(Stationery):
    def drow(self):
        print(f'Запуск отрисовки {self.title}.')


class Handle(Stationery):
    def drow(self):
        print(f'Запуск отрисовки {self.title}.')


stationery = Stationery()
pen = Pen('ручкой')
pencil = Pencil('карандашом')
handle = Handle('маркером')

stationery.drow()
pen.drow()
pencil.drow()
handle.drow()



