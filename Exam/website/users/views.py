from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.template import loader
from .models import *
from users.models import Profile
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from bboard.templatetags.custom_tags import censor
from django.shortcuts import redirect

def login_view(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)


        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return HttpResponse('Login error')
    else:
        return render(request, 'users/login.html', {})

def auth_view(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
            if user is not None:
                return HttpResponse('Такой пользователь существует!')
        except User.DoesNotExist:
            User.objects.create_user(username, password=password)
            return render(request, 'users/login.html', {})


    else:
        return render(request, 'users/auth.html', {})

def logout_view(request):
    logout(request)
    return redirect('index')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'



class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = '__all__'

class NotBannedProfilesList(APIView):
    def get(self, request, format=None):
        profiles = Profile.objects.filter(is_banned=False)
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)

def profile(request):
    template = loader.get_template('main/index.html')
    pro = Profile.objects.get(pk=id)
    context = {'pro':pro}
    return HttpResponse(template.render(context, request))