from django.contrib import admin
from .models import Ice

class IceAdmin(admin.ModelAdmin):
    list_display = ('kind', 'title', 'content', 'price', 'published')
    list_display_links = ('kind', 'title', 'content')
    search_fields = ('kind', 'title', 'content')

admin.site.register(Ice, IceAdmin)
# Register your models here.
