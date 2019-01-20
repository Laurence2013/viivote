from main.models import *

class View_All_My_Questionss:
    def __init__(self, user_id):
        self.__user_id = user_id

    def get_questions(self):
        questions = []
        get_ids = User_Questions_table.objects.filter(user_id_id = self.__user_id).values('question_id_id') 
        get_ask_id = Ask_A_Question_table.objects.all().values('id','question','date_updated').order_by('-date_updated') 
        for ask_id in range(0,len(get_ask_id)):
            for get_id in range(0,len(get_ids)):
                if get_ids[get_id].get('question_id_id') == get_ask_id[ask_id].get('id'):
                    get_qs_ids = Ask_A_Question_table.objects.filter(id = get_ids[get_id].get('question_id_id')).values('id','question','date_updated').latest('date_updated')
                    get_vote_ids = Questions_Votes_table.objects.filter(question_id_id = get_qs_ids.get('id')).values('votes_id_id')[0]
                    votes_abc = Votes_table.objects.filter(id = get_vote_ids.get('votes_id_id')).values('vote_a_id','vote_b_id','vote_c_id')[0]
                    vote_a = Vote_A_table.objects.filter(id = votes_abc.get('vote_a_id')).values('id','vote','total_votes','date_updated')[0]
                    vote_b = Vote_B_table.objects.filter(id = votes_abc.get('vote_b_id')).values('id','vote','total_votes','date_updated')[0]
                    vote_c = Vote_C_table.objects.filter(id = votes_abc.get('vote_c_id')).values('id','vote','total_votes','date_updated')[0]
                    context = {
                        'question': get_qs_ids,
                        'vote_a': vote_a,
                        'vote_b': vote_b,
                        'vote_c': vote_c,
                    }
                    questions.append(context)
        return questions
