import pprint
import os
from django.db.models import F
from django.conf import settings
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.views.generic import View
from django.shortcuts import HttpResponse, render, redirect
from main.forms import Ask_A_Question, Answer_Vote_Form, Edit_Answer
from main.models import *
from main.save_data_to_json import Save_Data_To_Json
from main.view_all_my_votess import View_All_My_Votess
from main.has_voted_per_question import Has_Voted_Per_Question
from main.view_all_my_questionss import View_All_My_Questionss
from django.contrib import messages
from main.saveToJsonGetQuestions import SaveToJsonGetQuestions

class Bookmark(View):
    def get(self, request, *args, **kwargs): 
        user_id = request.user.id
        username = request.user
        question_id = kwargs.get('question_id')
        if Bookmark_table.objects.filter(user_id_id = user_id, question_id_id = question_id).exists():
            messages.warning(request, f'This already exist in your bookmark {username}')
            return redirect('main')
        Bookmark_table.objects.create(user_id_id = user_id, question_id_id = question_id).save()
        messages.success(request, f'You have just added to your bookmarks {username}')
        return redirect('main')

class Get_Bookmarks(View):
    __get_json = Save_Data_To_Json()
    __base_dir = settings.BASE_DIR
    __get_bookmarks_json = 'get_bookmarks'
    __pp = pprint.PrettyPrinter(indent = 3)

    def get(self, request, *args, **kwargs):
        bookmarks = []
        user_id = request.user.id
        user_username = request.user
        context_user = {'user_id': int(user_id), 'username': str(user_username),}
        bookmarks.append(context_user)
        check_json = self.__base_dir + '/static/json/'+ self.__get_bookmarks_json +'.json'
        get_question_id = Bookmark_table.objects.filter(user_id_id = user_id).values('question_id_id','date_updated').order_by('-date_updated')
        for get_qs in get_question_id:
            answers = []
            question = Ask_A_Question_table.objects.filter(id = get_qs.get('question_id_id')).values('id','question')[0]
            has_voted = Has_Voted_Per_Question_table.objects.filter(question_id_id = get_qs.get('question_id_id'), user_id_id = user_id).count()
            has_voted_type = Has_Voted_Per_Question_table.objects.filter(question_id_id = get_qs.get('question_id_id'), user_id_id = user_id).values('vote_type')
            #voted_for = User_Questions_Votes_Answers_table.objects.filter(question_id_id = get_qs.get('question_id_id'), user_id_id = user_id).values('vote_a_id','vote_b_id','vote_c_id')
            voted_for = Has_Voted_Per_Question_table.objects.filter(question_id_id = get_qs.get('question_id_id'), user_id_id = user_id).values('vote_a_id','vote_b_id','vote_c_id')
            if not voted_for:
                user_voted_for = None
            else:
                if voted_for[0].get('vote_a_id') != None:
                    user_voted_for = voted_for[0].get('vote_a_id')
                if voted_for[0].get('vote_b_id') != None:
                    user_voted_for = voted_for[0].get('vote_b_id')
                if voted_for[0].get('vote_c_id') != None:
                    user_voted_for = voted_for[0].get('vote_c_id')
            if has_voted == 0 and not has_voted_type:
                context_has_voted = {'has_voted': False, 'you_voted': False}
            else:
                context_has_voted = {'has_voted': True, 'you_voted': has_voted_type[0].get('vote_type'), 'you_voted_for': user_voted_for,}

            get_user_id = User_Questions_table.objects.filter(question_id_id = question.get('id')).values('user_id_id')[0]
            get_username = User.objects.filter(id = get_user_id.get('user_id_id')).values('username')[0]
            answers_ids = User_Questions_Votes_Answers_table.objects.filter(question_id_id = get_qs.get('question_id_id')).values('answer_id_id', 'user_id_id')
            if not answers_ids:
                context_ans = {'ans': None,}
            if answers_ids:
                for answers_id in answers_ids:
                    get_ans_user = User.objects.filter(id = answers_id.get('user_id_id')).values('id','username')[0]
                    get_ans = Answer_table.objects.filter(id = answers_id.get('answer_id_id')).values('id','answer','date_updated')[0]
                    get_ans_and_users = get_ans, get_ans_user
                    answers.append(get_ans_and_users)
                    context_ans = {'ans': answers,}
            qs_vote_id = Questions_Votes_table.objects.filter(question_id_id = question.get('id')).values('votes_id_id', 'question_id_id')
            votes_a_id = Votes_table.objects.filter(id = qs_vote_id[0].get('votes_id_id')).values('vote_a_id')[0]
            votes_b_id = Votes_table.objects.filter(id = qs_vote_id[0].get('votes_id_id')).values('vote_b_id')[0]
            votes_c_id = Votes_table.objects.filter(id = qs_vote_id[0].get('votes_id_id')).values('vote_c_id')[0]
            votes_a = Vote_A_table.objects.filter(id = votes_a_id.get('vote_a_id')).values('id','vote','date_updated')[0]
            context_vote_a = {'type': 'type_a', 'vote_a': votes_a, 'qs_id_type': str(question.get('id')) + '_a',}
            votes_b = Vote_B_table.objects.filter(id = votes_b_id.get('vote_b_id')).values('id','vote','date_updated')[0]
            context_vote_b = {'type': 'type_b', 'vote_b': votes_b, 'qs_id_type': str(question.get('id')) + '_b',}
            votes_c = Vote_C_table.objects.filter(id = votes_c_id.get('vote_c_id')).values('id','vote','date_updated')[0]
            context_vote_c = {'type': 'type_c', 'vote_c': votes_c, 'qs_id_type': str(question.get('id')) + '_c',}
            context = {
                'question_id': question.get('id'),
                'question': question.get('question'),
                'username': get_username.get('username'),
                'answers': context_ans,
                'date_updated': get_qs.get('date_updated'),
                'vote_a': context_vote_a,
                'vote_b': context_vote_b,
                'vote_c': context_vote_c,
                'has_voted': context_has_voted,
            }
            bookmarks.append(context)  
        if check_json != 0 or check_json == 0:
            self.__get_json.save_json(bookmarks, self.__get_bookmarks_json)
        return render(request, 'view_all_my_bookmarks.html', {})

    def post(self, request, *args, **kwargs):
        username = request.user
        user_id = request.user.id
        votes = request.POST
        for k_vote, v_vote in votes.items():
            if k_vote == 'csrfmiddlewaretoken':
                continue
            k_votee = k_vote.split('_')
            ask_question_id = int(k_votee[0])
            vote_type = k_votee[1]
            vote_id = v_vote        
        try:
            if vote_type == 'a':
                User_Vote_A_table.objects.create(user_id_id = user_id, vote_a_id_id = vote_id, ask_question_id_id = ask_question_id).save()
                self.__save_user_votes(Vote_A_table, vote_id)
            if vote_type == 'b':
                User_Vote_B_table.objects.create(user_id_id = user_id, vote_b_id_id = vote_id, ask_question_id_id = ask_question_id).save()
                self.__save_user_votes(Vote_B_table, vote_id)
            if vote_type == 'c':
                User_Vote_C_table.objects.create(user_id_id = user_id, vote_c_id_id = vote_id, ask_question_id_id = ask_question_id).save()
                self.__save_user_votes(Vote_C_table, vote_id)

            has_voted = Has_Voted_Per_Question(vote_type, vote_id)
            has_voted.get_qs_id(user_id)

            messages.success(request, f'You have successfully voted {username}')
            return redirect('get_bookmarks')
        except UnboundLocalError as e:
            print(e)
            messages.warning(request, f'Please select a vote before submitting {username}')
            return redirect('get_bookmarks')
    
    def __save_user_votes(self, vote, vote_id):
        vote = vote.objects.get(id = vote_id)
        vote.total_votes = F('total_votes') + 1
        vote.save()        

class View_My_Bookmarks(View):
    __get_json = Save_Data_To_Json()
    __view_my_bookmarks_json = 'get_bookmarks'

    def get(self, request, *args, **kwargs):
        get_json = self.__get_json.get_json_file(self.__view_my_bookmarks_json)
        return JsonResponse(get_json, safe = False)

class Delete_Bookmark(View):
    def get(self, request, *args, **kwargs):
        user_id = request.user.id
        username = request.user
        question_id = kwargs.get('question_id')
        Bookmark_table.objects.filter(question_id = question_id).delete()
        messages.success(request, f'You successfully deleted a bookmark {username}')
        return redirect('get_bookmarks')

class Set_All_My_Questions(View):
    __get_json = Save_Data_To_Json()
    __base_dir = settings.BASE_DIR
    __view_all_my_qs_json = 'view_all_my_questions'
    __pp = pprint.PrettyPrinter(indent = 3)

    def get(self, request, *args, **kwargs): 
        check_json = self.__base_dir + '/static/json/'+ self.__view_all_my_qs_json +'.json'
        get_qs = View_All_My_Questionss(request.user.id)
        questions = get_qs.get_questions()
        if check_json != 0 or check_json == 0:
            self.__get_json.save_json(questions, self.__view_all_my_qs_json)
        return render(request, 'view_all_my_questions.html', {})
    
    def post(self, request, *args, **kwargs):
        username = request.user
        question_id = request.POST.get('question_id')
        question = request.POST.get('question')
        vote_a_id = request.POST.get('type_a')
        vote_b_id = request.POST.get('type_b')
        vote_c_id = request.POST.get('type_c')
        vote_a = request.POST.get('vote_a')
        vote_b = request.POST.get('vote_b')
        vote_c = request.POST.get('vote_c')

        if question != '':
            Ask_A_Question_table.objects.filter(id = question_id).update(question = question)
        if vote_a != '':
            Vote_A_table.objects.filter(id = vote_a_id).update(vote = vote_a)
        if vote_b != '':
            Vote_B_table.objects.filter(id = vote_b_id).update(vote = vote_b)
        if vote_c != '':
            Vote_C_table.objects.filter(id = vote_c_id).update(vote = vote_c)
        if question == '' and vote_a == '' and vote_b == '' and vote_c == '':
            messages.warning(request, f'You did not update anything so far, you can always try again later if you want {username}')
            return redirect('set_all_my_questions')

        messages.success(request, f'You successfully updated your question or vote(s) {username}')
        return redirect('set_all_my_questions')

class Get_All_My_Questions(View):
    __get_json = Save_Data_To_Json()
    __view_all_my_qs_json = 'view_all_my_questions'

    def get(self, request, *args, **kwargs):
        get_json = self.__get_json.get_json_file(self.__view_all_my_qs_json)
        return JsonResponse(get_json, safe = False)
    
class Edit_All_My_Questions(View):
    __get_json = Save_Data_To_Json()
    __base_dir = settings.BASE_DIR
    __edit_all_my_qs_json = 'edit_all_my_questions'

    def get(self, request, *args, **kwargs):
        to_edit = []
        check_json = self.__base_dir + '/static/json/'+ self.__edit_all_my_qs_json +'.json'
        get_question = Ask_A_Question_table.objects.filter(id = kwargs.get('question_id')).values('id','question','date_updated')[0]
        vote_a = Vote_A_table.objects.filter(id = kwargs.get('vote_a')).values('id','vote','date_updated')[0]
        context_vote_a = {'vote_type': 'type_a', 'vote': vote_a, 'vote_abc': 'vote_a',}
        vote_b = Vote_B_table.objects.filter(id = kwargs.get('vote_b')).values('id','vote','date_updated')[0]
        context_vote_b = {'vote_type': 'type_b', 'vote': vote_b, 'vote_abc': 'vote_b',}
        vote_c = Vote_C_table.objects.filter(id = kwargs.get('vote_c')).values('id','vote','date_updated')[0]
        context_vote_c = {'vote_type': 'type_c', 'vote': vote_c, 'vote_abc': 'vote_c',}
        to_edit.append(get_question)
        to_edit.append(context_vote_a)
        to_edit.append(context_vote_b)
        to_edit.append(context_vote_c)

        if check_json != 0 or check_json == 0:
            self.__get_json.save_json(to_edit, self.__edit_all_my_qs_json)

        return render(request, 'edit_all_my_questions.html', {})

class Get_Edit_All_My_Questions(View):
    __get_json = Save_Data_To_Json()
    __edit_all_my_qs_json = 'edit_all_my_questions'

    def get(self, request, *args, **kwargs):
        get_json = self.__get_json.get_json_file(self.__edit_all_my_qs_json)
        return JsonResponse(get_json, safe = False)    

class Delete(View):
    def get(self, request, *args, **kwargs): 
        username = request.user
        Answer_table.objects.filter(id = kwargs.get('answer_id')).delete()
        User_Questions_Votes_Answers_table.objects.filter(answer_id_id = kwargs.get('answer_id')).delete()
        messages.success(request, f'You have successfully deleted a post {username}')
        return redirect('main')

class Edit(View):
    def get(self, request, *args, **kwargs):
        get_answer = Answer_table.objects.filter(id = kwargs.get('answer_id')).values('id','answer')[0]
        edit = Edit_Answer()
        return render(request, 'edit.html', {'context': get_answer, 'edit': edit})

    def post(self, request, *args, **kwargs):
        username = request.user
        answer_id = request.POST.get('answer_id')
        edit = request.POST.get('edit')
        form = Edit_Answer(request.POST or None)
        
        if form.is_valid():
            Answer_table.objects.filter(id = answer_id).update(answer = edit)

        messages.success(request, f'You have successfully editted and updated {username}')
        return redirect('main')

class Answer_Vote(View):
    def get(self, request, *args, **kwargs):
        answer_vote = Answer_Vote_Form()
        get_question = Ask_A_Question_table.objects.filter(id = kwargs.get('question_id')).values('id','question')[0]
        if kwargs.get('vote_type') == 'a':
            get_vote = Vote_A_table.objects.filter(id = kwargs.get('vote')).values('id','vote')[0]
        if kwargs.get('vote_type') == 'b':
            get_vote = Vote_B_table.objects.filter(id = kwargs.get('vote')).values('id','vote')[0]
        if kwargs.get('vote_type') == 'c':
            get_vote = Vote_C_table.objects.filter(id = kwargs.get('vote')).values('id','vote')[0]

        context = {
            'user_id': request.user.id,
            'question_id': get_question.get('id'),
            'question': get_question.get('question'),
            'vote_id': get_vote.get('id'),
            'vote': get_vote.get('vote'),
            'vote_type': kwargs.get('vote_type'),
        }
        return render(request, 'answer_vote.html', {'context': context, 'form': answer_vote,})

    def post(self, request, *args, **kwargs):
        username = request.user
        Answer_table.objects.create(answer = request.POST.get('answer')).save()
        get_answer = Answer_table.objects.values('id','answer').latest('date_updated')
        
        if request.POST.get('vote_type') == 'a':
            User_Questions_Votes_Answers_table.objects.create(user_id_id = request.POST.get('user_id'), question_id_id = request.POST.get('question_id'), answer_id_id = get_answer.get('id'), vote_a_id = request.POST.get('vote_id'), vote_type = request.POST.get('vote_type')).save()
        if request.POST.get('vote_type') == 'b':
            User_Questions_Votes_Answers_table.objects.create(user_id_id = request.POST.get('user_id'), question_id_id = request.POST.get('question_id'), answer_id_id = get_answer.get('id'), vote_b_id = request.POST.get('vote_id'), vote_type = request.POST.get('vote_type')).save()
        if request.POST.get('vote_type') == 'c':
            User_Questions_Votes_Answers_table.objects.create(user_id_id = request.POST.get('user_id'), question_id_id = request.POST.get('question_id'), answer_id_id = get_answer.get('id'), vote_c_id = request.POST.get('vote_id'), vote_type = request.POST.get('vote_type')).save()

        messages.success(request, f'You have successfully answered your vote {username}')
        return redirect('main')

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
    __pp = pprint.PrettyPrinter(indent = 3)

    def get(self, request, *args, **kwargs):
        check_json = self.__base_dir + '/static/json/'+ self.__all_user_votes_json +'.json'
        all_qs_vs = []

        user_id = request.user.id
        user_vote_a = User_Vote_A_table.objects.filter(user_id_id = user_id).values_list('vote_a_id_id','date_updated').order_by('-date_updated')
        user_vote_b = User_Vote_B_table.objects.filter(user_id_id = user_id).values_list('vote_b_id_id','date_updated').order_by('-date_updated')
        user_vote_c = User_Vote_C_table.objects.filter(user_id_id = user_id).values_list('vote_c_id_id','date_updated').order_by('-date_updated')
 
        from_votes_table_a = View_All_My_Votess(user_vote_a)
        get_votes_a_table_ids = from_votes_table_a.get_from_votes_type('a')
        get_qs_with_its_vote_a = from_votes_table_a.get_from_questions_votes(get_votes_a_table_ids)
        qs_vs_a = from_votes_table_a.get_qs_with_its_vote(get_qs_with_its_vote_a,'a',Vote_A_table,'vote_a')
        context_a = {'vote_type': 'a', 'votes': qs_vs_a}

        from_votes_table_b = View_All_My_Votess(user_vote_b)
        get_votes_b_table_ids = from_votes_table_b.get_from_votes_type('b')
        get_qs_with_its_vote_b = from_votes_table_b.get_from_questions_votes(get_votes_b_table_ids)
        qs_vs_b = from_votes_table_b.get_qs_with_its_vote(get_qs_with_its_vote_b,'b',Vote_B_table,'vote_b')
        context_b = {'vote_type': 'b', 'votes': qs_vs_b}
        
        from_votes_table_c = View_All_My_Votess(user_vote_c)
        get_votes_c_table_ids = from_votes_table_c.get_from_votes_type('c')
        get_qs_with_its_vote_c = from_votes_table_c.get_from_questions_votes(get_votes_c_table_ids)
        qs_vs_c = from_votes_table_c.get_qs_with_its_vote(get_qs_with_its_vote_c,'c',Vote_C_table,'vote_c')
        context_c = {'vote_type': 'c', 'votes': qs_vs_c}

        all_qs_vs.append(context_a)
        all_qs_vs.append(context_b)
        all_qs_vs.append(context_c)
        
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
            #sort_json_qs = SaveToJsonGetQuestions(json_file = self.__all_votes_json, user_id = user_id)
            #if sort_json_qs == True:
            #    return render(request, 'index.html', {})
            check_json = self.__base_dir + '/static/json/'+ self.__all_votes_json +'.json'
            ''' Start from here '''
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
        try:
            if vote_type == 'a':
                User_Vote_A_table.objects.create(user_id_id = user_id, vote_a_id_id = vote_id, ask_question_id_id = ask_question_id).save()
                self.__save_user_votes(Vote_A_table, vote_id)
            if vote_type == 'b':
                User_Vote_B_table.objects.create(user_id_id = user_id, vote_b_id_id = vote_id, ask_question_id_id = ask_question_id).save()
                self.__save_user_votes(Vote_B_table, vote_id)
            if vote_type == 'c':
                User_Vote_C_table.objects.create(user_id_id = user_id, vote_c_id_id = vote_id, ask_question_id_id = ask_question_id).save()
                self.__save_user_votes(Vote_C_table, vote_id)

            has_voted = Has_Voted_Per_Question(vote_type, vote_id)
            has_voted.get_qs_id(user_id)

            messages.success(request, f'You have successfully voted {username}')
            return redirect('main')
        except UnboundLocalError as e:
            print(e)
            messages.warning(request, f'Please select a vote before submitting {username}')
            return redirect('main')

    def __save_user_votes(self, vote, vote_id):
        vote = vote.objects.get(id = vote_id)
        vote.total_votes = F('total_votes') + 1
        vote.save()        
    
    def __get_questions(self, user_id):
        votes_list = []
        get_qs = Ask_A_Question_table.objects.values_list('id').order_by('-date_updated')
        qs = [get_qs[qs] for qs in range(0,len(get_qs))]
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

    def __get_context(self, qs_answers, get_q, user_id, con_vote_a, con_vote_b, con_vote_c, T_F, v_type, v_a, v_b, v_c):
        get_q_id = Ask_A_Question_table.objects.get(id = get_q[0][0])
        get_user_id = get_q_id.user_questions_table_set.values('user_id_id')[0]
        get_username = User.objects.filter(id = get_user_id.get('user_id_id')).values('username')[0]
        group_ans = []
        context = {
            'user_id': user_id,
            'has_voted': T_F,
            'question_id': get_q[0][0],
            'question': get_q[0][1],
            'date': get_q[0][2],
            'vote_a': con_vote_a,
            'vote_b': con_vote_b,
            'vote_c': con_vote_c,
            'vote_type': v_type,
            'vote_a_id': v_a,
            'vote_b_id': v_b,
            'vote_c_id': v_c,
            'answers': group_ans,
            'asked_by': get_username.get('username'),
        }        
        for ans in range(0,len(qs_answers)):
            if get_q[0][0] == qs_answers[ans][0]:
                get_user = User_Questions_Votes_Answers_table.objects.filter(answer_id_id = qs_answers[ans][1].get('id')).values('user_id_id')[0]
                username = User.objects.filter(id = get_user.get('user_id_id')).values('id','username')[0]
                context_ans = {
                    'question_id': get_q[0][0],
                    'answer_id': qs_answers[ans][1].get('id'),
                    'date_updated': qs_answers[ans][1].get('date_updated'),
                    'answer': qs_answers[ans][1].get('answer'),
                    'user_id': username.get('id'),
                    'username': username.get('username'),
                }
                group_ans.append(context_ans)
        return context

class Ask_Question(View):
    def get(self, request, *args, **kwargs):
        question = Ask_A_Question()
        return render(request, 'ask_question.html', {'form':question})

    def post(self, request, *args, **kwargs):
        username = request.user
        if request.user.is_authenticated == True:
            user_id = request.user.id
            if request.method == 'POST':
                question = request.POST.get('ask_question')
                vote_a = request.POST.get('vote_a')
                vote_b = request.POST.get('vote_b')
                vote_c = request.POST.get('vote_c')
                self.__save_question(question, user_id)
                self.__save_votes(vote_a, vote_b, vote_c, user_id)
                self.__save_question_votes()
        messages.success(request, f'You have successfully asked a question {username}')
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
