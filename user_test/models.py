from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

class resume(models.Model):
    files=models.FileField()
    user =models.CharField(max_length=30,default=100, primary_key=True)
    def __str__(self):
        return 'UserID {0}'.format(self.user)

class manual_input(models.Model):
    user =models.CharField(max_length=30,default=100, primary_key=True)
    experience=models.CharField(null=True, max_length=5000)
    education = models.CharField(max_length=50, null=False)
    description=models.CharField(null=True,max_length=5000)
    technicals=models.CharField(null=True,max_length=5000)
    def __str__(self):
        return 'UserID {0}'.format(self.user)

class technical_list(models.Model):
    technical=models.CharField(max_length=40, default=0)
    def __str__(self):
        return u'{0}'.format(self.technical)

RIASEC=(('R','Realistic'),('I','Investigative'),('A','Artistic'),('S','Social'),('E','Enterprising'),('C','Conventional'))

class holland(models.Model):
    question=models.CharField(null=False, max_length=50)
    interest_type=models.CharField(choices=RIASEC,null=False, max_length=15)

class holland_score(models.Model):
    user = models.CharField(max_length=30, default=100, primary_key=True)
    realistic = models.IntegerField(null=False,validators=[MaxValueValidator(100), MinValueValidator(0)])
    investigative = models.IntegerField(null=False,validators=[MaxValueValidator(100), MinValueValidator(0)])
    artistic = models.IntegerField(null=False,validators=[MaxValueValidator(100), MinValueValidator(0)])
    social = models.IntegerField(null=False,validators=[MaxValueValidator(100), MinValueValidator(0)])
    enterprising = models.IntegerField(null=False,validators=[MaxValueValidator(100), MinValueValidator(0)])
    conventional = models.IntegerField(null=False,validators=[MaxValueValidator(100), MinValueValidator(0)])
    def __str__(self):
        return 'UserID {0}'.format(self.user)

class Holland_interests(models.Model):
    job_profile=models.CharField(max_length=300, default=100)
    Holland_interest=models.CharField(max_length=4000, default=100)
    def __str__(self):
        return self.job_profile

class Job_description(models.Model):
    job_profile=models.CharField(max_length=300, default=100)
    description=models.CharField(max_length=4000, default=100)
    def __str__(self):
        return self.job_profile

class Related_job_profile(models.Model):
    job_profile=models.CharField(max_length=300, default=100)
    Related_jobs=models.CharField(max_length=4000, default=100)
    def __str__(self):
        return self.job_profile

class Technical_skill(models.Model):
    job_profile=models.CharField(max_length=300, default=100)
    Technical_skills=models.CharField(max_length=4000, default=100)
    def __str__(self):
        return self.job_profile
    
class User_Filtered_Job(models.Model):
    user = models.CharField(max_length=30, default=100, primary_key=True)
    filtered_list = models.CharField(max_length=1000, default="None")
    def __str__(self):
        return 'UserID {0}'.format(self.user)

class Final_Results(models.Model):
    user = models.CharField(max_length=30, default=100, primary_key=True)
    recommended_jobs = models.CharField(max_length=1000, default="None")
    def __str__(self):
        return 'UserID {0}'.format(self.user)

class Knowledge(models.Model):
    job_profile=models.CharField(max_length=300, default=100)
    Knowledge=models.CharField(max_length=4000, default=100)
    def __str__(self):
        return self.job_profile

class Skills(models.Model):
    job_profile=models.CharField(max_length=300, default=100)
    skills=models.CharField(max_length=4000, default=100)
    def __str__(self):
        return self.job_profile

class Education(models.Model):
    job_profile=models.CharField(max_length=300, default=100)
    education=models.CharField(max_length=4000, default=100)
    def __str__(self):
        return self.job_profile