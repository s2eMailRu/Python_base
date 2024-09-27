# ----------   Урок # 6   ООП. Введение  -----------
#   2.	Реализовать класс Road (дорога).
#
# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги; использовать формулу:
# длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см*число см толщины полотна;
# проверить работу метода.
#
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.

class AsphaltRoad:
    def __init__(self, length=5000, width=20):
        self._l = length
        self._w = width
        print(f'You create a road, which length is {self._l} m , and width is {self._w} m ')

    def full_asphalt_mass(self, mass=25, height=5):
        f_a_m = (self._l * self._w * mass * height) / 1000
        print(f'Asphalt mass is: {self._l} m * {self._w} m * {mass} kg * {height} sm = {f_a_m} ton')

my_road = AsphaltRoad()
my_road.full_asphalt_mass()





