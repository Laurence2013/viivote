from django.contrib.auth.models import User
from django.db import models

class Category_table(models.Model):
    CATEGORY_TYPE = (
            ('Astrophysicist','Astrophysicist'),
            ('Civil Engineering','Civil Engineering'),
            ('Politics','Politics'),
    )
    category = models.CharField(max_length = 100, choices = CATEGORY_TYPE)
    date_updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name_plural = 'Category'

class Ask_A_Question_table(models.Model):
    question = models.TextField()
    date_updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.question

    class Meta:
        verbose_name_plural = 'Ask a question'

class Vote_A_table(models.Model):
    vote = models.TextField()
    total_votes = models.IntegerField(default = 0)
    date_updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.vote

    class Meta:
        verbose_name_plural = 'Vote A'

class Vote_B_table(models.Model):
    vote = models.TextField()
    total_votes = models.IntegerField(default = 0)
    date_updated = models.DateTimeField(auto_now_add = True)
 
    def __str__(self):
        return self.vote

    class Meta:
        verbose_name_plural = 'Vote B'

class Vote_C_table(models.Model):
    vote = models.TextField()
    total_votes = models.IntegerField(default = 0)
    date_updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.vote

    class Meta:
        verbose_name_plural = 'Vote C'

class Answer_table(models.Model):
    answer = models.TextField()
    date_updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.answer

    class Meta:
        verbose_name_plural = 'Answer'

# Surrogate tables
class User_Questions_table(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE, blank = False)
    question_id = models.ForeignKey(Ask_A_Question_table, on_delete = models.CASCADE, blank = False)
    date_updated = models.DateTimeField(auto_now_add = True)
    
    class Meta:
        verbose_name_plural = 'User and Question'

class Votes_table(models.Model):
    vote_a = models.ForeignKey(Vote_A_table, on_delete = models.CASCADE, blank = False)
    vote_b = models.ForeignKey(Vote_B_table, on_delete = models.CASCADE, blank = False)
    vote_c = models.ForeignKey(Vote_C_table, on_delete = models.CASCADE, blank = False)
    date_updated = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name_plural = 'Votes'

class Questions_Votes_table(models.Model):
    question_id = models.ForeignKey(Ask_A_Question_table, on_delete = models.CASCADE, blank = False)
    votes_id = models.ForeignKey(Votes_table, on_delete = models.CASCADE, blank = False)
    date_updated = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name_plural = 'Question and Votes'

class User_Vote_A_table(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE, blank = False)
    vote_a_id = models.ForeignKey(Vote_A_table, on_delete = models.CASCADE, blank = False)
    ask_question_id = models.ForeignKey(Ask_A_Question_table, on_delete = models.CASCADE, blank = False)
    date_updated = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name_plural = 'Users and Vote A'

class User_Vote_B_table(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE, blank = False)
    vote_b_id = models.ForeignKey(Vote_B_table, on_delete = models.CASCADE, blank = False)
    ask_question_id = models.ForeignKey(Ask_A_Question_table, on_delete = models.CASCADE, blank = False)
    date_updated = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name_plural = 'Users and Vote B'

class User_Vote_C_table(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE, blank = False)
    vote_c_id = models.ForeignKey(Vote_C_table, on_delete = models.CASCADE, blank = False)
    ask_question_id = models.ForeignKey(Ask_A_Question_table, on_delete = models.CASCADE, blank = False)
    date_updated = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name_plural = 'Users and Vote C'

class Has_Voted_Per_Question_table(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE, blank = False)
    question_id = models.ForeignKey(Ask_A_Question_table, on_delete = models.CASCADE, blank = False)
    vote_type = models.CharField(max_length = 10, blank = False)
    vote_a = models.ForeignKey(Vote_A_table, on_delete = models.CASCADE, blank = True, null = True)
    vote_b = models.ForeignKey(Vote_B_table, on_delete = models.CASCADE, blank = True, null = True)
    vote_c = models.ForeignKey(Vote_C_table, on_delete = models.CASCADE, blank = True, null = True)
    date_updated = models.DateTimeField(auto_now_add = True)
    
    class Meta:
        verbose_name_plural = 'Has the user answered this questions via voting?'

class User_Questions_Votes_Answers_table(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE, blank = False)
    question_id = models.ForeignKey(Ask_A_Question_table, on_delete = models.CASCADE, blank = False)
    answer_id = models.ForeignKey(Answer_table, on_delete = models.CASCADE, blank = False)
    vote_type = models.CharField(max_length = 10, blank = False, null = True)
    vote_a = models.ForeignKey(Vote_A_table, on_delete = models.CASCADE, blank = True, null = True)
    vote_b = models.ForeignKey(Vote_B_table, on_delete = models.CASCADE, blank = True, null = True)
    vote_c = models.ForeignKey(Vote_C_table, on_delete = models.CASCADE, blank = True, null = True)
    date_updated = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name_plural = 'User and Questions and Answers'

class Bookmark_table(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE, blank = False)
    question_id = models.ForeignKey(Ask_A_Question_table, on_delete = models.CASCADE, blank = False)
    date_updated = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name_plural = 'All bookmarked questions from a user'

