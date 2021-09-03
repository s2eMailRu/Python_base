# ----------   Урок # 4  Полезные инструменты   -----------
# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce

def multiply(arg1, arg2):
    return arg1 * arg2


test_list = [el for el in range(100, 1001, 2)]
#print(test_list)

result_0 = 1    # В лоб посчитал произведения всех элементов test_list. Результат непостижимо огромный
for i in range(0, len(test_list) - 1):
    result_0 = result_0 * multiply(test_list[1], test_list[i+1])
#print(result)

result_1 = reduce(multiply, test_list)

print(result_1 - result_0) if result_1 == result_0 else print('не совпало!')

result_2 = reduce(lambda m, n: m * n, [el for el in range(100, 1001, 2)])

print(f'разница двух решений через reduce = {result_2 - result_1}') if result_2 == result_1 else print('не совпало!')

print(result_2 - result_0) if result_2 == result_0 else print('не совпало!')




