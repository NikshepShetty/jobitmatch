# Generated by Django 3.1.4 on 2021-02-25 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_test', '0021_auto_20210213_0140'),
    ]

    operations = [
        migrations.CreateModel(
            name='Holland_interests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_profile', models.CharField(default=100, max_length=300)),
                ('Holland_interest', models.CharField(default=100, max_length=4000)),
            ],
        ),
        migrations.CreateModel(
            name='Job_description',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_profile', models.CharField(default=100, max_length=300)),
                ('description', models.CharField(default=100, max_length=4000)),
            ],
        ),
        migrations.CreateModel(
            name='Related_job_profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_profile', models.CharField(default=100, max_length=300)),
                ('Related_jobs', models.CharField(default=100, max_length=4000)),
            ],
        ),
        migrations.CreateModel(
            name='Technical_skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_profile', models.CharField(default=100, max_length=300)),
                ('Technical_skills', models.CharField(default=100, max_length=4000)),
            ],
        ),
    ]
