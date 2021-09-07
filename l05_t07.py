# ----------   Урок # 5  Работа с файлами   -----------
# 7.	Создать вручную и заполнить несколькими строками текстовый файл,
# в котором каждая строка будет содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1   ООО   10000   5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчёт средней прибыли её не включать. Далее реализовать список.
# Он должен содержать словарь с фирмами и их прибылями,  а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить её в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.

import json

with open("text_file_07.txt", "r", encoding='utf-8') as t_f:
    auxiliary_list = t_f.readlines()
    print(f'на входе достаем из файла {t_f.name} список: {auxiliary_list} ')
    subj_dict = {}
    t_d = {}
    res_list = []
    for el in auxiliary_list:
        subj_list = el.split()
        profit = int(subj_list[2]) - int(subj_list[3])
        t_d = {subj_list[0]: profit}
        subj_dict.update(t_d)
    res_list.append(subj_dict)
    t_d = {'averege profit': sum(subj_dict.values())}
    res_list.append(t_d)
    print(f'на выходе имеем список: {res_list}')
    with open("json_file_07.json", "w", encoding='utf-8') as j_f:
        print(f'и на последок сериализуем данные в файл: {j_f.name}')
        json.dump(res_list, j_f, ensure_ascii=False)



