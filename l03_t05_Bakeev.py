# ----------   Урок #3   -----------
# 5.	Программа запрашивает у пользователя строку чисел, разделённых пробелом.
#  При нажатии Enter должна выводиться сумма чисел.
#  Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter.
#  Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.
#  Но если вместо числа вводится специальный символ, выполнение программы завершается.
#  Если специальный символ введён после нескольких чисел,
#  то вначале нужно добавить сумму этих чисел к полученной ранее сумме
#  и после этого завершить программу.

list_num_str = []
summma = 0    # Attention! This is a global variable

def sum_list(subsequence):
    '''
    This function returns the result of adding numbers from the resulting string or False

    :param subsequence: string with numbers separated by spaces (e.g. '1 2 3')
    :return Sum of numbers
    :return False (if there is a non-numeric character in the string (e.g. '1 2 a'))

    '''
    global summma    # Attention! This is a global variable
    list_num_str = subsequence.split()
    for el in list_num_str:
        try:
            summma = summma + int(el)
        except ValueError:
            return False
    return summma

print('\nЭта программа предназначена для суммирования введенных Вами чисел ')
i = 0
while True:
    i += 1 # для страховки от ухода в бесконечный цикл
    print('\nЕсли Вы введете любой символ отличный от числа или пробела, то программа прекратит свою работу ')
    str_of_numbers = input('Введите через пробел числа, которые вы хотите просуммировать и нажмите клавишу Enter ')
    if sum_list(str_of_numbers) and i < 30: # для страховки от ухода в бесконечный цикл
        print(f'сумма чисел {summma}')
    else:
        print('Завершаемся')
        break

print(f'итоговая сумма {summma}')