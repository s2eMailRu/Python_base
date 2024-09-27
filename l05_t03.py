# ----------   Урок # 5  Работа с файлами   -----------
# 3.	Создать текстовый файл (не программно).
# Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников. Пример файла:
# Иванов 23543.12
# Петров 13749.32

with open("text_file_03.txt", "r", encoding='utf-8') as t_f:
    auxiliary_list = t_f.readlines()
    sallary_less_20 = [sirname for sirname in auxiliary_list if float(sirname[-9: -1]) < 20000]
    #print(sallary_less_20)
    for person in sallary_less_20:
        pos = person.find(' ')
        print(f'сотрудник {person[0: pos]} имеет з/пл {person[pos + 1: -1]} ')
    sallary = [float(person[-9: -1]) for person in auxiliary_list]
    av_sallary = round(sum(sallary) / len(sallary), 2)
    print(f'средняя з/пл сотрудников составляет {av_sallary}')