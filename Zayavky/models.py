from django.db import models

class Car_mark(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name.title()

    class Meta:
        verbose_name = 'Марка'
        verbose_name_plural = 'Марки'


class Car_model(models.Model):
    model = models.ForeignKey(Car_mark, on_delete = models.CASCADE)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name.title()

    class Meta:
        verbose_name = 'Модель'
        verbose_name_plural = 'Модели'





class Car_engin_type(models.Model):
    engin = models.ForeignKey(Car_model, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name.title()

    class Meta:
        verbose_name = 'Двигатель'
        verbose_name_plural = 'Двигатели'

