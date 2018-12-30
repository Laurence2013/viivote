from django.views.generic import View
from django.shortcuts import HttpResponse, render
from django.contrib.auth.forms import UserCreationForm

class Register(View):
    def get(self, request, *args, **kwargs):
        register = UserCreationForm() 
        return render(request, 'register.html', {'register': register})

class Login(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello from Login')

class Logout(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello from Logout')

