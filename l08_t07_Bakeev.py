# ----------   Урок # 8   ООП. Шаг третий  -----------
# 7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа)
# z1 + z2 = x1 + i y1 + x2 + i y2 = x1 + x2 + i (y1 + y2) ,
# z1 * z2 = (x1 + i y1) (x2 + i y2) = x1x2 – y1y2 + i (x1y2 + x2y1)
# и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.

class MyComplexNumber:
    def __init__(self, nums):
        self.nums = nums

    def print_c_n(self):
        return f'{self.nums[0]} + {self.nums[1]}*i'

    def __add__(self, other):
        real_part = self.nums[0] + other.nums[0]
        imaginary_part = self.nums[1] + other.nums[1]
        return MyComplexNumber((real_part, imaginary_part))

    def __mul__(self, other):
        real_part = self.nums[0] * other.nums[0] - self.nums[1] * other.nums[1]
        imaginary_part = self.nums[0] * other.nums[1] + self.nums[1] * other.nums[0]
        return MyComplexNumber((real_part, imaginary_part))


real_part = int(input('Input real_part of Complex Number: '))
imaginary_part = int(input('Input imaginary_part of Complex Number: '))
compl_num_1 = (real_part, imaginary_part)
#compl_num_1 = (int(input('Input real_part of  ')), int(input('Input imaginary_part of Complex Number: ')))
# compl_num_1 = (3, 3)
c_n_1 = MyComplexNumber(compl_num_1)
print(f'You have entered Complex Number: {c_n_1.print_c_n()}')
compl_num_2 = (1, 1)
c_n_2 = MyComplexNumber(compl_num_2)
compl_num_3 = (2, 2)
c_n_3 = MyComplexNumber(compl_num_3)
print(f"I will make test: let's add your number with {c_n_2.print_c_n()} and {c_n_3.print_c_n()}")
c_n_add = c_n_1 + c_n_2 + c_n_3
print(f"Sum of complex numbers ({c_n_1.print_c_n()}) + ({c_n_2.print_c_n()}) + ({c_n_3.print_c_n()}) is:")
print('\t', c_n_add.print_c_n())
print(f"I will make test: let's multiply your number with {c_n_2.print_c_n()} and {c_n_3.print_c_n()}")
c_n_mult = c_n_1 * c_n_2 * c_n_3
print(f"Multiply of complex numbers ({c_n_1.print_c_n()}) * ({c_n_2.print_c_n()}) * ({c_n_3.print_c_n()}) is:")
print('\t', c_n_mult.print_c_n())

