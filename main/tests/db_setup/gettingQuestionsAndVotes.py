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

    def questions_votes_table(self, **kwargs):
        Questions_Votes_table.objects.create(question_id_id = kwargs.get('qs'), votes_id_id = kwargs.get('votes_table')).save()

    def get_questions_votes_table(self):
        qs_votes = Questions_Votes_table.objects.values('id', 'question_id_id', 'votes_id_id', 'date_updated')[0]
        return qs_votes
    
    def votes_table(self):
        a = Vote_A_table.objects.values('id', 'vote', 'total_votes', 'date_updated')[0]
        b = Vote_B_table.objects.values('id', 'vote', 'total_votes', 'date_updated')[0]
        c = Vote_C_table.objects.values('id', 'vote', 'total_votes', 'date_updated')[0]
        Votes_table.objects.create(vote_a_id = a.get('id'), vote_b_id = b.get('id'), vote_c_id = c.get('id')).save()

    def get_votes_table(self):
        votes_tbl = Votes_table.objects.values('id', 'vote_a_id', 'vote_b_id', 'vote_c_id', 'date_updated')[0]
        return votes_tbl

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
