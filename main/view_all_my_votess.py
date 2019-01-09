from main.models import *

class View_All_My_Votess:
    def __init__(self, vote_type):
        self.__vote_types = vote_type

    def get_from_votes_type(self, vote_type):
        votes_table_id = []
        if vote_type == 'a':
            for vote_type in self.__vote_types:
                votes_table_ids = (Votes_table.objects.filter(vote_a_id = vote_type[0]).values_list('id','vote_a_id'))[0]
                context_a = {
                    'id': votes_table_ids[0],
                    'vote_a': votes_table_ids[1]
                }
                votes_table_id.append(context_a)
        if vote_type == 'b':
            for vote_type in self.__vote_types:
                votes_table_id.append(Votes_table.objects.filter(vote_b_id = vote_type[0]).values_list('id','vote_b_id')[0][0])
                context_b = {
                    'id': votes_table_ids[0],
                    'vote_b': votes_table_ids[1]
                }
        if vote_type == 'c':
            for vote_type in self.__vote_types:
                votes_table_id.append(Votes_table.objects.filter(vote_c_id = vote_type[0]).values_list('id','vote_c_id')[0][0])
                context_c = {
                    'id': votes_table_ids[0],
                    'vote_c': votes_table_ids[1]
                }
        return votes_table_id

    def get_from_questions_votes(self, questions_votes):
        for qs_vs in questions_votes:
            qs_id = Questions_Votes_table.objects.filter(votes_id_id = qs_vs.get('id')).values_list('question_id_id')[0][0]            
            qs_vs.update({'question_id': qs_id})
        return questions_votes

    def get_qs_with_its_vote(self, qs_votes, vote_type):
        for qs_vote in qs_votes:
            question = Ask_A_Question_table.objects.filter(id = qs_vote.get('question_id')).values_list('question')[0][0]
            qs_vote.update({'question': question})
            if vote_type == 'a':
                vote = Vote_A_table.objects.filter(id = qs_vote.get('vote_a')).values_list('vote')[0][0]
                qs_vote.update({'vote': vote})
            if vote_type == 'b':
                vote = Vote_B_table.objects.filter(id = qs_vote.get('vote_b')).values_list('vote')[0][0]
                qs_vote.update({'vote': vote})
            if vote_type == 'c':
                vote = Vote_C_table.objects.filter(id = qs_vote.get('vote_c')).values_list('vote')[0][0]
                qs_vote.update({'vote': vote})
        return qs_votes
