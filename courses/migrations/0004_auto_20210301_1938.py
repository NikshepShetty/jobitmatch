# Generated by Django 3.1.4 on 2021-03-01 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20210301_1936'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_lacking_skills',
            old_name='user_skill',
            new_name='user_should_learn',
        ),
    ]
