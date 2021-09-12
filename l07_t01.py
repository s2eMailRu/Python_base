# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов
# класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
# складываем с первым элементом первой строки второй матрицы и т.д.
from typing import List, Any

m_1 = [[1, 20], [30, 4], [5, 60]]
m_2 = [[6, 50], [40, 3], ['2', 10]]

class Matrix:
    def __init__(self, siq):
        self.siq = siq

    def __str__(self):
        #print(self.siq)
        return '\n'.join('\t'.join([str(num) for num in el]) for el in self.siq)

    def __add__(self, other):
        print(f'MATRIX1:\n{self.__str__()}')
        print(f'MATRIX2:\n{other.__str__()}')
        try:
            aux_matr = self.siq
            for i in range(0, len(self.siq)):
                for j in range(0, len(self.siq[i])):
                    aux_matr[i][j] = int(self.siq[i][j]) + int(other.siq[i][j])
            print(f'MATRIX1 + MATRIX2 =\n{Matrix(aux_matr).__str__()}')
            return Matrix(aux_matr)
        except IndexError:
            return print('length matrix error')


matrix_1 =  Matrix(m_1)
matrix_2 =  Matrix(m_2)
matrix_1 + matrix_2