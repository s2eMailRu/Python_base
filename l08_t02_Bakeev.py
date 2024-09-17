# ----------   Урок # 8   ООП. Шаг третий  -----------
# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию
# и не завершиться с ошибкой.

class MyExcptn(Exception):
    def __init__(self, txt):
        self.txt = txt


def division(arg_1, arg_2):
    '''
    Function returns the result of dividing two arguments

    :param arg_1: number 1 (e.g. 4)
    :param arg_2: number 2 (e.g. 2)
    :return: number 1 / number 2 (e.g. 2)

    '''
    print(f'you want to divide {arg_1} by {arg_2}')
    try:
        num_1 = int(arg_1)
        num_2 = int(arg_2)
        if num_2 == 0:
            raise MyExcptn('Division by 0 !!!')
    except (ValueError, MyExcptn) as err:
        print(err)
    else:
        result = num_1 / num_2
        return round(result, 2)


num_1 = input('Enter the number to be divided ')
num_2 = input('Enter the divisor ')

print(f'result: {division(num_1, num_2)}')
#division(3, 0)