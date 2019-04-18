from django.contrib import admin

from .models import Car_model_inl
from .models import Car_model_main

admin.site.register(Car_model_inl)
admin.site.register(Car_model_main)
