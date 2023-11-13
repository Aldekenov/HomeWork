# Generated by Django 4.2.7 on 2023-11-12 14:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Restaurant",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=250, verbose_name="Name")),
                ("description", models.TextField(verbose_name="Description")),
                ("address", models.CharField(max_length=250, verbose_name="Address")),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="Is active"),
                ),
                ("rating", models.FloatField(verbose_name="Rating")),
                ("logo", models.ImageField(upload_to="")),
            ],
        ),
        migrations.CreateModel(
            name="Review",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("text", models.TextField(verbose_name="Text")),
                (
                    "restaurant",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="restaurants.restaurant",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]