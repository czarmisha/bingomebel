# Generated by Django 4.2 on 2023-04-19 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KitchenRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50, verbose_name='Планировка')),
                ('size', models.CharField(max_length=50, verbose_name='Размер')),
                ('style', models.CharField(max_length=50, verbose_name='Стиль')),
                ('fasad', models.CharField(max_length=50, verbose_name='Материал фасада')),
                ('stoleshnica', models.CharField(max_length=50, verbose_name='Материал столешницы')),
                ('budget', models.CharField(max_length=50, verbose_name='Бюджет')),
                ('furnitura', models.CharField(max_length=50, verbose_name='Фурнитура')),
                ('height', models.CharField(max_length=50, verbose_name='Высота')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('phone', models.CharField(max_length=50, verbose_name='Телефон')),
                ('comment', models.CharField(blank=True, max_length=255, verbose_name='Комментарий')),
            ],
        ),
    ]
