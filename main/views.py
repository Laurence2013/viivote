import os
from django.db.models import F
from django.conf import settings
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.views.generic import View
from django.shortcuts import HttpResponse, render, redirect
from main.forms import Ask_A_Question
from main.models import *
from main.save_data_to_json import Save_Data_To_Json
from main.view_all_my_votess import View_All_My_Votess
from main.has_voted_per_question import Has_Voted_Per_Question
from django.contrib import messages

class All_Votes(View):
    __get_json = Save_Data_To_Json()
    __all_votes_json = 'all_votes'

    def get(self, request, *args, **kwargs):
        get_json = self.__get_json.get_json_file(self.__all_votes_json)
        return JsonResponse(get_json, safe = False)

class Get_All_My_Votes(View):
    __get_json = Save_Data_To_Json()
    __all_user_votes_json = 'all_user_votes'

    def get(self, request, *args, **kwargs):
        get_json = self.__get_json.get_json_file(self.__all_user_votes_json)
        return JsonResponse(get_json, safe = False)

class View_All_My_Votes(View):
    __get_json = Save_Data_To_Json()
    __base_dir = settings.BASE_DIR
    __all_user_votes_json = 'all_user_votes'

    def get(self, request, *args, **kwargs):
        check_json = self.__base_dir + '/static/json/'+ self.__all_user_votes_json +'.json'
        all_qs_vs = []

        user_id = request.user.id
        user_vote_a = User_Vote_A_table.objects.filter(user_id_id = user_id).values_list('vote_a_id_id')
        user_vote_b = User_Vote_B_table.objects.filter(user_id_id = user_id).values_list('vote_b_id_id')
        user_vote_c = User_Vote_C_table.objects.filter(user_id_id = user_id).values_list('vote_c_id_id')
        
        from_votes_table_a = View_All_My_Votess(user_vote_a)
        get_votes_a_table_ids = from_votes_table_a.get_from_votes_type('a')
        get_qs_with_its_vote_a = from_votes_table_a.get_from_questions_votes(get_votes_a_table_ids)
        qs_vs_a = from_votes_table_a.get_qs_with_its_vote(get_qs_with_its_vote_a,'a',Vote_A_table,'vote_a')

        from_votes_table_b = View_All_My_Votess(user_vote_b)
        get_votes_b_table_ids = from_votes_table_b.get_from_votes_type('b')
        get_qs_with_its_vote_b = from_votes_table_b.get_from_questions_votes(get_votes_b_table_ids)
        qs_vs_b = from_votes_table_b.get_qs_with_its_vote(get_qs_with_its_vote_b,'b',Vote_B_table,'vote_b')
        
        from_votes_table_c = View_All_My_Votess(user_vote_c)
        get_votes_c_table_ids = from_votes_table_c.get_from_votes_type('c')
        get_qs_with_its_vote_c = from_votes_table_c.get_from_questions_votes(get_votes_c_table_ids)
        qs_vs_c = from_votes_table_c.get_qs_with_its_vote(get_qs_with_its_vote_c,'c',Vote_C_table,'vote_c')

        all_qs_vs.append(qs_vs_a)
        all_qs_vs.append(qs_vs_b)
        all_qs_vs.append(qs_vs_c)
        
        if check_json != 0 or check_json == 0:
            self.__get_json.save_json(all_qs_vs, self.__all_user_votes_json)
        return render(request, 'view_all_votes.html', {})

class Main(View):
    __get_json = Save_Data_To_Json()
    __base_dir = settings.BASE_DIR
    __all_votes_json = 'all_votes'
    __has_voted_per_qs = 'has_voted_per_question'

    def get(self, request, *args, **kwargs):
        user_id = request.user.id
        if user_id:
            check_json = self.__base_dir + '/static/json/'+ self.__all_votes_json +'.json'
            get_q = self.__get_questions(user_id)
            if check_json != 0 or check_json == 0:
                self.__get_json.save_json(get_q, self.__all_votes_json)
            return render(request, 'index.html', {})
        return redirect('login')

    def post(self, request, *args, **kwargs):
        username = request.user
        user_id = request.user.id
        votes = request.POST
        for k_vote, v_vote in votes.items():
            if k_vote == 'csrfmiddlewaretoken':
                continue
            ask_question_id = int(k_vote)
            vote_split = v_vote.split('_')
            vote_type = vote_split[1]
            vote_id = int(vote_split[0])

        #if vote_type == 'a':
        #    User_Vote_A_table.objects.create(user_id_id = user_id, vote_a_id_id = vote_id).save()
        #    self.__save_user_votes(Vote_A_table, vote_id)
        #if vote_type == 'b':
        #    User_Vote_B_table.objects.create(user_id_id = user_id, vote_b_id_id = vote_id).save()
        #    self.__save_user_votes(Vote_B_table, vote_id)
        #if vote_type == 'c':
        #    User_Vote_C_table.objects.create(user_id_id = user_id, vote_c_id_id = vote_id).save()
        #    self.__save_user_votes(Vote_C_table, vote_id)

        has_voted = Has_Voted_Per_Question(vote_type, vote_id)
        has_voted.get_qs_id(user_id)

        messages.success(request, f'You have successfully voted {username}')
        return redirect('main')

    def __save_user_votes(self, vote, vote_id):
        vote = vote.objects.get(id = vote_id)
        vote.total_votes = F('total_votes') + 1
        vote.save()        
    
    def __get_questions(self, user_id):
        votes_list = []
        get_qs = Ask_A_Question_table.objects.values_list('id')
        qs = [get_qs[qs] for qs in range(0,len(get_qs))]
        for ques_vote_q in qs:
            vote_id = Questions_Votes_table.objects.filter(votes_id_id = ques_vote_q[0]).values_list('votes_id_id')
            try:
                votes_list.append(vote_id[0][0])
            except:
                pass
        return self.__get_votes(votes_list, user_id)

    def __get_votes(self, votes, user_id):
        context_list = [] 
        has_voted = Has_Voted_Per_Question_table.objects.filter(user_id_id = user_id).values_list('question_id_id') 
        for qv in votes:
            get_qs = Questions_Votes_table.objects.filter(votes_id_id = qv).values_list('question_id_id')[0][0]
            get_q = Ask_A_Question_table.objects.filter(id = get_qs).values_list('id','question')
            for v in range(0,len(get_q)):
                get_vote_ids = Votes_table.objects.filter(id = qv).values_list('vote_a_id','vote_b_id','vote_c_id')
                vote_a = Vote_A_table.objects.filter(id = get_vote_ids[0][0]).values_list('id','vote')[0]
                con_vote_a = {'id': str(vote_a[0]) + '_a', 'vote': vote_a[1], 'questions_vote_id': get_qs, 'user_id': user_id,}
                vote_b = Vote_B_table.objects.filter(id = get_vote_ids[0][1]).values_list('id','vote')[0]
                con_vote_b = {'id': str(vote_b[0]) + '_b', 'vote': vote_b[1], 'questions_vote_id': get_qs, 'user_id': user_id,}
                vote_c = Vote_C_table.objects.filter(id = get_vote_ids[0][2]).values_list('id','vote')[0]
                con_vote_c = {'id': str(vote_c[0]) + '_c', 'vote': vote_c[1], 'questions_vote_id': get_qs, 'user_id': user_id,}
                
                for voted in has_voted:
                    if voted[0] == get_q[0][0]:
                        context = {
                            'user_id': user_id,
                            'has_voted': True,
                            'question_id': get_q[0][0],
                            'question': get_q[0][1],
                            'vote_a': con_vote_a,
                            'vote_b': con_vote_b,
                            'vote_c': con_vote_c,
                        }        
                        break

                    if voted[0] != get_q[0][0]:
                        context = {
                            'user_id': user_id,
                            'has_voted': False,
                            'question_id': get_q[0][0],
                            'question': get_q[0][1],
                            'vote_a': con_vote_a,
                            'vote_b': con_vote_b,
                            'vote_c': con_vote_c,
                        }
            if not has_voted:
                context = {
                    'user_id': user_id,
                    'has_voted': False,
                    'question_id': get_q[0][0],
                    'question': get_q[0][1],
                    'vote_a': con_vote_a,
                    'vote_b': con_vote_b,
                    'vote_c': con_vote_c,
                }
            context_list.append(context)
        return context_list

class Ask_Question(View):
    def get(self, request, *args, **kwargs):
        question = Ask_A_Question()
        return render(request, 'ask_question.html', {'form':question})

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated == True:
            user_id = request.user.id
            if request.method == 'POST':
                question = request.POST.get('ask_question')
                vote_a = request.POST.get('vote_a')
                vote_b = request.POST.get('vote_b')
                vote_c = request.POST.get('vote_c')
                #self.__save_question(question, user_id)
                #self.__save_votes(vote_a, vote_b, vote_c, user_id)
                #self.__save_question_votes()
        return redirect('main')

    def __save_question(self, question, user_id):
        Ask_A_Question_table.objects.create(question = question)
        get_question_id = Ask_A_Question_table.objects.latest('date_updated')
        get_user_id = User.objects.get(id = user_id)

        User_Questions_table.objects.create(user_id = get_user_id, question_id = get_question_id,)

    def __save_votes(self, a,b,c, user_id):
        Vote_A_table.objects.create(vote = a)
        Vote_B_table.objects.create(vote = b)
        Vote_C_table.objects.create(vote = c)
           
        get_vote_a = Vote_A_table.objects.latest('date_updated')
        get_vote_b = Vote_B_table.objects.latest('date_updated')
        get_vote_c = Vote_C_table.objects.latest('date_updated')

        Votes_table.objects.create(vote_a = get_vote_a,vote_b = get_vote_b, vote_c = get_vote_c)

    def __save_question_votes(self):
        get_question = Ask_A_Question_table.objects.latest('date_updated')
        get_vote = Votes_table.objects.latest('date_updated')

        Questions_Votes_table.objects.create(question_id = get_question, votes_id = get_vote)
