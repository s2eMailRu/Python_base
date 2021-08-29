# ----------   Урок #3   -----------
# 4.	Программа принимает действительное положительное число x и целое отрицательное число y.
#  Выполните возведение числа x в степень y. Задание реализуйте в виде функции my_func(x, y).
#  При решении задания нужно обойтись без встроенной функции возведения числа в степень.
#   Подсказка: попробуйте решить задачу двумя способами.
#   Первый — возведение в степень с помощью оператора **.
#   Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

def any_exponentiation(arg_1, arg_2):
    '''
        Function returns the result of raising the first argument to the power of the second.
        Second number can be any integer number (positive or negative)

        :param arg_1: number 1 (e.g. 2)
        :param arg_2: number 2 (e.g. -2)
        :return: max1 + max2 (e.g. =  2 ** (-2) = 1 / 4 = 0.25)

    '''
    try:
        x = float(arg_1)
        y = int(arg_2)
        result = 1 / (x ** abs(y)) if y < 0 else x ** y
        return round(result, 5)
    except Exception as e:
            print(f'Исключительная ситуация: {e}')

def negative_exponentiation(arg_1, arg_2):
    '''
        Function returns the result of raising the first argument to the power of the second,
        if the second argument is negative

        :param arg_1: number 1 (e.g. 2)
        :param arg_2: number 2 (e.g. -2)
        :return: max1 + max2 (e.g. =  2 ** (-2) = 1 / 4 = 0.25)

    '''
    try:
        x = float(arg_1)
        y = int(arg_2)
        if y > 0:
            return None
        else:
            result = 1
            for i in range(0, abs(y)):
                result = result * (1 / x)
            return round(result, 5)
    except Exception as e:
            print(f'Исключительная ситуация: {e}')

number_1 = input('Введите действительное положительное число x ')

number_2 = input('Введите целое отрицательное число y ')

print(f'первый способ возведения числа {number_1} в степень {number_2} дал результат {any_exponentiation(number_1, number_2)}')

print(f'второй способ возведения числа {number_1} в степень {number_2} дал результат {negative_exponentiation(number_1, number_2)}')
