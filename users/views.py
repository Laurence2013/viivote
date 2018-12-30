from django.views.generic import View
from django.shortcuts import HttpResponse, render

class Register(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello from Register')

class Login(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello from Login')

class Logout(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello from Logout')

