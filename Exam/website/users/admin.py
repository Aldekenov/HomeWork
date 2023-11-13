from django.contrib import admin
from bboard.models import *
from users.models import *
from django.conf.urls import include

class PostAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Comment, CommentAdmin)

class ProfileAdmin(admin.ModelAdmin):
    pass

admin.site.register(Profile, ProfileAdmin)