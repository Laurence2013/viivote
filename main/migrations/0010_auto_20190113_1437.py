# Generated by Django 2.1.4 on 2019-01-13 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_has_voted_per_question_table_vote_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_questions_votes_answers_table',
            name='vote_a',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Vote_A_table'),
        ),
        migrations.AddField(
            model_name='user_questions_votes_answers_table',
            name='vote_b',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Vote_B_table'),
        ),
        migrations.AddField(
            model_name='user_questions_votes_answers_table',
            name='vote_c',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Vote_C_table'),
        ),
        migrations.AddField(
            model_name='user_questions_votes_answers_table',
            name='vote_type',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]