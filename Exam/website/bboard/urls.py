from django.contrib import admin
from django.urls import path, include
from bboard.views import *
from users.views import *

urlpatterns = [
    path('', index),
    # path('students/', students, name="students"),
]
