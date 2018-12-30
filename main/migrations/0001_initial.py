# Generated by Django 2.1.4 on 2018-12-30 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField()),
                ('date_updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Answer',
            },
        ),
        migrations.CreateModel(
            name='Ask_A_Question_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('date_updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Ask a question',
            },
        ),
        migrations.CreateModel(
            name='Category_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Astrophysicist', 'Astrophysicist'), ('Civil Engineering', 'Civil Engineering'), ('Politics', 'Politics')], max_length=100)),
                ('date_updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Category',
            },
        ),
        migrations.CreateModel(
            name='Vote_A_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote', models.TextField()),
                ('total_votes', models.IntegerField()),
                ('date_updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Vote A',
            },
        ),
        migrations.CreateModel(
            name='Vote_B_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote', models.TextField()),
                ('total_votes', models.IntegerField()),
                ('date_updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Vote B',
            },
        ),
        migrations.CreateModel(
            name='Vote_C_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote', models.TextField()),
                ('total_votes', models.IntegerField()),
                ('date_updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Vote C',
            },
        ),
    ]