from django.shortcuts import render
from django.http import HttpResponseRedirect
from .recommendation import course_rec_db
from .skill_mapper import create_profile

def course_ref_view(request):
    if request.method == 'POST':
        course_rec_db()
    return render(request,'rec_courses.html',{})


