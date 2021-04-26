# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
# is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов
# TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно
# выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.


class Car:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.isPolice = False
        self.isRunning = False

    def go(self):
        if self.isRunning:
            print(f'Машина {self.name} уже в движении')
        else:
            print(f'Машина {self.name} поехала')
            self.isRunning = True

    def stop(self):
        if self.isRunning:
            print(f'Машина {self.name} остановилась')
            self.isRunning = False
        else:
            print(f'Машина {self.name} не в движении')

    def turn(self, direction):
        if self.isRunning:
            print(f'Машина {self.name} повернула {direction}')
        else:
            print(f'Машина {self.name} не в движении')

    def show_speed(self):
        if self.isRunning:
            print(f'Машина {self.name} едет со скоростью {self.speed}')
        else:
            print(f'Машина {self.name} не в движении')

    def show_info(self):
        print(f'Имя {self.name}')
        print(f'Цвет {self.color}')
        print(f'Скорость {self.speed}')
        print(f'Полиция? {self.isPolice}')


class TownCar(Car):
    def show_speed(self):
        if self.isRunning:
            if self.speed > 60:
                print(f'Машина {self.name} превышает скорость')
            print(f'Машина {self.name} едет со скоростью {self.speed}')
        else:
            print(f'Машина {self.name} не в движении')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.isRunning:
            if self.speed > 40:
                print(f'Машина {self.name} превышает скорость')
            print(f'Машина {self.name} едет со скоростью {self.speed}')
        else:
            print(f'Машина {self.name} не в движении')


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        Car.__init__(self, speed, color, name)
        self.isPolice = True


police = PoliceCar(200, 'Синяя', 'Полиция')
police.go()
police.turn('налево')
police.show_speed()
police.stop()
police.show_info()

pizzacar = WorkCar(100, 'Белая', 'Курьер')
pizzacar.go()
pizzacar.turn('направо')
pizzacar.show_speed()
pizzacar.stop()
pizzacar.show_info()