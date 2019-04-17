# Логика такая, мы парсим все в базу данных.
# И достаем из нее на хтмл страницу в формате орм

from django.db import models

# Create your models here.

class MyModelName(models.Model):
    car_name = models.CharField(max_length=255, help_text="")
    discount = models.CharField(max_length=20, help_text="Enter field documentation")
    quantity =
    year =
    engine =
    component =
    color =
    car_img =


    # Metadata
    class Meta:
        ordering = ["-my_field_name"]

    def __str__(self):
        return self.field_name
