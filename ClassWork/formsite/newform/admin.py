from django.contrib import admin
from .models import Info, Lesson

class InfoAdmin(admin.ModelAdmin):
    list_display = ('lesson', 'name', 'surname', 'birthday', 'number', 'comment')
    list_display_links = ('lesson', 'name', 'surname', 'number')
    search_fields = ('lesson', 'name', 'birthday', 'number')

class LessonAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)

admin.site.register(Info, InfoAdmin)
admin.site.register(Lesson, LessonAdmin)
