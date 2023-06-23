from django.db import models
from django.core import validators

class Lesson(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Название')

    def __str__(self):
        return self.name

class Info(models.Model):
    lesson = models.ForeignKey(Lesson, null=True, on_delete=models.PROTECT, verbose_name='Курс')
    name = models.CharField(max_length=50, verbose_name='Имя', validators=[validators.MinLengthValidator(3, message='Минимум 3 символов')])
    surname = models.CharField(max_length=50, verbose_name='Фамилия', validators=[validators.MinLengthValidator(3, message='Минимум 3 символов')])
    birthday = models.DateField(auto_now_add=False, db_index=True, verbose_name='Дата рождения')
    number = models.FloatField(null=True, blank=True, verbose_name='Номер телефона')
    comment = models.TextField(null=True, blank=True, verbose_name='Комментарии')