# ----------   Урок # 6   ООП. Введение  -----------
#   3.	Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров.

# Немножко разовьем задачу.
# У меня wage_rate будет ставкой почасовой оплаты и для того чтобы получить полный доход
# при вызове get_total_income надо передать количество отработанных часов,
# если эти данные не будут преданы, то программа решит что рабочих часов не было
# и сотруднику пологается только премия

class Worker:
    def __init__(self, name, surname, position, wage_rate, bonus):
        self.n = name
        self.s = surname
        self.p = position
        self.income = {'wage_rate': wage_rate, 'bonus': bonus}

class Position(Worker):
    def get_full_name(self):
        return self.n, self.s, self.p

    def get_total_income(self, hours_worked = 0):
        print(f'According to you data, hours worked by {self.n} {self.s}: {hours_worked}')
        sum = self.income.get('wage_rate') * hours_worked + self.income.get('bonus')
        return sum

teacher_1 = Position('Kate', 'Smith', 'Professor', 100, 200)

print(f'{teacher_1.get_full_name()[0]} {teacher_1.get_full_name()[1]} - {teacher_1.get_full_name()[2]}')
print(f'Total income is {teacher_1.get_total_income(20)}')

teacher_2 = Position('Jhon', 'Smith', 'Lecturer', 50, 100)

print(f'{teacher_2.get_full_name()[0]} {teacher_2.get_full_name()[1]} - {teacher_2.get_full_name()[2]}')
print(f'Total income is {teacher_2.get_total_income(0)}')
