from django.forms import ModelForm
from .models import Bb

class BbForm(ModelForm):
    class Meta:
        model = Bb
        fields = ('titlr', 'content', 'price', 'img', 'rubric')