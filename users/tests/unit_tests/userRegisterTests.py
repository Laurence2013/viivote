from django.urls import reverse
from django_downloadview import setup_view
from django.test import RequestFactory, TestCase
from unittest.mock import patch, MagicMock
from users.views import *

class UserRegisterTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.data = {'username': 'lozza2000', 'email': 'lozza2000@gmail.com', 'password1': 'lozza2000pass',}

    def test_00_get_login_page(self):
        login = reverse('register')
        self.assertEqual('/main/register/',login)

    def test_01_sample(self):
        register = reverse('register')
        request = self.factory.post(register, self.data)
        test = setup_view(Register(), request)
        #print(test.request.POST)

    def test_02_sample(self):
        mock_msg = patch('users.views.Register.post').start()
        print(mock_msg)

        request = self.factory.post(reverse('register'))
        response = Register.as_view()(request)
        print(response)

if __name__ == '__main__':
    unittest.main()
