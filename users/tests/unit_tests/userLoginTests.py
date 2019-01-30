from users.tests.db_setup.db_setup import UserLoginInfo
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User
from django.urls import reverse
from django.test import RequestFactory, TestCase
from main.views import *

class UserLoginTests(TestCase, UserLoginInfo):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = UserLoginInfo('lozza2000','lozza2000@gmail.com')
        self.user.setupLogin() 

    def test_00_get_login_page(self):
        login = reverse('login')
        self.assertEqual('/main/login/',login)

    def test_01_user_can_login_and_when_logged_in_status_code_is_200(self):
        request = self.factory.get('main/login')
        request.user = self.user
        response = auth_views.LoginView.as_view(template_name='login.html')(request)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
