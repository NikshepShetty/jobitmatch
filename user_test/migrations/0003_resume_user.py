# Generated by Django 3.1.4 on 2021-01-21 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_test', '0002_remove_resume_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='user',
            field=models.TextField(default='100', max_length=50),
        ),
    ]
