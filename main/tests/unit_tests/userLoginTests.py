from django.urls import reverse
from django.test import TestCase
from main.views import *

class UserLoginTests(TestCase):
    def test_00_get_login_page(self):
        login = reverse('login')
        self.assertEqual('/main/login/',login)

if __name__ == '__main__':
    unittest.main()
