# Generated by Django 2.1.4 on 2019-01-09 18:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0002_auto_20190103_1813'),
    ]

    operations = [
        migrations.CreateModel(
            name='Has_Voted_Per_Question_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_updated', models.DateTimeField(auto_now_add=True)),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Ask_A_Question_table')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Has the user answered this questions via voting?',
            },
        ),
    ]
