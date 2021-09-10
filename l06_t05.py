# ----------   Урок # 6   ООП. Введение  -----------
#   5.	Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw.
# Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:

    def __init__(self, title='Instr'):
        self.title = title

    def draw(self):
        print(f'Drawing with a {self.title} has just begun!')


class Pen(Stationery):
    def draw(self):
        print(f'{self.title} drawing is a new word in painting!')


class Pencil(Stationery):
    def draw(self):
        print(f'{self.title} drawing is like the movement of a magic wand!')


class Handle(Stationery):
    def draw(self):
        print(f'{self.title} drawing - poster painting!')


brush = Stationery('brush')
handle = Handle('Handle')
pencil = Pencil('Kohinoor')
pen = Pen('Pen')
charcoal = Stationery('charcoal')


instr_list = [brush, handle, pencil, charcoal, pen]

for instr in instr_list:
    instr.draw()


