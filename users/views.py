from django.views.generic import View
from django.shortcuts import HttpResponse, render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

class Register(View):
    def get(self, request, *args, **kwargs):
        register = UserCreationForm() 
        return render(request, 'register.html', {'register': register})

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            register = UserCreationForm(request.POST)
            if register.is_valid():
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

