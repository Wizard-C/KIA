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

#  Для того что бы оставить поле в базе данных пустой
#  blank=True, null=True
# найстройка для забивания в бд
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "KIA.settings")
import django
django.setup()
from main.models import Car_model_inl
from main.models import Car_model_main
# Библтотека для подсоса у экселя
import xlrd
# для парсинга сайта
# from BeautifulSoup , import BeautifulSoup

# Подключение к эксельке
file = xlrd.open_workbook('kia.xls', formatting_info=True)
sheet = file.sheet_by_index(0)
len_sheet = sheet.nrows
print('Количество строк в таблице:',len_sheet)

# Вводим переменные
rio_x_line=0
rio=0
stinger=0
k900=0
picanto=0
soul=0
ceed_sw=0
ceed=0
sportage=0
sorento_prime=0
sorento=0
cerato=0
cerato_new=0
mohave=0
optima=0

list_car=[]

# Создаю массив машин, для того что бы удалять из него нужные машины,
# что бы подсчеты не сбились
for row_number in range(len_sheet):
    list_car.append(sheet.cell_value(row_number, 0).lower())

for row_number in range(len_sheet):
    if 'rio fb 5dr (х/б)' in str(list_car[row_number]):
        rio_x_line += 1;
        list_car[row_number]='none';
        # result_inl = Car_model_inl(
        #     car_name_inl = sheet.cell_value(row_number, 0).lower(),
        #     component = sheet.cell_value(row_number, 1).lower(),
        #     color = sheet.cell_value(row_number, 2).lower(),
        #     engine =  sheet.cell_value(row_number, 4).lower(),
        #     year =  sheet.cell_value(row_number, 6).lower(),
        # )
        # result_inl.save()

    if 'rio' in str(list_car[row_number]):
        rio += 1;
        list_car[row_number] = 'none';
        # result_inl = Car_model_inl(
        #     car_name_inl = sheet.cell_value(row_number, 0).lower(),
        #     component = sheet.cell_value(row_number, 1).lower(),
        #     color = sheet.cell_value(row_number, 2).lower(),
        #     engine =  sheet.cell_value(row_number, 4).lower(),
        #     year =  sheet.cell_value(row_number, 6).lower(),
        # )
        # result_inl.save()

    if 'stinger' in str(list_car[row_number]):
        stinger += 1;
        list_car[row_number] = 'none';
        # result_inl = Car_model_inl(
        #     car_name_inl = sheet.cell_value(row_number, 0).lower(),
        #     component = sheet.cell_value(row_number, 1).lower(),
        #     color = sheet.cell_value(row_number, 2).lower(),
        #     engine =  sheet.cell_value(row_number, 4).lower(),
        #     year =  sheet.cell_value(row_number, 6).lower(),
        # )
        # result_inl.save()

    if 'k900' in str(list_car[row_number]):
        k900 += 1;
        list_car[row_number] = 'none';
        # result_inl = Car_model_inl(
        #     car_name_inl = sheet.cell_value(row_number, 0).lower(),
        #     component = sheet.cell_value(row_number, 1).lower(),
        #     color = sheet.cell_value(row_number, 2).lower(),
        #     engine =  sheet.cell_value(row_number, 4).lower(),
        #     year =  sheet.cell_value(row_number, 6).lower(),
        # )
        # result_inl.save()

    if 'picanto' in str(list_car[row_number]):
        picanto += 1;
        list_car[row_number] = 'none';
        # result_inl = Car_model_inl(
        #     car_name_inl = sheet.cell_value(row_number, 0).lower(),
        #     component = sheet.cell_value(row_number, 1).lower(),
        #     color = sheet.cell_value(row_number, 2).lower(),
        #     engine =  sheet.cell_value(row_number, 4).lower(),
        #     year =  sheet.cell_value(row_number, 6).lower(),
        # )
        # result_inl.save()

    if 'soul' in str(list_car[row_number]):
        soul += 1;
        list_car[row_number] = 'none';
        # result_inl = Car_model_inl(
        #     car_name_inl = sheet.cell_value(row_number, 0).lower(),
        #     component = sheet.cell_value(row_number, 1).lower(),
        #     color = sheet.cell_value(row_number, 2).lower(),
        #     engine =  sheet.cell_value(row_number, 4).lower(),
        #     year =  sheet.cell_value(row_number, 6).lower(),
        # )
        # result_inl.save()

    if 'ceed cd sw' in str(list_car[row_number]):
        ceed_sw += 1;
        list_car[row_number] = 'none';
        # result_inl = Car_model_inl(
        #     car_name_inl = sheet.cell_value(row_number, 0).lower(),
        #     component = sheet.cell_value(row_number, 1).lower(),
        #     color = sheet.cell_value(row_number, 2).lower(),
        #     engine =  sheet.cell_value(row_number, 4).lower(),
        #     year =  sheet.cell_value(row_number, 6).lower(),
        # )
        # result_inl.save()

    if 'ceed' in str(list_car[row_number]):
        ceed += 1;
        list_car[row_number] = 'none';
        # result_inl = Car_model_inl(
        #     car_name_inl = sheet.cell_value(row_number, 0).lower(),
        #     component = sheet.cell_value(row_number, 1).lower(),
        #     color = sheet.cell_value(row_number, 2).lower(),
        #     engine =  sheet.cell_value(row_number, 4).lower(),
        #     year =  sheet.cell_value(row_number, 6).lower(),
        # )
        # result_inl.save()

    if 'sportage' in str(list_car[row_number]):
        sportage += 1;
        list_car[row_number] = 'none';
        # result_inl = Car_model_inl(
        #     car_name_inl = sheet.cell_value(row_number, 0).lower(),
        #     component = sheet.cell_value(row_number, 1).lower(),
        #     color = sheet.cell_value(row_number, 2).lower(),
        #     engine =  sheet.cell_value(row_number, 4).lower(),
        #     year =  sheet.cell_value(row_number, 6).lower(),
        # )
        # result_inl.save()

    #
    # ВОТ ТУТ ВАЖНЫЙ ВОПРОС, SORENTO UM PE ЭТО PRIME ИЛИ CLASSIC
    # если я перепутал, то нужно просто поменять местами условия if
    #
    if 'xm sorento' in str(list_car[row_number]):
        sorento += 1;
        list_car[row_number] = 'none';
        # result_inl = Car_model_inl(
        #     car_name_inl = sheet.cell_value(row_number, 0).lower(),
        #     component = sheet.cell_value(row_number, 1).lower(),
        #     color = sheet.cell_value(row_number, 2).lower(),
        #     engine =  sheet.cell_value(row_number, 4).lower(),
        #     year =  sheet.cell_value(row_number, 6).lower(),
        # )
        # result_inl.save()

    if 'sorento' in str(list_car[row_number]):
        sorento_prime += 1;
        list_car[row_number] = 'none';
        # result_inl = Car_model_inl(
        #     car_name_inl = sheet.cell_value(row_number, 0).lower(),
        #     component = sheet.cell_value(row_number, 1).lower(),
        #     color = sheet.cell_value(row_number, 2).lower(),
        #     engine =  sheet.cell_value(row_number, 4).lower(),
        #     year =  sheet.cell_value(row_number, 6).lower(),
        # )
        # result_inl.save()

    #
    # ВОТ ТУТ ВАЖНЫЙ ВОПРОС, CERATO YD PE ЭТО calssic ИЛИ new
    # если я перепутал, то нужно просто поменять местами условия if
    #
    if 'cerato bd' in str(list_car[row_number]):
        cerato += 1;
        list_car[row_number] = 'none';
        # result_inl = Car_model_inl(
        #     car_name_inl = sheet.cell_value(row_number, 0).lower(),
        #     component = sheet.cell_value(row_number, 1).lower(),
        #     color = sheet.cell_value(row_number, 2).lower(),
        #     engine =  sheet.cell_value(row_number, 4).lower(),
        #     year =  sheet.cell_value(row_number, 6).lower(),
        # )
        # result_inl.save()

    if 'cerato' in str(list_car[row_number]):
        cerato_new += 1;
        list_car[row_number] = 'none';
        # result_inl = Car_model_inl(
        #     car_name_inl = sheet.cell_value(row_number, 0).lower(),
        #     component = sheet.cell_value(row_number, 1).lower(),
        #     color = sheet.cell_value(row_number, 2).lower(),
        #     engine =  sheet.cell_value(row_number, 4).lower(),
        #     year =  sheet.cell_value(row_number, 6).lower(),
        # )
        # result_inl.save()

    # Этих вообще нет
    if 'mohave' in str(list_car[row_number]):
        mohave += 1;
        list_car[row_number] = 'none';
        # result_inl = Car_model_inl(
        #     car_name_inl = sheet.cell_value(row_number, 0).lower(),
        #     component = sheet.cell_value(row_number, 1).lower(),
        #     color = sheet.cell_value(row_number, 2).lower(),
        #     engine =  sheet.cell_value(row_number, 4).lower(),
        #     year =  sheet.cell_value(row_number, 6).lower(),
        # )
        # result_inl.save()

    if 'optima' in str(list_car[row_number]):
        optima += 1;
        list_car[row_number] = 'none';
        # result_inl = Car_model_inl(
        #     car_name_inl = sheet.cell_value(row_number, 0).lower(),
        #     component = sheet.cell_value(row_number, 1).lower(),
        #     color = sheet.cell_value(row_number, 2).lower(),
        #     engine =  sheet.cell_value(row_number, 4).lower(),
        #     year =  sheet.cell_value(row_number, 6).lower(),
        # )
        # result_inl.save()

print('rio line: ', rio_x_line)
print('rio: ', rio)
print('stinger: ', stinger)
print('k900: ', k900)
print('picanto: ', picanto)
print('soul: ', soul)
print('ceed sw: ', ceed_sw)
print('ceed: ', ceed)
print('sportage: ', sportage)
print('sorento: ', sorento)
print('sorento prime: ', sorento_prime)
print('cerato: ', cerato)
print('cerato_new: ', cerato_new)
print('mohave: ', mohave)
print('optima: ', optima)

print('Good')
