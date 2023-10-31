from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from bboard.models import *
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from bboard.forms import CommentForm, PostForm
from django.urls import reverse_lazy
from django.shortcuts import redirect


def index(request):
    template = loader.get_template('main/index.html')
    pub = Post.objects.order_by('published')
    context = {'pub':pub}
    return HttpResponse(template.render(context, request))

def students(request):
    template = loader.get_template('main/students.html')
    context = {}
    return HttpResponse(template.render(context, request))

def create(request):
    template = loader.get_template('main/create.html')
    context = {}
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main/index.html')
    usr = Post.objects.order_by('user')
    context = {'usr': usr}
    return HttpResponse(template.render(context, request))

def posts_detail(request, post_id):
    template = loader.get_template('main/posts.html')
    post = get_object_or_404(Post, id=post_id)
    comments = Comment.objects.filter(post_id=post_id).order_by('-id')
    form = CommentForm()
    form_post = PostForm()
    context = {'post':post, 'comments':comments, 'form': form, 'form_post':form_post}
    return HttpResponse(template.render(context, request))


def posts(request):
    if request.method == 'POST':
        user_id = request.user.id
        title = request.POST.get('title')
        text = request.POST.get('text')
        post = Post(user_id=user_id, title=title, text=text)
        post.save()
        return redirect('index')


def comments(request):
    if request.method == 'POST':
        user_id = request.user.id
        post_id = request.POST.get('post_id')
        text = request.POST.get('text')
        comment = Comment(user_id=user_id, post_id=post_id, text=text)
        comment.save()
        return redirect('posts_detail', post_id=post_id)
