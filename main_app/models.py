from django.db import models


class KitchenRequest(models.Model):
    type = models.CharField(max_length=50, verbose_name='Планировка')
    size = models.CharField(max_length=50, verbose_name='Размер')
    style = models.CharField(max_length=50, verbose_name='Стиль')
    fasad = models.CharField(max_length=50, verbose_name='Материал фасада')
    stoleshnica = models.CharField(max_length=50, verbose_name='Материал столешницы')
    # budget = models.CharField(max_length=50, verbose_name='Бюджет')
    furnitura = models.CharField(max_length=50, verbose_name='Фурнитура')
    height = models.CharField(max_length=50, verbose_name='Высота')
    name = models.CharField(max_length=50, verbose_name='Имя')
    phone = models.CharField(max_length=50, verbose_name='Телефон')
    comment = models.CharField(max_length=255, verbose_name='Комментарий', blank=True)

    def __str__(self) -> str:
        return f'{self.name} {self.phone}'
