from django.db import models

class User(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Имя пользователя')

class Password(models.Model):
    password = models.CharField(max_length=20, db_index=True, verbose_name='Пароль')
