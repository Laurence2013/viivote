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
    total_votes = models.IntegerField()
    date_updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.vote

    class Meta:
        verbose_name_plural = 'Vote A'

class Vote_B_table(models.Model):
    vote = models.TextField()
    total_votes = models.IntegerField()
    date_updated = models.DateTimeField(auto_now_add = True)
 
    def __str__(self):
        return self.vote

    class Meta:
        verbose_name_plural = 'Vote B'

class Vote_C_table(models.Model):
    vote = models.TextField()
    total_votes = models.IntegerField()
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

# Truncate tables

class User_Questions_table(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE, blank = False)
    question_id = models.ForeignKey(Ask_A_Question_table, on_delete = models.CASCADE, blank = False)
    date_updated = models.DateTimeField(auto_now_add = True)

    #def __str__(self):
    #    return 'User id ', str(self.user_id), ' --> Questions id ', str(self.question_id)

    class Meta:
        verbose_name_plural = 'User and Question'

class Votes_table(models.Model):
    vote_a = models.ForeignKey(Vote_A_table, on_delete = models.CASCADE, blank = False)
    vote_b = models.ForeignKey(Vote_B_table, on_delete = models.CASCADE, blank = False)
    vote_c = models.ForeignKey(Vote_C_table, on_delete = models.CASCADE, blank = False)
    date_updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return 'Vote A id ', str(self.vote_a), ' --> Vote B id ', str(self.vote_b), ' --> Vote C id ', str(self.vote_c)

    class Meta:
        verbose_name_plural = 'Votes'

class Questions_Votes_table(models.Model):
    question_id = models.ForeignKey(Ask_A_Question_table, on_delete = models.CASCADE, blank = False)
    votes_id = models.ForeignKey(Votes_table, on_delete = models.CASCADE, blank = False)
    date_updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return 'Questions id ', str(self.question_id), ' --> Votes id ', str(self.votes_id)

    class Meta:
        verbose_name_plural = 'Question and Votes'

class User_Questions_Votes_Answers_table(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE, blank = False)
    question_id = models.ForeignKey(Ask_A_Question_table, on_delete = models.CASCADE, blank = False)
    answer_id = models.ForeignKey(Answer_table, on_delete = models.CASCADE, blank = False)
    date_updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return 'User id ', str(self.user_id), ' --> Question id ', str(self.question_id), ' --> Answers id ', str(self.answer_id)

    class Meta:
        verbose_name_plural = 'User and Questions and Answers'

class User_Vote_A_table(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE, blank = False)
    vote_a_id = models.ForeignKey(Vote_A_table, on_delete = models.CASCADE, blank = False)
    date_updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return 'User id ', str(self.user_id), ' --> Vote A id ', str(self.vote_a_id)

    class Meta:
        verbose_name_plural = 'Users and Vote A'

class User_Vote_B_table(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE, blank = False)
    vote_b_id = models.ForeignKey(Vote_B_table, on_delete = models.CASCADE, blank = False)
    date_updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return 'User id ', str(self.user_id), ' --> Vote B id ', str(self.vote_b_id)

    class Meta:
        verbose_name_plural = 'Users and Vote B'

class User_Vote_C_table(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE, blank = False)
    vote_c_id = models.ForeignKey(Vote_C_table, on_delete = models.CASCADE, blank = False)
    date_updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return 'User id ', str(self.user_id), ' --> Vote C id ', str(self.vote_c_id)

    class Meta:
        verbose_name_plural = 'Users and Vote C'
