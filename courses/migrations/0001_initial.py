# Generated by Django 3.1.4 on 2021-02-25 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='coursera_db',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Lang', models.CharField(default=100, max_length=200)),
                ('Name', models.CharField(default=100, max_length=300)),
                ('Type', models.CharField(default=100, max_length=300)),
                ('Company', models.CharField(default=100, max_length=300)),
                ('Rating', models.DecimalField(decimal_places=2, max_digits=3)),
                ('Difficulty', models.CharField(default=100, max_length=30)),
            ],
        ),
    ]