from main.models import *

class Has_Voted_Per_Question(object):
    def __init__(self, vote_type, vote_id):
        self.__vote_type = vote_type
        self.__vote_id = vote_id

    def get_qs_id(self, user_id):
        if self.__vote_type == 'a':
            get_id = Votes_table.objects.filter(vote_a_id = self.__vote_id).values_list('id')[0][0]
            get_qv_id = Questions_Votes_table.objects.filter(votes_id_id = get_id).values_list('question_id_id')[0][0]
            question_id = Ask_A_Question_table.objects.filter(id = get_qv_id).values_list('id')[0][0]
            Has_Voted_Per_Question_table.objects.create(user_id_id = user_id, question_id_id = question_id).save()

