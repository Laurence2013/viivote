from django.contrib.auth.models import User
from django.views.generic import View
from django.shortcuts import HttpResponse, render
from main.forms import Ask_A_Question
from main.models import *

class Main(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html', {})

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
        return HttpResponse('Hello world')

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

