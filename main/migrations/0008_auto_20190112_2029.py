# Generated by Django 2.1.4 on 2019-01-12 20:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_has_voted_per_question_table_vote_a'),
    ]

    operations = [
        migrations.AddField(
            model_name='has_voted_per_question_table',
            name='vote_b',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Vote_B_table'),
        ),
        migrations.AddField(
            model_name='has_voted_per_question_table',
            name='vote_c',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Vote_C_table'),
        ),
    ]
