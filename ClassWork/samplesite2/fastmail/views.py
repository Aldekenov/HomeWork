from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import User, Password

def index(request):
    template = loader.get_template('fastmail/index.html')
    log = User.objects.order_by('name')
    pas = Password.objects.order_by('password')
    context = {'log': log, 'pas': pas}
    return HttpResponse(template.render(context, request))
