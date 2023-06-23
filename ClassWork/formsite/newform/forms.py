from django.forms import ModelForm
from .models import Info

class InfoForm(ModelForm):
    class Meta:
        model = Info
        fields = ('lesson', 'name', 'surname', 'birthday', 'number', 'comment')