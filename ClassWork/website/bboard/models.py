from django.db import models
from django.shortcuts import render
from django.contrib.auth.models import User
from django.views import generic

class Post(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250, verbose_name='Загаловок')
    text = models.TextField(verbose_name='Текст')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')
class Comment(models.Model):
    id = models.BigAutoField(primary_key=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length='100', verbose_name='Комментарии')