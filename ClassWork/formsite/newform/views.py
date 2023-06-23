from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Info, Lesson
from django.views.generic.edit import CreateView
from .forms import InfoForm
from django.urls import reverse_lazy

def index(request):
    template = loader.get_template('newform/index.html')
    cont = Info.objects.order_by('lesson')
    context = {'cont': cont}
    return HttpResponse(template.render(context, request))

class InfoCreateView(CreateView):
    template_name = 'newform/form.html'
    form_class = InfoForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lesson'] = Lesson.objects.all()
        return context