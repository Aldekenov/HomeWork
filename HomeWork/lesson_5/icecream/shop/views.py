from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Ice, Page

def index(request):
    template = loader.get_template('index.html')
    ice = Ice.objects.order_by('-published')
    context = {'ice': ice}
    return HttpResponse(template.render(context, request))
# Create your views here.

def step1(request):
    stepfields = Step.objects.get()
    navigators = Navigation_bar.objects.all()
    context = {
        "stepfieldst" : stepfields,
        "navigators" : navigators,
    }
    return render_to_response('templates/index.html', context)

def by_page(request, page_id):
    ice = Ice.objects.filter(page=page_id)
    pg = Page.objects.all()
    current_page = Page.objects.get(pk=page_id)
    context = {'ice':ice, 'pg':pg, 'current_page':current_page}
    return render(request, 'bboard/by_page.html', context)