# Generated by Django 4.2 on 2023-04-21 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kitchenrequest',
            name='budget',
        ),
    ]
