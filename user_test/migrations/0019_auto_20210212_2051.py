# Generated by Django 3.1.4 on 2021-02-12 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_test', '0018_auto_20210209_2157'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manual_input',
            name='achievements',
        ),
        migrations.RemoveField(
            model_name='manual_input',
            name='technicals',
        ),
    ]
