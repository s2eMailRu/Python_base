# ----------   Урок # 5  Работа с файлами   -----------
# 5.	Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

import random

random_str = ' '.join([str(random.randint(0, 100)) for _ in range (0, random.randint(10, 20))])
print(f'строка чисел, которую мы будем записывать в файл: \n{random_str}')
r_l = [int(el) for el in random_str.split(' ')]
print(f'ДЛЯ ПРОВЕРКИ! Сумма чисел в изначальной строке: {sum(r_l)}')

with open("text_file_05.txt", "w+") as t_f:
    t_f.writelines(random_str + '\n')
    t_f.seek(0)
    second_random_list = [int(el) for el in t_f.readline().split(' ')]
    print(f'сумма чисел находящихся в строке созданного файла {t_f.name}: {sum(second_random_list)}')
