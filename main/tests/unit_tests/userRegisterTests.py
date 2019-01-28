from django.urls import reverse
from django.test import TestCase
from main.views import *

class UserRegisterTests(TestCase):
    def test_00_get_login_page(self):
        login = reverse('register')
        self.assertEqual('/main/register/',login)

if __name__ == '__main__':
    unittest.main()
