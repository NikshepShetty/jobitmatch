# Generated by Django 3.1.4 on 2021-01-21 20:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='achievement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('achievements', models.CharField(max_length=5000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='manual_input',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employed', models.CharField(max_length=3)),
                ('experience', models.IntegerField(validators=[django.core.validators.MaxValueValidator(70), django.core.validators.MinValueValidator(0)])),
                ('education', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('files', models.FileField(upload_to='')),
                ('user', models.TextField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='technical',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('technicals', models.CharField(max_length=5000, null=True)),
            ],
        ),
    ]
