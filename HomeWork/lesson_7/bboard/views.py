from django.shortcuts import render
from django.http import HttpResponse
from .models import Bb, Rubric
from django.template import loader
from .forms import BbForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

class BbCreateView(CreateView):
    template_name = 'bboard/create.html'
    form_class = BbForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rub'] = Rubric.objects.all()
        return context

def index(request):
    template = loader.get_template('bboard/index.html')
    bbs = Bb.objects.order_by('-published')
    rub = Rubric.objects.order_by('name')
    context = {'bbs': bbs, 'rub': rub}
    return HttpResponse(template.render(context, request))

def one(request):
    return HttpResponse('<a href="../"><h1>EZ!</h1></a> <style>h1 {color:red;'
                        'font-family: "Impact"; font-size:101px; border:5px solid black;'
                        'text-align: center; text-shadow:black 5px 5px 2px; transition: .5s all} h1:hover{color:blue;'
                        'cursor:pointer; text-shadow:black 10px 10px 2px; transition: .5s all}a{text-decoration:none}</style>')

def step1(request):
    stepfields = Step.objects.get()
    navigators = Navigation_bar.objects.all()
    context = {
        "stepfieldst" : stepfields,
        "navigators" : navigators,
    }
    return render_to_response('templates/bboard/index.html', context)

def by_rubric(request, rubric_id):
    bbs = Bb.objects.filter(rubric=rubric_id)
    rub = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'bbs':bbs, 'rub':rub, 'current_rubric':current_rubric}
    return render(request, 'bboard/by_rubric.html', context)