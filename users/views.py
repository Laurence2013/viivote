from django.views.generic import View
from django.shortcuts import HttpResponse, render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

class Register(View):
    def get(self, request, *args, **kwargs):
        form = UserRegisterForm() 
        return render(request, 'register.html', {'form': form})

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f'Account created for {username}! You are now able to log in')
                return redirect('login')
        else:
            form = UserCreationForm()
        messages.warning(request, f'Error, check your username or password')
        return render(request, 'register.html', {'form': form})

