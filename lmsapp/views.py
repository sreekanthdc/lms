from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from . models import *

# Create your views here.

def myIndex(request):
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, request))


def checkLogin(request):
    try:
        v_username = request.POST.get('userName')
        v_password = request.POST.get('password')
        context = {}
        LoginObj = UserData.objects.filter(userName=v_username).exists()
       
        if(LoginObj):
            LoginObj1 = UserData.objects.get(userName=v_username)

            if(LoginObj1.password == v_password):
                if LoginObj1.role == 'admin':
                    template = loader.get_template('admin.html')
                if LoginObj1.role == 'candidate':
                    template = loader.get_template('candidate.html')
                template = loader.get_template('home.html')

            else:
                return HttpResponse("Password didnt match")

        else:
            return HttpResponse("User name didnt match")

    except Exception as e:
        print(e)
    return HttpResponse(template.render(context, request))
