# Generated by Django 3.1.4 on 2021-02-09 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_test', '0016_auto_20210206_2352'),
    ]

    operations = [
        migrations.CreateModel(
            name='technical_list',
            fields=[
                ('technical', models.CharField(max_length=40, primary_key=True, serialize=False)),
            ],
        ),
    ]
