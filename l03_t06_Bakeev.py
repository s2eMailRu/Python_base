# ----------   Урок #3   -----------

# тестовая строка для задачи        nice авп ъghj jапро hjjпаро вапрghgh cool

# 6.	Реализовать функцию int_func(),
# принимающую слова из маленьких латинских букв и возвращающую их же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# 7.	Продолжить работу над заданием.
# В программу должна попадать строка из слов, разделённых пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Нужно сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Используйте написанную ранее функцию int_func().

def int_func(any_string):
    '''
    This function finds words in the input string that contain only Latin letters
    and capitalizes the first letter of this word

    :param any_string: string with words separated by spaces (e.g. 'nice авп')
    :return result_string: (e.g. 'Nice авп')
    '''
    try:
        result_str = ''
        result_list = any_string.split()
        # print(result_list)
        for word in result_list:
            counter = 0
            for char in word:
                if 96 < ord(char) < 123:
                    # print(ord(char))
                    counter += 1
                    # print(sign)
            result_str = (result_str + word.capitalize() + ' ') if len(word) == counter else (result_str + word + ' ')
            # print(result_str)
        return result_str
    except Exception as e:
        print(f'Исключительная ситуация: {e}')


print('тестируем функцию с помощью строки: "nice   авп ъghj jапро   hjjпаро вапрghgh cool"')
s = int_func('nice авп ъghj jапро hjjпаро вапрghgh cool')
print(f'результат: {s}')
