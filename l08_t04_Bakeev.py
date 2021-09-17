# ----------   Урок # 8   ООП. Шаг третий  -----------
# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
# 5. Продолжить работу над первым заданием.
# Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
# можно использовать любую подходящую структуру, например словарь.
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.
#
# 1. Сформулировать задачу.
# 2. Определить объекты предметной области, участвующие в решении задачи.
# 3. Выделить классы, на основе которых генерируются объекты. При необходимости определить базовые классы и классы-потомки.
# 4. Установить основные атрибуты и методы объектов.
# 5. Создать классы, их атрибуты и методы.
# 6. Создать объекты классов.
# 7. Выполнить итоговое решение задачи, организовав взаимодействие объектов.
# {'invoice_num': '100', 'data': '22-02-21', 'name': 'Компьютер', 'price': 2, 'quantity': 10, 'units': 'шт'}
# {'invoice_num': '101', 'data': '23-02-21', 'name': 'Компьютер', 'price': 3, 'quantity': 15, 'units': 'шт'}
import json

class Warehouse():
    def __init__(self):
        pass

    def to_receive_into_warehouse(self):
        print('Для справки:')
        OfficeEquipment().get_info()
        print('Для получения оргтехники на склад необходимо оформить накладную.')
        invoice = {}
        sign = 'sign'
        i = 0
        while sign != '':
            num_name = int(input(f'Выберете вид оргтехники: 1 - Компьютер, 2 - Копир, 3 - Принтер '))
            if num_name == 1:
                invoice.update({'name': 'Компьютер'})
            elif num_name == 2:
                invoice.update({'name': 'Копир'})
            elif num_name == 3:
                invoice.update({'name': 'Принтер'})
            else:
                print('Ошибка Вввода')
            with open('into_warehouse.json') as r_f:
                data_list = json.load(r_f)
                print(f'для примера предидущая накладная выглядит так:\n{data_list[len(data_list) - 1]}')
            inv_data = input('Введите дату в формате "dd-mm-yy": ')
            invoice.update({'data': inv_data})
            invoice_number = int(input('Введите номер накладной как трехзначное число: '))
            invoice.update({'invoice_number': f'{invoice_number:03}'})
            quantity = int(input('Введите количество товара: '))
            invoice.update({'quantity': f'{quantity}'})
            price = int(input('Введите стоимость товара: '))
            invoice.update({'price': f'{price}'})
            storekeeper = input('Введите имя кладовщика: ')
            invoice.update({'storekeeper': storekeeper})
            supplier = input('Введите название поставщика: ')
            invoice.update({'supplier': supplier})
            print(f'мы подготовили накладную: \n{invoice}')
            sign = input('если в накладной все правильно жмите Enter, если надо что-то поправить введите любой символ')
            i += 1
            if i > 5:
                break
        data_list.append(invoice)
        with open('into_warehouse.json', "w") as wr_f:
            json.dump(data_list, wr_f)

    def to_give_out(self, data, invoice_number, name, inventory_number, storekeeper, f_r_p):
        pass


class SubdivisionOfCompany:
    def __init__(self, subdivision_name, f_r_p):
        self.subdivision_name = subdivision_name
        # f_r_p == financially_responsible_person
        self.f_r_p = f_r_p

    def to_receive_from_warehouse(self, storekeeper='A'):
        self.storekeeper = storekeeper
        print('Для справки:')
        OfficeEquipment().get_info()
        print('Для получения оргтехники необходимо оформить накладную.')
        invoice = {}
        sign = 'sign'
        i = 0
        while sign != '':
            num_name = int(input(f'Выберете вид оргтехники: 1 - Компьютер, 2 - Копир, 3 - Принтер '))
            if num_name == 1:
                invoice.update({'name': 'Компьютер'})
            elif num_name == 2:
                invoice.update({'name': 'Копир'})
            elif num_name == 3:
                invoice.update({'name': 'Принтер'})
            else:
                print('Ошибка Вввода')
            with open('from_warehouse.json') as r_f:
                data_list = json.load(r_f)
                print(f'предидущая накладная выглядит так:\n{data_list[len(data_list) - 1]}')
                print(f'будьте внимательны, Вы оформляете накладную следующую за приведенным примером,')
                num_last_invoice = data_list[len(data_list) - 1].get('invoice_number')
                for i in range(len(data_list) - 1, 0, -1):
                    #print(data_list[i])
                    if data_list[i].get('name') == invoice.get('name'):
                        inventory_number = int(data_list[i].get('inventory_number')) + 1
                        #print(inventory_number)
                        break
            inv_data = input('Введите дату в формате "dd-mm-yy": ')
            invoice.update({'data': inv_data})
            print(f'предидущая накладная имела номер {num_last_invoice}, номер Вашей накладной {(int(num_last_invoice) + 1):03}')
            my_num = int(num_last_invoice) + 1
            invoice.update({'invoice_number': f'{my_num:03}'})
            # invoice_number = int(input('Введите номер накладной как трехзначное число: '))
            # invoice.update({'invoice_number': f'{invoice_number:03}'})
            #inventory_number = int(input('Введите инвентарный номер как пятизначное число: '))
            invoice.update({'inventory_number': f'{inventory_number:05}'})
            invoice.update({'storekeeper': storekeeper})
            invoice.update({'f_r_p': self.f_r_p})
            print(f'мы подготовили накладную: \n{invoice}')
            sign = input('если в накладной все правильно жмите Enter, если надо что-то поправить введите любой символ')
            i += 1
            if i > 5:
                break
        data_list.append(invoice)
        with open('from_warehouse.json', "w") as wr_f:
            json.dump(data_list, wr_f)


class OfficeEquipment:

    def get_info(self):
        with open('into_warehouse.json') as r_f:
            data_list = json.load(r_f)
            num_comp_in = 0
            num_cop_in = 0
            num_pr_in = 0
            for el in data_list:
                #print(el)
                num_comp_in = num_comp_in + int(el.get('quantity')) if el.get('name') == 'Компьютер' else num_comp_in
                num_cop_in = num_cop_in + int(el.get('quantity')) if el.get('name') == 'Копир' else num_cop_in
                num_pr_in = num_pr_in + int(el.get('quantity')) if el.get('name') == 'Принтер' else num_pr_in
                #print(num_pr_in, num_pr_in, num_pr_in)
        with open('from_warehouse.json') as r_f:
            data_list = json.load(r_f)
            num_comp_from = 0
            num_cop_from = 0
            num_pr_from = 0
            for el in data_list:
                #print(el)
                num_comp_from = num_comp_from + 1 if el.get('name') == 'Компьютер' else num_comp_from
                num_cop_from = num_cop_from + 1 if el.get('name') == 'Копир' else num_cop_from
                num_pr_from = num_pr_from + 1 if el.get('name') == 'Принтер' else num_pr_from
                #print(num_comp_from, num_cop_from, num_pr_from)
        print(f'\tНа складе сейчас {num_comp_in - num_comp_from} компьютеров')
        print(f'\tНа складе сейчас {num_cop_in - num_cop_from} копировальных аппаратов')
        print(f'\tНа складе сейчас {num_pr_in - num_pr_from} принтеров')

class Copier(OfficeEquipment):

    def get_info_copier(self):
        print('Для справки:')
        OfficeEquipment().get_info()
        with open('into_warehouse.json') as r_f:
            data_list = json.load(r_f)
            num_cop_in = 0
            sum_cop_in = 0
            print('Все накладные на поступление Копиров:')
            for el in data_list:
                if el.get('name') == 'Копир':
                    print(el)
                    sum_cop_in = sum_cop_in + el.get('price') * el.get('quantity') if el.get('name') == 'Копир' else sum_cop_in
                    num_cop_in = num_cop_in + el.get('quantity') if el.get('name') == 'Копир' else num_cop_in
            print(f'\tсредняя цена покупки Копиров = {sum_cop_in / num_cop_in}')
        with open('from_warehouse.json') as r_f:
            data_list = json.load(r_f)
            num_cop_off = 0
            num_cop_pl = 0
            print('Все накладные на выдачу Копиров в подразделения:')
            for el in data_list:
                if el.get('name') == 'Копир':
                    print(el)
                    num_cop_off = num_cop_off + 1 if el.get('f_r_p') == 'Off' else num_cop_off
                    num_cop_pl = num_cop_pl + 1 if el.get('f_r_p') == 'Pl' else num_cop_pl
            print(f'\tВ подразделение Office выдано {num_cop_off} Копиров')
            print(f'\tВ подразделение Plant выдано {num_cop_pl} Копиров')


# d_1 = SubdivisionOfCompany('office', 'Off')
# d_1.to_receive_from_warehouse('C')

# d_2 = SubdivisionOfCompany('plant', 'Pl')
# d_2.to_receive_from_warehouse('B')

# Warehouse().to_receive_into_warehouse()

# OfficeEquipment().get_info()

# Copier().get_info_copier()