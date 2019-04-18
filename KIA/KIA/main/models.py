# Логика такая, мы парсим все в базу данных.
# И достаем из нее на хтмл страницу в формате орм

from django.db import models

# Create your models here.

# class Car_Model(models.Model):
#     car_name_inl = models.CharField(max_length = 80, help_text = "Модель")
#     discount = models.CharField(max_length = 20, help_text = "Скидка")
#     quantity = models.CharField(max_length = 40, help_text = 'Остаток', default = 'Остались последние модели!')
#     year = models.IntegerField(default = 2019, help_text = 'Год выпуска')
#     engine = models.CharField(max_length = 100, help_text = "Двигатель")
#     component = models.CharField(max_length = 100, help_text = "Комплектация")
#     color = models.CharField(max_length = 80, help_text = "Цвет модели")
#     # car_img =
#
#     def __str__(self):
#         return self.car_name

class Car_model_inl(models.Model):
    car_name_inl = models.CharField(max_length = 80, help_text = "Модель")
    year = models.IntegerField(default = 2019, help_text = 'Год выпуска')
    engine = models.CharField(max_length = 100, help_text = "Двигатель")
    component = models.CharField(max_length = 100, help_text = "Комплектация")
    color = models.CharField(max_length = 80, help_text = "Цвет модели")
    # car_img =

    def __str__(self):
        return self.car_name_inl


class Car_model_main(models.Model):
    car_name_main = models.CharField(max_length = 80, help_text = "Модель")
    discount = models.CharField(max_length = 20, help_text = "Скидка")
    quantity = models.CharField(max_length = 40, help_text = 'Остаток', default = 'Остались последние модели!')
    # car_img =

    def __str__(self):
        return self.car_name_main

    # Metadata
    # class Meta:
    #     ordering = ["-my_field_name"]
