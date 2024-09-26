# ----------   Урок # 4  Полезные инструменты   -----------
# 4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке.
# Для выполнения задания обязательно использовать генератор.
# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]

origin_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

print(f'исходный список {origin_list}')

result_list = [el for el in origin_list if (origin_list.count(el)) < 2]

print(f'итоговый список по первому варианту {result_list}')

result_list = []

result_list = [origin_list[i] for i in range(0, len(origin_list)) if (origin_list.count(origin_list[i])) < 2]

print(f'итоговый список по второму варианту {result_list}')