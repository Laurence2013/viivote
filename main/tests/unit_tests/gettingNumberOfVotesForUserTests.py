from django.test import TestCase
from users.tests.db_setup.db_setup import UserLoginInfo
from main.tests.db_setup.gettingQuestionsAndVotes import GettingQuestionsAndVotes
from main.views import *
from unittest.mock import patch, Mock

class GettingNumberOfVotesForUserTests(TestCase):
    def setUp(self):
        self.user = UserLoginInfo('lozza2000','lozza2000@gmail.com')
        self.user.setupLogin() 
        self.question1 = GettingQuestionsAndVotes(question = 'lorem 00', vote_a = 'lorem 00 vote a', vote_b = 'lorem 00 vote b', vote_c = 'lorem 00 vote c')
        self.question1.questions()
        self.question1.vote_a_table()
        self.question1.vote_b_table()
        self.question1.vote_c_table()

    def test_00_a_question_is_the_same(self):
        qs = self.question1.get_questions()
        self.assertEqual('lorem 00', qs.get('question'))

    def test_01_vote_a_is_the_same(self):
        a = self.question1.get_vote_a()
        self.assertEqual('lorem 00 vote a', a.get('vote'))
    
    def test_02_vote_b_is_the_same(self):
        b = self.question1.get_vote_b()
        self.assertEqual('lorem 00 vote b', b.get('vote'))
    
    def test_03_vote_c_is_the_same(self):
        c = self.question1.get_vote_c()
        self.assertEqual('lorem 00 vote c', c.get('vote'))

