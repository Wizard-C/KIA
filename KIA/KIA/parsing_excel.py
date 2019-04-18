# a="Новый ceed"
# if "Новый ceed" == a:
#     print(1)

# Пример того как забивать инфу в БД!

# import os
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "KIA.settings")
# import django
# django.setup()
# from main.models import Car_Model
#
# result = Car_Model(
#     car_name = "optim test",
#     discount = "130 000",
#     quantity = "3",
#     year =  "2019",
#     engine =  "benzine 3.3",
#     component = "gt awd",
#     color = "red",
# )
# result.save()
# print('Good')

# S.capitalize()	Переводит первый символ строки в верхний регистр, а все остальные в нижний
# ПОЛЕЗНАЯ ХЕРНЯ

# найстройка для забивания в бд
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "KIA.settings")
import django
django.setup()
from main.models import Car_model_inl
from main.models import Car_model_main
# Библтотека для подсоса у экселя
import xlrd

# Подключение к эксельке
file = xlrd.open_workbook('kia.xls', formatting_info=True)
sheet = file.sheet_by_index(0)
len_sheet = sheet.nrows
print('Количество строк в таблице:',len_sheet)
# Вводим переменные
ceed=0
ceed_sw=0
rio=0
rio_x_line=0
stinger=0
k900=0
soul=0
picanto=0
list_car=[]

# Создаю массив машин, для того что бы удалять из него нужные машины,
# что бы подсчеты не сбились

for row_number in range(len_sheet):
    list_car.append(sheet.cell_value(row_number, 0).lower())
# print(list_car)

for row_number in range(len_sheet):
    # хуевина для оптимы
    if 'k900' in str(list_car[row_number]):
        ceed_sw+=1;
        list_car[row_number]='none';
        result_inl = Car_model_inl(
            car_name_inl = sheet.cell_value(row_number, 0).lower(),
            component = sheet.cell_value(row_number, 1).lower(),
            color = sheet.cell_value(row_number, 2).lower(),
            engine =  sheet.cell_value(row_number, 4).lower(),
            year =  sheet.cell_value(row_number, 6).lower(),
        )
        result_inl.save()
        print(1)
    # if 'ceed cd sw' in str(list_car[row_number]): ceed_sw+=1; list_car[row_number]='none'
    # if 'ceed' in str(list_car[row_number]): ceed+=1; list_car[row_number]='none'
    # if 'rio fb 5dr' in str(list_car[row_number]): rio_x_line+=1; list_car[row_number]='none' #баг каклй-то... Хз.
    # if 'rio' in str(list_car[row_number]): rio+=1; list_car[row_number]='none'
    # if 'stinger' in str(list_car[row_number]): stinger+=1; list_car[row_number]='none'
    # if 'k900' in str(list_car[row_number]): k900+=1; list_car[row_number]='none'
    # if 'soul' in str(list_car[row_number]): soul+=1; list_car[row_number]='none'
    # Нужно еще дополнить

# print('ceed', ceed)
# print('ceed sw', ceed_sw)
# print('rio', ceed)
# print('rio_x_line', rio_x_line)
# print('stinger ', stinger)
# print('k900 ', k900)
# print('soul ', soul)
# print('picanto ', picanto)

# result_inl = Car_model_inl(
#     car_name = "",
#     year =  "2019",
#     engine =  "benzine 3.3",
#     component = "gt awd",
#     color = "red",
# )
# result.save()
print('Good')


#         print(sheet.cell_value(row_number, 0).lower())
#         print(sheet.cell_value(row_number, 1).lower())
#         print(sheet.cell_value(row_number, 2).lower(), '\n')
#         i+=1
# print(i)
