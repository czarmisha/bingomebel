from django.db import models


class KitchenRequest(models.Model):
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    type = models.CharField(max_length=50, verbose_name='Планировка')
    size = models.CharField(max_length=50, verbose_name='Размер')
    style = models.CharField(max_length=50, verbose_name='Стиль')
    fasad = models.CharField(max_length=50, verbose_name='Материал фасада')
    stoleshnica = models.CharField(max_length=50, verbose_name='Материал столешницы')
    budget = models.CharField(max_length=50, verbose_name='Бюджет')
    name = models.CharField(max_length=50, verbose_name='Имя')
    phone = models.CharField(max_length=50, verbose_name='phone')

    def __str__(self) -> str:
        return self.name + self.phone
