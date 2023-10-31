from django.forms import ModelForm
from bboard.models import Comment, Post
from django.contrib.auth.models import User

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('img', 'title', 'text')