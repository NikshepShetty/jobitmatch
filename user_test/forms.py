from django import forms
from .models import resume, manual_input, technical_list
from .validate import file_size,validate_file_extension
from django.core.validators import MaxValueValidator, MinValueValidator
from django_select2 import forms as s2forms
from django_select2.forms import Select2TagWidget
from django.db.models.fields import BLANK_CHOICE_DASH


class ResumeInput(forms.ModelForm):
    files= forms.FileField(required=True,validators=[file_size,validate_file_extension],label='')
    class Meta:
        model=resume
        fields=['files']

yesorno=[('yes','Yes'),('no','No')]

education_list=[
    ('No formal education','No formal education'),
    ('Primary education','Primary education'),
    ('Secondary education or high school','Secondary education or high school'),
    ('Vocational qualification','Vocational qualification'),
    ("Bachelor's degree - CS/IT","Bachelor's degree - CS/IT"),
    ("Master's degree - CS/IT","Master's degree - CS/IT"),
    ('Doctorate or higher - CS/IT','Doctorate or higher - CS/IT'),
    ("Bachelor's degree - Others","Bachelor's degree - Others"),
    ("Master's degree - Others","Master's degree - Others"),
    ('Doctorate or higher - Others','Doctorate or higher - Others')
    ]

class ManualInput(forms.ModelForm):
    experience=forms.CharField(widget=forms.Textarea(attrs={'rows':'4','minlength':'50'}),label='Work Experience/ Projects')
    education= forms.CharField(required=True,widget=forms.Select(choices=BLANK_CHOICE_DASH + education_list))
    description=forms.CharField(widget=forms.Textarea(attrs={'rows':'4','minlength':'50'}))

    class Meta:
        model=manual_input
        fields=['experience','education','technicals','description']
        
agreeornot=(('disagree',''),('slightly disagree',''),('neutral',''),('slightly agree',''),('agree',''))


class holland_choices(forms.Form):
    user_choice=forms.ChoiceField(label='',required=True,choices=agreeornot,widget=forms.RadioSelect(attrs={'class': 'form-check-inline','class': 'required'}))

    
