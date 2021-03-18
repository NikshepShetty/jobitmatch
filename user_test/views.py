from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ResumeInput,ManualInput,holland_choices
from django.contrib.auth.decorators import login_required
from user_test.models import holland, holland_score,resume,manual_input,User_Filtered_Job,Final_Results,Job_description,Technical_skill,Skills,Education,Related_job_profile
from django.forms.formsets import formset_factory, BaseFormSet
from .Onet_extract import xml_extract
from .job_filter import holland_filter
from courses.models import user_lacking_skills,coursera_db
from django.template.defaulttags import register
from courses.recommendation import keylist
from courses.skill_mapper import skill_checker


@login_required
def test_start_view(request):
    if request.method == 'POST':
        form = ResumeInput(request.POST,request.FILES)
        if form.is_valid():
            if resume.objects.filter(user=request.user.id).exists():
                resume.objects.filter(user=request.user.id).delete()
                
            stock = form.save(commit=False)
            stock.user = request.user.id
            stock.save()
            return HttpResponseRedirect('/test/interests')
    else:
        form = ResumeInput()
    return render(request, 'test_start.html', {'form': form})

@login_required
def manual_input_view(request):
    keys=keylist()
    if request.method == 'POST':
        form = ManualInput(request.POST, request.FILES)
        if form.is_valid():
            if manual_input.objects.filter(user=request.user.id).exists():
                manual_input.objects.filter(user=request.user.id).delete()
                
            stock = form.save(commit=False)
            stock.user = request.user.id
            stock.save()
            return HttpResponseRedirect('/test/interests')
    else:
        form = ManualInput()
    return render(request, 'manual_input.html', {'form': form,'keys':keys})

class RequiredFormSet(BaseFormSet):
    def __init__(self, *args, **kwargs):
        super(RequiredFormSet, self).__init__(*args, **kwargs)
        for form in self.forms:
            form.empty_permitted = False


user_score={'R':0,'I':0,'A':0,'S':0,'E':0,'C':0}


@login_required
def interest_view(request):
    realistic_total=holland.objects.filter(interest_type__exact='R').count()
    investigative_total=holland.objects.filter(interest_type__exact='I').count()
    artistic_total=holland.objects.filter(interest_type__exact='A').count()
    social_total=holland.objects.filter(interest_type__exact='S').count()
    enterprising_total=holland.objects.filter(interest_type__exact='E').count()
    conventional_total=holland.objects.filter(interest_type__exact='C').count()
    questions= holland.objects.all()
    total_questions=questions.count()
    Holland_Set = formset_factory(holland_choices,formset=RequiredFormSet, extra=total_questions)
    global user_score
    if request.method == 'POST':
        formset = Holland_Set(request.POST, request.FILES)
        if formset.is_valid():
            count=1
            for form in formset:
                if form.is_valid():
                    holland_result(form.cleaned_data['user_choice'], count)
                    count+=1
            if holland_score.objects.filter(user=request.user.id).exists():
                holland_score.objects.filter(user=request.user.id).delete()
                
            score=holland_score(
                user=request.user.id,
                realistic=(user_score['R']/realistic_total)*25,
                investigative=(user_score['I']/investigative_total)*25,
                artistic=(user_score['A']/artistic_total)*25,
                social=(user_score['S']/social_total)*25,
                enterprising=(user_score['E']/enterprising_total)*25,
                conventional=(user_score['C']/conventional_total)*25,
            )
            score.save()
            holland_filter(request.user.id)
            user_score={'R':0,'I':0,'A':0,'S':0,'E':0,'C':0}
            return HttpResponseRedirect('/test/result')

    else:
        formset = Holland_Set()
    return render(request,'interest.html', {'formset': formset,'questions':questions})

def holland_result(choice, question_number):
    agree=4
    slightly_agree=3
    neutral=2
    slightly_disagree=1

    #Realistic
    if (holland.objects.get(id__exact=question_number)).interest_type=='R':
        if choice=='agree':
            user_score['R']+=agree
        elif choice=='slightly agree':
            user_score['R']+=slightly_agree
        elif choice=='neutral':
            user_score['R']+=neutral
        elif choice=='slightly disagree':
            user_score['R']+=slightly_disagree

    #Investigative    
    elif (holland.objects.get(id__exact=question_number)).interest_type=='I':
        if choice=='agree':
            user_score['I']+=agree
        elif choice=='slightly agree':
            user_score['I']+=slightly_agree
        elif choice=='neutral':
            user_score['I']+=neutral
        elif choice=='slightly disagree':
            user_score['I']+=slightly_disagree

    #Artisitc
    elif (holland.objects.get(id__exact=question_number)).interest_type=='A':
        if choice=='agree':
            user_score['A']+=agree
        elif choice=='slightly agree':
            user_score['A']+=slightly_agree
        elif choice=='neutral':
            user_score['A']+=neutral
        elif choice=='slightly disagree':
            user_score['A']+=slightly_disagree
    #Social
    elif (holland.objects.get(id__exact=question_number)).interest_type=='S':
        if choice=='agree':
            user_score['S']+=agree
        elif choice=='slightly agree':
            user_score['S']+=slightly_agree
        elif choice=='neutral':
            user_score['S']+=neutral
        elif choice=='slightly disagree':
            user_score['S']+=slightly_disagree
    #Enterprising
    elif (holland.objects.get(id__exact=question_number)).interest_type=='E':
        if choice=='agree':
            user_score['E']+=agree
        elif choice=='slightly agree':
            user_score['E']+=slightly_agree
        elif choice=='neutral':
            user_score['E']+=neutral
        elif choice=='slightly disagree':
            user_score['E']+=slightly_disagree
    #Conventional
    elif (holland.objects.get(id__exact=question_number)).interest_type=='C':
        if choice=='agree':
            user_score['C']+=agree
        elif choice=='slightly agree':
            user_score['C']+=slightly_agree
        elif choice=='neutral':
            user_score['C']+=neutral
        elif choice=='slightly disagree':
            user_score['C']+=slightly_disagree

@register.filter
def keyvalue(dict, key):    
    return dict[key]

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
def length(value):
    return len(value)

@register.filter
def add_space_after_comma(value):
    return value.replace(",",", ")

@login_required
def result_view(request):
    skill_checker(request.user.id)
    jobs=""
    if Final_Results.objects.filter(user=request.user.id).exists():
        jobs=Final_Results.objects.get(user=request.user.id).recommended_jobs
    else:
        HttpResponseRedirect("/test/")
    jobs=eval(jobs)
    lacking_skills=""
    if user_lacking_skills.objects.filter(user=request.user.id).exists():
        lacking_skills=user_lacking_skills.objects.get(user=request.user.id).user_should_learn
    else:
        HttpResponseRedirect("/test/")
    lacking_skills=eval(lacking_skills)
    course_list=[]
    for value in lacking_skills.values():
        for i in value:
            if coursera_db.objects.filter(Lang=i).exists():
                course_list.append(i)
    course_list=set(course_list)
    hollandScore=[]
    if holland_score.objects.filter(user=request.user.id).exists():
        hollandScore.append(holland_score.objects.get(user=request.user.id).realistic)
        hollandScore.append(holland_score.objects.get(user=request.user.id).investigative)
        hollandScore.append(holland_score.objects.get(user=request.user.id).artistic)
        hollandScore.append(holland_score.objects.get(user=request.user.id).social)
        hollandScore.append(holland_score.objects.get(user=request.user.id).enterprising)
        hollandScore.append(holland_score.objects.get(user=request.user.id).conventional)
        
    course_dict={}
    for software in course_list:
        list_of_courses=[]
        if coursera_db.objects.filter(Lang=software).exists():
            obj=coursera_db.objects.filter(Lang=software)
        else:
            continue
        for element in obj:
            course_str=""
            course_str=element.Name.replace(" ","_")+" "+element.Type.replace(" ","_")+" "+element.Company.replace(" ","_")+" "+str(element.Rating)+" "+element.Difficulty+" "+element.Link
            list_of_courses.append(course_str)
        course_dict[software]=list_of_courses
    info_dict={}
    for job in jobs.keys():
        temp_list=[]
        temp_list.append(Related_job_profile.objects.get(job_profile=job).Related_jobs)
        temp_list.append(Job_description.objects.get(job_profile=job).description)
        temp_list.append(Technical_skill.objects.get(job_profile=job).Technical_skills)
        info_dict[job]=temp_list
    return render(request,'result.html',{"jobs":jobs,"lacking_skills":lacking_skills,"course_dict":course_dict,"info_dict":info_dict,"Hscore":hollandScore})
    

def onet_ref_view(request):
    if request.method == 'POST':
        xml_extract()
    return render(request,'onet_refresh.html',{})

