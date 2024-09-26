# ----------   Урок #3   -----------
# 1.	Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
#  Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def division(arg_1, arg_2):
    '''
    Function returns the result of dividing two arguments

    :param arg_1: number 1 (e.g. 4)
    :param arg_2: number 2 (e.g. 2)
    :return: number 1 / number 2 (e.g. 2)

    '''
    try:
        result = arg_1 / arg_2
        return round(result, 2)
    except Exception as e:
        print(f'Исключительная ситуация: {e}')

print(division(4, 2))