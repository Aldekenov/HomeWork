# Generated by Django 4.2.6 on 2023-10-29 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0002_post_published'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=20, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Пост',
                'ordering': ['name'],
            },
        ),
    ]