from django.views.generic import View
from django.shortcuts import HttpResponse, render

class Main(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello from main')
