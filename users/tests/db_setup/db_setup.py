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
    def __init__(self, **kwargs):
        self.username = kwargs.get('username')
        self.email = kwargs.get('email')
        self.password1 = kwargs.get('password')

    def setupRegistration(self):
        lozza_admin = User.objects.create_superuser(self.username, self.email, self.password1)

    def setupRegisterNormalUsers(self):
        lozza_admin = User.objects.create_user(username = self.username, email = self.email, password = self.password1)

    def getUserInfo(self):
        return User.objects.values('id', 'username', 'email')
