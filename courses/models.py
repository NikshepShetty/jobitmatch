from django.db import models

class coursera_db(models.Model):
    Lang=models.CharField(max_length=200, default=100)
    Name=models.CharField(max_length=300, default=100)
    Type=models.CharField(max_length=300, default=100)
    Company=models.CharField(max_length=300,default=100)
    Rating=models.DecimalField(max_digits=3,decimal_places=2)
    Difficulty=models.CharField(max_length=30, default=100)
    Link=models.CharField(max_length=500, default=100)

    def __str__(self):
        return self.Lang

class user_lacking_skills(models.Model):
    user = models.CharField(max_length=30, default=100, primary_key=True)
    user_should_learn=models.CharField(max_length=1000, default="None")
    def __str__(self):
        return 'UserID {0}'.format(self.user)

