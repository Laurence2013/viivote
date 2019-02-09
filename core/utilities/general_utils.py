from main.models import *

class General_Utils:
    
    def get_questions(self, user_id):
        votes_list = []
        get_qs = Ask_A_Question_table.objects.values_list('id').order_by('-date_updated')
        qs = [get_qs[qs] for qs in range(0,len(get_qs))]
        print(qs)
        for ques_vote_q in qs:
            vote_id = Questions_Votes_table.objects.filter(votes_id_id = ques_vote_q[0]).values_list('votes_id_id')
            try:
                votes_list.append(vote_id[0][0])
            except IndexError as e:
                pass #print(e) save to log eventually
        return self.__get_votes(votes_list, user_id)
    
    def __get_votes(self, votes, user_id):
        context_list = []
        qs_answers = []
        has_voted = Has_Voted_Per_Question_table.objects.filter(user_id_id = user_id).values_list('question_id_id') 
        has_voted1 = Has_Voted_Per_Question_table.objects.filter(user_id_id = user_id).values_list('question_id_id','vote_type','vote_a_id','vote_b_id','vote_c_id')
        for qv in votes:
            get_qs = Questions_Votes_table.objects.filter(votes_id_id = qv).values_list('question_id_id')[0][0]
            get_qs_vote = User_Questions_Votes_Answers_table.objects.filter(question_id_id = get_qs).values('question_id_id','answer_id_id','user_id_id')
            try:
                for vote in range(0,len(get_qs_vote)):
                    get_anss = Answer_table.objects.filter(id = get_qs_vote[vote].get('answer_id_id')).values('id','answer','date_updated')[0]
                    qs_anss = get_qs_vote[0].get('question_id_id'), get_anss
                    qs_answers.append(qs_anss)
            except IndexError as e:
                pass #print(e) save to log eventually
            
            get_q = Ask_A_Question_table.objects.filter(id = get_qs).values_list('id','question','date_updated') 
            for v in range(0,len(get_q)):
                get_vote_ids = Votes_table.objects.filter(id = qv).values_list('vote_a_id','vote_b_id','vote_c_id')
                vote_a = Vote_A_table.objects.filter(id = get_vote_ids[0][0]).values_list('id','vote')[0]
                con_vote_a = {'id': str(vote_a[0]) + '_a', 'vote': vote_a[1], 'questions_vote_id': get_qs, 'user_id': user_id,}
                vote_b = Vote_B_table.objects.filter(id = get_vote_ids[0][1]).values_list('id','vote')[0]
                con_vote_b = {'id': str(vote_b[0]) + '_b', 'vote': vote_b[1], 'questions_vote_id': get_qs, 'user_id': user_id,}
                vote_c = Vote_C_table.objects.filter(id = get_vote_ids[0][2]).values_list('id','vote')[0]
                con_vote_c = {'id': str(vote_c[0]) + '_c', 'vote': vote_c[1], 'questions_vote_id': get_qs, 'user_id': user_id,}    

                for voted in has_voted1:
                    if voted[0] == get_q[0][0]:
                        context = self.__get_context(qs_answers, get_q, user_id, con_vote_a, con_vote_b, con_vote_c, True, voted[1], voted[2], voted[3], voted[4]) 
                        break
                    if voted[0] != get_q[0][0]:
                        context = self.__get_context(qs_answers, get_q, user_id, con_vote_a, con_vote_b, con_vote_c, False,None,None,None,None) 
            if not has_voted:
                context = self.__get_context(qs_answers, get_q, user_id, con_vote_a, con_vote_b, con_vote_c, False, None, None, None, None) 
            context_list.append(context)
        return context_list
