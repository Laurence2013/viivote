from django.views.generic import View
from django.shortcuts import HttpResponse, render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

class Register(View):
    def get(self, request, *args, **kwargs):
        register = UserRegisterForm() 
        return render(request, 'register.html', {'register': register})

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            register = UserRegisterForm(request.POST)
            if register.is_valid():
                register.save()
                username = register.cleaned_data.get('username')
                messages.success(request, f'Account created for {username}!')
                return redirect('main')
        else:
            register = UserCreationForm()
        messages.warning(request, f'Error, check your username or password')
        return render(request, 'register.html', {'register': register})

class Login(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'login.html', {})

class Logout(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'logout.html', {})

