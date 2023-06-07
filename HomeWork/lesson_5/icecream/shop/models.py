from django.db import models

class Page(models.Model):
    number = models.CharField(max_length=20, db_index=True, verbose_name='Номер')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Страница'
        verbose_name = 'Страница'
        ordering = ['number']

class Ice(models.Model):
    page = models.ForeignKey(Page, null=True, on_delete=models.PROTECT, verbose_name='Номер')
    KINDS = (('b', "Рожок"),
             ('s', "Стаканчик"),
             ('c', "Шарик"))
    kind = models.CharField(max_length=1, choices=KINDS, default='s', verbose_name="Вид")
    img = models.ImageField(upload_to='product', null=True, blank=True, verbose_name='Изображение')
    title = models.CharField(max_length=50, verbose_name='Название')
    content = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.FloatField(null=True, blank=True, verbose_name='Цена')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')

    class Meta:
        verbose_name_plural = 'Магазин'
        verbose_name = 'Магазин'
        ordering = ['-published']
# Create your models here.
