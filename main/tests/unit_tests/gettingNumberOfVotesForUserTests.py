from django.test import TestCase
from users.tests.db_setup.db_setup import UserLoginInfo
from main.tests.db_setup.gettingQuestionsAndVotes import GettingQuestionsAndVotes
from main.views import *
from unittest.mock import patch, Mock

class GettingNumberOfVotesForUserTests(TestCase):
    def setUp(self):
        self.user = UserLoginInfo('lozza2000','lozza2000@gmail.com')
        self.user.setupLogin() 
        self.question1 = GettingQuestionsAndVotes(question = 'lorem 00')
        self.question1.questions()

    def test_00_sample(self):
        test = self.question1.get_questions()
        print(test)
        self.assertTrue(True)

