from main.models import *

class GettingQuestionsAndVotes:
    def __init__(self, **kwargs):
        self.__qs       = kwargs.get('question')
        self.__vote_a   = kwargs.get('vote_a')
        self.__vote_b   = kwargs.get('vote_b')
        self.__vote_c   = kwargs.get('vote_c')

    def questions(self):
        Ask_A_Question_table.objects.create(question = self.__qs).save()

    def get_questions(self):
        qs = Ask_A_Question_table.objects.values('id', 'question', 'date_updated')[0]
        return qs

    def questions_votes_table(self):
        pass
    
    def votes_table(self):
        pass

    def vote_a_table(self):
        Vote_A_table.objects.create(vote = self.__vote_a, total_votes = 0).save()

    def get_vote_a(self):
        a = Vote_A_table.objects.values('id', 'vote', 'total_votes', 'date_updated')[0]
        return a
    
    def vote_b_table(self):
        Vote_B_table.objects.create(vote = self.__vote_b, total_votes = 0).save()
    
    def get_vote_b(self):
        b = Vote_B_table.objects.values('id', 'vote', 'total_votes', 'date_updated')[0]
        return b

    def vote_c_table(self):
        Vote_C_table.objects.create(vote = self.__vote_c, total_votes = 0).save()
    
    def get_vote_c(self):
        c = Vote_C_table.objects.values('id', 'vote', 'total_votes', 'date_updated')[0]
        return c
