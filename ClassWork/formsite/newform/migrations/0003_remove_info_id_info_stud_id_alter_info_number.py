# Generated by Django 4.2 on 2023-07-19 15:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newform', '0002_alter_info_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='info',
            name='id',
        ),
        migrations.AddField(
            model_name='info',
            name='stud_id',
            field=models.AutoField(default='1', primary_key=True, serialize=False, verbose_name='ID студента'),
        ),
        migrations.AlterField(
            model_name='info',
            name='number',
            field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(10000000000, message='номер введен не корректно'), django.core.validators.MaxValueValidator(100000000000, message='номер введен не корректно')], verbose_name='Номер телефона'),
        ),
    ]
