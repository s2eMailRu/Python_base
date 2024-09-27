# ----------   Урок # 5  Работа с файлами   -----------
# 2.	Создать текстовый файл (не программно), сохранить в нём несколько строк,
#  выполнить подсчёт строк и слов в каждой строке.

with open("text_file_02.txt", "r", encoding='utf-8') as t_f:
    auxiliary_list = t_f.readlines()
    #print(auxiliary_list)
    print(f'в файле {t_f. name} содержится {len(auxiliary_list)} строк \n')
    for i in range(0, len(auxiliary_list)):
        num_words = auxiliary_list[i].count(' ') + 1 if len(auxiliary_list[i]) > 2 else 0
        print(f'  в строке {i + 1} \n{auxiliary_list[i]}  содержится {num_words} слов \n')