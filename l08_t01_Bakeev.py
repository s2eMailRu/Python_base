# ----------   Урок # 8   ООП. Шаг третий  -----------
# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату
# в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год
# и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года
# (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

# class MyExcptn(Exception):
#     def __init__(self, txt):
#         self.txt = txt

class MyData:
    #def d_1(self,data):
    def __init__(self, siq):
        self.siq = siq

    @staticmethod
    def validation(str_1):
        '''
             This function check data format according to format "dd-mm-yy"
                :param param_1:
                :return:
        '''
        i = 0
        print(str_1)
        try:
            if len(str_1) == 8:
                if str_1[2:3] == '-' and str_1[5:6] == '-':
                    if str_1.replace('-','').isdecimal():
                        if 0 < int(str_1[0:2]) < 32 and 0 < int(str_1[3:5]) < 13 and 0 < int(str_1[6:]):
                            pass
                        else:
                            print(str_1[0:2], str_1[3:5], str_1[6:])
                            print('Wrong range of numbers')
                            i += 1
                    else:
                        print(str_1.replace('-',''))
                        print('Wrong numbers - some of them are not numbers')
                        i += 1
                else:
                    print(str_1[2:3], str_1[5:6])
                    print('Wrong format of input')
                    i += 1
            else:
                print(f'Wrong length of str, it should be 8 symbols, but now it is {len(str_1)} symbols')
                i += 1
            return True if i < 1 else False
        except Exception as err:
            print(err)

    @classmethod
    def d_1(cls, arg):
        #print(MyData.validation(param_1))
        if MyData.validation(arg):
            aux_list = arg.split('-')
            day = int(aux_list[0])
            month = int(aux_list[1])
            year = int(aux_list[2])
            print(f'{arg} -> day: {day:02}, month: {month:02}, year: {year}')
            return [day, month, year]
        else:
            return []

data = input('enter data in "dd-mm-yy" format ')
#data = '01-11+O2'
m_d = MyData(data)
m_d.d_1(data)