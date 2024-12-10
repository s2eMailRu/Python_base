# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class AnyClothes(ABC):
    def __init__(self):
        pass

    @property
    # работать с методом как с атрибутом,
    # применяем здесь чтобы при неверно введенных пользователем значений размера или роста
    # программа продолжиа работу в заранее заданных диапазонах значений (не меньше мин, не больше макс)
    @abstractmethod
    # обязательный для переопределения метод для потомков
    def calculation(self):
        pass

    def __add__(self, other):
        return self.calculation + other.calculation


class Coat(AnyClothes):
    def __init__(self, size):
        super().__init__()
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        min_s = 38
        max_s = 60
        if size < min_s:
            print(f'Minimum is {min_s}')
            self.__size = min_s
        elif size > max_s:
            print(f'Maximum is {max_s}')
            self.__size = max_s
        else:
            self.__size = size

    @property
    def calculation(self):
        return round((self.__size / 6.5 + 0.5), 3)


class Suit(AnyClothes):
    def __init__(self, height):
        super().__init__()
        self.height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        min_h = 125
        max_h = 210
        if height < min_h:
            print(f'Minimum is {min_h}')
            self.__height = min_h
        elif height > max_h:
            print(f'Maximum is {max_h}')
            self.__height = max_h
        else:
            self.__height = height

    @property
    def calculation(self):
        return round((2 * (self.__height / 100) + 0.3), 3)


size_1 = int(input('Input coat size:'))
coat_1 = Coat(size_1)
print(f"You'll need {coat_1.calculation} m of tissue for coat of size {coat_1.size}")
height_1 = int(input('Input height of person (in cm):'))
suit_1 = Suit(height_1)
print(f"You'll need {suit_1.calculation} m of tissue for suit for person with height {suit_1.height} sm")
print(f"All in all you'll need {coat_1 + suit_1} m of tissue")
