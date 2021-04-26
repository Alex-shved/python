# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
# зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего
# (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке
# (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее
# сообщение и завершать скрипт.


import time


class TrafficLight:

    __light_sleep = dict(red=[1, 0], yellow=[2, 1], green=[3, 2])
    __order = 0

    def auto_action_light(self):
        for i in self.__light_sleep:
            print(i)
            time.sleep(self.__light_sleep.get(i)[0])
            print('-'*30)

    def manual_action_light(self, color):
        if color not in self.__light_sleep.keys():
            print('не допустимый цвет')
            return 0
        if self.__order == int(self.__light_sleep.get(color)[1]):
            print(color)
            __order = self.__light_sleep.get(color)[1]
            time.sleep(self.__light_sleep.get(color)[0])
            if self.__order == 2:
                self.__order = 0
            else:
                self.__order += 1
        else:
            print("Порядок включения цветов светофора неверен")




work = TrafficLight()
#while True:
#    work.auto_action_light()
#    if input('Завершить работу светофора ? [y/n]').upper() == 'Y':
#        break
while True:
    work.manual_action_light(input('Введите цвет - '))
