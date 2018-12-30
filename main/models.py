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
    
