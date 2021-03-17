from django.shortcuts import render
from user_test.models import Job_description, Related_job_profile, Technical_skill, Knowledge, Skills, Education
from django.template.defaulttags import register

# Create your views here.
def home_view(request):
    return render(request,'home.html', {'nbar':'home'})


def about_view(request):
    return render(request,'about.html', {'nbar':'about'})


def job_profile_view(request):
    jobs=Job_description.objects.all()
    info_dict={}
    for job in jobs:
        info_list=[]
        info_list.append(Job_description.objects.get(job_profile=job).description)
        info_list.append(Related_job_profile.objects.get(job_profile=job).Related_jobs)
        info_list.append(Technical_skill.objects.get(job_profile=job).Technical_skills)
        info_list.append(Knowledge.objects.get(job_profile=job).Knowledge)
        info_list.append(Skills.objects.get(job_profile=job).skills)
        info_list.append(Education.objects.get(job_profile=job).education)
        info_dict[job]=info_list
    return render(request,'job_profile.html', {'nbar':'job_profile','info':info_dict})


@register.filter
def keyvalue(dict, key):    
    return dict[key]

@register.filter
def notdivibleby2(value):
    if value%2!=0:
        return True
    else:
        return False

@register.filter
def underscore_space(value):
    return value.replace("_"," ")

@register.filter
def underscore_hyphen(value):
    return value.replace("_","-")

@register.filter
def split(value):
    return value.split(' ')

@register.filter
def split_dot(value):
    return value.split('.')

@register.filter
def split_comma(value):
    return value.split(',')

@register.filter
def length(value):
    return len(value)

@register.filter
def add_space_after_comma(value):
    return value.replace(",",", ")