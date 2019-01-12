from main.models import *

class Has_Voted_Per_Question(object):
    def __init__(self, vote_type, vote_id):
        self.__vote_type = vote_type
        self.__vote_id = vote_id

    def get_qs_id(self, user_id):
        # Use the vote id to trace back to where it was questioned from, so you can use that ...
        # to get the vote id question and save into Has Voted Per Question
        if self.__vote_type == 'a':
            get_id = Votes_table.objects.filter(vote_a_id = self.__vote_id).values_list('id')[0][0]
            get_qv_id = Questions_Votes_table.objects.filter(votes_id_id = get_id).values_list('question_id_id')[0][0]
            question_id = Ask_A_Question_table.objects.filter(id = get_qv_id).values_list('id')[0][0]
            Has_Voted_Per_Question_table.objects.create(user_id_id = user_id, question_id_id = question_id, vote_type = self.__vote_type, vote_a_id = self.__vote_id).save() 
        if self.__vote_type == 'b':
            get_id = Votes_table.objects.filter(vote_b_id = self.__vote_id).values_list('id')[0][0]
            get_qv_id = Questions_Votes_table.objects.filter(votes_id_id = get_id).values_list('question_id_id')[0][0]
            question_id = Ask_A_Question_table.objects.filter(id = get_qv_id).values_list('id')[0][0]
            Has_Voted_Per_Question_table.objects.create(user_id_id = user_id, question_id_id = question_id, vote_type = self.__vote_type, vote_b_id = self.__vote_id).save() 
        if self.__vote_type == 'c':
            get_id = Votes_table.objects.filter(vote_c_id = self.__vote_id).values_list('id')[0][0]
            get_qv_id = Questions_Votes_table.objects.filter(votes_id_id = get_id).values_list('question_id_id')[0][0]
            question_id = Ask_A_Question_table.objects.filter(id = get_qv_id).values_list('id')[0][0]
            Has_Voted_Per_Question_table.objects.create(user_id_id = user_id, question_id_id = question_id, vote_type = self.__vote_type, vote_c_id = self.__vote_id).save() 
