from django.db import models
from django.core import validators

class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['name']

class Bb(models.Model):
    KINDS = (('b', "Куплю"),
             ('s', "Продам"),
             ('c', "Обменяю"))
    kind = models.CharField(max_length=1, choices=KINDS, default='s', verbose_name="Вид")
    img = models.ImageField(upload_to='product', null=True, blank=True, verbose_name='Изображение')
    rubric = models.ForeignKey(Rubric, null=True, on_delete=models.PROTECT, verbose_name='Рубрика')
    titlr = models.CharField(max_length=50, verbose_name='Товар', validators=[validators.MinLengthValidator(10, message='Минимум 10 символов')])
    content = models.TextField(null=True, blank=True, verbose_name='Описание', validators=[validators.MinLengthValidator(20, message='Минимум 20 символов')])
    price = models.FloatField(null=True, blank=True, verbose_name='Цена')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')

    class Meta:
        verbose_name_plural = 'Объявление'
        verbose_name = 'Объявление'
        ordering = ['-published']

    def title_and_price(self):
        return f'{self.titlr} ({self.price})'
# Create your models here.
