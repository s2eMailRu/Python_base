# ----------   Урок # 6   ООП. Введение  -----------
# 1.	Создать класс TrafficLight (светофор).
#
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды,
# третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.
#
# Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении выводить соответствующее сообщение и завершать скрипт.
#
# цвета
# https://all-python.ru/osnovy/tsvetnoj-vyvod-teksta.html
# https://en.wikipedia.org/wiki/ANSI_escape_code
# https://stackoverflow.com/questions/287871/how-to-print-colored-text-in-terminal-in-python
#
# turtle
#

import time
import itertools

# --- simple implementation ---
# class TrafficLight:
#     __colore = 'Black'
#
#     def switching(self):
#         num = int(input('How many cycles? '))
#         print(num)
#         for _ in range(1, num + 1):
#             print('red')
#             time.sleep(1)
#             print('yellow')
#             time.sleep(0.5)
#             print('green')
#             time.sleep(1)
#             print('yellow')
#             time.sleep(0.5)
#
# my_traffic_light = TrafficLight()
# my_traffic_light.switching()

# --- second implementation ---
class TrafficLight:
    __colour = [['red', [1, 31]], ['yellow', [0.5, 33]], ['green', [1, 32]], ['yellow', [0.5, 33]]]

    def switching(self):
        num = int(input('How many cycles? '))
        for _ in range(1, num + 1):
            for colour in self.__colour:
                print(f'\033[{colour[1][1]}m\033[1m{colour[0]}\033[0m')
                time.sleep(colour[1][0])

my_traffic_light = TrafficLight()
my_traffic_light.switching()


# --- third implementation ---
# my_traffic_light = TrafficLight()
# my_traffic_light.switching()
#
# class TrafficLight:
#     __colore = [['red', [1, 31]], ['yellow', [0.5, 33]], ['green', [1, 32]], ['yellow', [0.5, 33]]]
#
#     def switching(self):
#         num = int(input('How many cycles? '))
#         #print(num)
#         i = 0
#         #for _ in range(1, num + 1):
#         for colure in itertools.cycle(self.__colore):
#             print(f'\r\033[{colure[1][1]}m\033[1m{colure[0]}\033[0m', end='')
#             time.sleep(colure[1][0])
#             i += 1
#             if i > num * 3:
#                 break
#
# my_traffic_light = TrafficLight()
# my_traffic_light.switching()

