from users.tests.db_setup.db_setup import UserRegistrationInfo
from core.utilities.general_utils import General_Utils
from django.test import TestCase
from unittest.mock import patch, Mock

class GeneralUtilitiesTests(TestCase):
    def setUp(self):
        self.gen_utilities = General_Utils()
        self.register = UserRegistrationInfo(username = 'lozza2001', email = 'lozza2001@gmail.com', password = 'lozza2001pass')
        self.register.setupRegisterNormalUsers()

    def test_00_sample(self):
        user = self.register.getUserInfo()
        user_id = tuple(i.get('id') for i in user)
        test = self.gen_utilities.get_questions(user_id)
        print(test)




