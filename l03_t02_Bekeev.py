# ----------   Урок #3   -----------
# 2.	Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя:
#  имя, фамилия, год рождения, город проживания, email, телефон.
#  Функция должна принимать параметры как именованные аргументы.
#  Осуществить вывод данных о пользователе одной строкой.

def customer(first_name, second_name, y_of_b, town, e_mail, phone):
    '''
        Function prints information about customer in one line
        and returns customer information as a tuple
    '''
    try:
        print(f'first_name: {first_name}; second_name: {second_name}; year of birthday: {y_of_b}; place of residence: {town}; e-mail: {e_mail}; phone: {phone}')
        return first_name, second_name, y_of_b, town, e_mail, phone
    except Exception as e:
        print(f'Исключительная ситуация: {e}')

print(customer(y_of_b = 2000, first_name = 'A', second_name = 'B', town = 'C', e_mail = 'd@e.com', phone = '+1(234)567890'))

#first_name = input('Enter your first_name ')
#second_name = input('Enter your second_name ')
#y_of_b = input('Enter your year of birthday ')
#town = input('Enter your place of residence ')
#e_mail = input('Enter your e_mail ')
#phone = input('Enter your phone ')







