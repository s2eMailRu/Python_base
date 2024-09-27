# ----------   Урок # 5  Работа с файлами   -----------
# 4.	Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

# pip install googletrans==3.1.0a0
# from googletrans import translater
# не успел разобраться, !ДОДЕЛАТЬ в выходные

dict_04 = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре', 'Five': 'Пять'}

with open("text_file_04.txt", "r", encoding='utf-8') as t_f:
    auxiliary_list = t_f.readlines()
    print(f'берем из файла {t_f.name}: {auxiliary_list}')
    with open("transl_text_file_04.txt", "w", encoding='utf-8') as tr_f:
        for el in auxiliary_list:
            num = el[0:el.index(' ')]
            print(f'пишем в файл {tr_f.name}: {dict_04.get(num)} {el[-4:-1]}')
            tr_f.writelines(f'{dict_04.get(num)} {el[-4:-1]}\n')
