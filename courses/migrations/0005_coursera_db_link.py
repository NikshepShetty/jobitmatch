# Generated by Django 3.1.4 on 2021-03-05 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_auto_20210301_1938'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursera_db',
            name='Link',
            field=models.CharField(default=100, max_length=500),
        ),
    ]
