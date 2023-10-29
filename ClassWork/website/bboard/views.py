from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from bboard.models import *
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

def index(request):
    template = loader.get_template('main/index.html')
    pub = Post.objects.order_by('published')
    context = {'pub':pub}
    return HttpResponse(template.render(context, request))

def students(request):
    template = loader.get_template('main/students.html')
    context = {}
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main/index.html')
    usr = Post.objects.order_by('user')
    context = {'usr': usr}
    return HttpResponse(template.render(context, request))

def posts(request, post_id):
    template = loader.get_template('main/posts.html')
    post = get_object_or_404(Post, id=post_id)
    comments = Comment.objects.filter(post_id=post_id).order_by('-id')
    context = {'post':post, 'comments':comments}
    return HttpResponse(template.render(context, request))