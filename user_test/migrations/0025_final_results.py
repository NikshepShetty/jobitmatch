# Generated by Django 3.1.4 on 2021-02-27 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_test', '0024_manual_input_achievements'),
    ]

    operations = [
        migrations.CreateModel(
            name='Final_Results',
            fields=[
                ('user', models.CharField(default=100, max_length=30, primary_key=True, serialize=False)),
                ('recommended_jobs', models.CharField(default='None', max_length=1000)),
            ],
        ),
    ]
