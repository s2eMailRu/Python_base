# ----------   Урок #3   -----------
# 3.	Реализовать функцию my_func(), которая принимает три позиционных аргумента
#  и возвращает сумму наибольших двух аргументов.

def sum_2_max_of_3 (arg_1, arg_2, arg_3):
    '''
        Function returns the result of the addition of the two maximum arguments of three

        :param arg_1: number 1 (e.g. 3)
        :param arg_2: number 2 (e.g. 5)
        :param arg_3: number 3 (e.g. -2)
        :return: max1 + max2 (e.g. =  3 + 5 = 8)

        '''
    try:
        work_list = [arg_1, arg_2, arg_3]
        work_list.remove(min(arg_1, arg_2, arg_3))
        result = work_list[0] + work_list[1]
        return result
    except Exception as e:
        print(f'Исключительная ситуация: {e}')

print(sum_2_max_of_3(3, 'n', -2))