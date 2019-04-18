# a="Новый ceed"
# if "Новый ceed" == a:
#     print(1)

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "KIA.settings")
import django
django.setup()
from main.models import Car_Model

result = Car_Model(
    car_name = "optim test",
    discount = "130 000",
    quantity = "3",
    year =  "2019",
    engine =  "benzine 3.3",
    component = "gt awd",
    color = "red",
)
result.save()
print('Good')
