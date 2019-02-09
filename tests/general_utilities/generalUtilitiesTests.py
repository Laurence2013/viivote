from users.tests.db_setup.db_setup import UserLoginInfo, UserRegistrationInfo
from core.utilities.general_utils import General_Utils
from django.test import TestCase
from unittest.mock import patch, Mock

class GeneralUtilitiesTests(TestCase):
    def setUp(self):
        self.user_id = 11
        self.gen_utilities = General_Utils()

    def test_00_sample(self):
        test = self.gen_utilities.get_questions(self.user_id)
        print(test)
