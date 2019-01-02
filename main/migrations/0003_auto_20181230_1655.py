# Generated by Django 2.1.4 on 2018-12-30 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_user_question_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questions_Votes_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_updated', models.DateTimeField(auto_now_add=True)),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Ask_A_Question_table')),
            ],
            options={
                'verbose_name_plural': 'Question and Votes',
            },
        ),
        migrations.CreateModel(
            name='Votes_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_updated', models.DateTimeField(auto_now_add=True)),
                ('vote_a', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Vote_A_table')),
                ('vote_b', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Vote_B_table')),
                ('vote_c', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Vote_C_table')),
            ],
            options={
                'verbose_name_plural': 'Votes',
            },
        ),
        migrations.AddField(
            model_name='questions_votes_table',
            name='votes_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Votes_table'),
        ),
    ]