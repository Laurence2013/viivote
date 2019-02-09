from main.models import *

class GettingQuestionsAndVotes:
    def __init__(self, **kwargs):
        self.__qs = kwargs.get('question')

    def questions(self):
        Ask_A_Question_table.objects.create(question = self.__qs).save()

    def get_questions(self):
        qs = Ask_A_Question_table.objects.values('id', 'question', 'date_updated')
        return qs

    def questions_votes_table(self):
        pass
    
    def votes_table(self):
        pass

    def vote_a_table(self):
        pass

    def vote_b_table(self):
        pass

    def vote_c_table(self):
        pass
