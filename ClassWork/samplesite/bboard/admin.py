from django.contrib import admin
from .models import Bb, Rubric

class BbAdmin(admin.ModelAdmin):
    list_display = ('kind', 'rubric', 'titlr', 'content', 'price', 'published')
    list_display_links = ('kind', 'rubric', 'titlr', 'content')
    search_fields = ('kind', 'rubric', 'titlr', 'content')

class RubricAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)

admin.site.register(Rubric, RubricAdmin)
admin.site.register(Bb, BbAdmin)
# Register your models here.
