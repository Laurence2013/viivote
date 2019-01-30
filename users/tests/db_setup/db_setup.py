from django.contrib.auth.models import User
from django.test.client import Client
from main.models import *

class UserLoginInfo:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def setupLogin(self):
        my_pass = 'mysha25pass'
        lozza_admin = User.objects.create_superuser(self.username, self.email, my_pass)
        client = Client()
        client.login(username = lozza_admin.username, password = my_pass)

class UserRegistrationInfo:
    def __init__(self, username, email, password1):
        self.username = username
        self.email = email
        self.password1 = password1

    def setupRegistration(self):
        lozza_admin = User.objects.create_superuser(self.username, self.email, self.password1)

