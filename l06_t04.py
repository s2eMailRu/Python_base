# ----------   Урок # 6   ООП. Введение  -----------
#   4.	Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что
# машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.

import random

class Car:
    def __init__(self, speed, colour, name, model, is_police=False):
        self.speed = speed
        self.colour = colour
        self.name = name
        self.model = model
        self.is_police = is_police

    def info(self):
        print(f'This is a {self.name} car, model: {self.model}, colour: {self.colour}')

    def go(self):
        print(f'{self.model} went')

    def stop(self):
        print(f'{self.model} has stopped \n')

    def turn(self, direction='right'):
        print(f'{self.model} has turned {direction} ')

    def show_speed(self):
        return f'{self.model} speed is {self.speed}'


class TownCar(Car):
    """ Town Car """

    def show_speed(self):
        return(f'{self.model} is exceeding the speed limit by {self.speed - 60} km / h! ' if self.speed > 60 else super().show_speed())


class WorkCar(Car):
    """ Work Car """

    def show_speed(self):
        return(f'{self.model} is exceeding the speed limit by {self.speed - 40} km / h! ' if self.speed > 40 else super().show_speed())


class SportCar(Car):
    """ Sport Car """


class PoliceCar(Car):
    """ Police Car """

    def __init__(self, speed, colour, name, model, is_police=True):
        super().__init__(speed, colour, name, model, is_police)

    def info(self):
        print(f'This is a police car, model: {self.model}, colour: {self.colour}')


direction_variants = ['right', 'left', 'back']
col_var = ['white', 'red', 'green', 'yellow', 'blue', 'black']
sm_m_var = ['Lexus', 'Mazda', 'Ferrari', 'BMW', 'Ford']
big_m_var = ['MAN', 'VOLVO', 'ISUZU', 'KAMAZ']


town_car = TownCar(random.randint(40, 100), random.choice(col_var), 'town', random.choice(sm_m_var))
work_car = WorkCar(random.randint(20, 80), random.choice(col_var), 'work', random.choice(big_m_var))
sport_car = SportCar(random.randint(90, 200), f'silver-{random.choice(col_var)}', 'sport', random.choice(sm_m_var))
police_car = PoliceCar(random.randint(40, 120), 'white-blue', 'police', random.choice(sm_m_var))

car_list = [town_car, work_car, sport_car, police_car]

for car in car_list:
    car.info()
    car.go()
    car.turn(random.choice(direction_variants))
    print(car.show_speed())
    car.stop()