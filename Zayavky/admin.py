from django.contrib import admin
from .models import Car_mark, Car_model, Car_engin_type
# Register your models here.


admin.site.register(Car_model)
admin.site.register(Car_mark)
admin.site.register(Car_engin_type)
