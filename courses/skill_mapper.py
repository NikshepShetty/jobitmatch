#Resume Phrase Matcher code


#importing all required libraries

import os
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
from io import StringIO
import pandas as pd
from collections import Counter
import spacy
import en_core_web_sm

nlp = en_core_web_sm.load()
from spacy.matcher import PhraseMatcher
from user_test.models import resume,Final_Results,Technical_skill,manual_input
from .models import user_lacking_skills,coursera_db



def pdf_to_string(file):
    output_string = StringIO()
    parser = PDFParser(file.open())
    doc = PDFDocument(parser)
    codec = 'utf-8'
    rsrcmgr = PDFResourceManager()
    device = TextConverter(rsrcmgr, output_string, codec=codec, laparams=LAParams())
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    for page in PDFPage.create_pages(doc):
        interpreter.process_page(page)
    return(output_string.getvalue())

#function to read resume ends


#function that does phrase matching and builds a candidate profile
def create_profile(file):
    restext = pdf_to_string(file) 
    restext = str(restext)
    restext = restext.replace("\\n", "")
    restext = restext.replace(",", "")
    restext = restext.lower()
    #below is the csv where we have all the keywords, you can customize your own
    keyword_dict = pd.read_csv('courses/course_csv/ProgramsDatabase.csv')
    pro1 = [nlp(text) for text in keyword_dict['Actuaries'].dropna(axis = 0)]
    pro2 = [nlp(text) for text in keyword_dict['Bioinformatics Technicians'].dropna(axis = 0)]
    pro3 = [nlp(text) for text in keyword_dict['Biostaticians'].dropna(axis = 0)]
    pro4 = [nlp(text) for text in keyword_dict['Business Intelligence Analysts'].dropna(axis = 0)]
    pro5 = [nlp(text) for text in keyword_dict['Clinical Data Managers'].dropna(axis = 0)]
    pro6 = [nlp(text) for text in keyword_dict['Computer and Information Research Scientists'].dropna(axis = 0)]
    pro7 = [nlp(text) for text in keyword_dict['Computer Network Support Specialists'].dropna(axis = 0)]
    pro8 = [nlp(text) for text in keyword_dict['Computer Programmers'].dropna(axis = 0)]
    pro9 = [nlp(text) for text in keyword_dict['Computer Systems Analysts'].dropna(axis = 0)]
    pro10 = [nlp(text) for text in keyword_dict['Computer Systems Engineers Architects'].dropna(axis = 0)]
    pro11 = [nlp(text) for text in keyword_dict['Computer User Support Specialists'].dropna(axis = 0)]
    pro12 = [nlp(text) for text in keyword_dict['Data Warehousing Specialists'].dropna(axis = 0)]
    pro13 = [nlp(text) for text in keyword_dict['Database Administrators'].dropna(axis = 0)]
    pro14 = [nlp(text) for text in keyword_dict['Database Architects'].dropna(axis = 0)]
    pro15 = [nlp(text) for text in keyword_dict['Document Management Specialists'].dropna(axis = 0)]
    pro16 = [nlp(text) for text in keyword_dict['Geographic Information Systems Technologists and Technicians'].dropna(axis = 0)]
    pro17 = [nlp(text) for text in keyword_dict['Health Informatics Specialists'].dropna(axis = 0)]
    pro18 = [nlp(text) for text in keyword_dict['Information Security Analysts'].dropna(axis = 0)]
    pro19 = [nlp(text) for text in keyword_dict['Information Technology Project Managers'].dropna(axis = 0)]
    pro21 = [nlp(text) for text in keyword_dict['Network and Computer Systems Administrators'].dropna(axis = 0)]
    pro22 = [nlp(text) for text in keyword_dict['Operations Research Analysts'].dropna(axis = 0)]
    pro23 = [nlp(text) for text in keyword_dict['Software Quality Assurance Analysts and Testers'].dropna(axis = 0)]
    pro24 = [nlp(text) for text in keyword_dict['Statisticians'].dropna(axis = 0)]
    pro25 = [nlp(text) for text in keyword_dict['Telecommunications Engineering Specialists'].dropna(axis = 0)]
    pro26 = [nlp(text) for text in keyword_dict['Video Game Designers'].dropna(axis = 0)]
    pro27 = [nlp(text) for text in keyword_dict['Web Administrators'].dropna(axis = 0)]
    pro28 = [nlp(text) for text in keyword_dict['Web Developers'].dropna(axis = 0)]
    

    matcher = PhraseMatcher(nlp.vocab)
    matcher.add('Actuaries', None, *pro1)
    matcher.add('Bioinformatics Technicians', None, *pro2)
    matcher.add('Biostaticians', None, *pro3)
    matcher.add('Business Intelligence Analysts', None, *pro4)
    matcher.add('Clinical Data Managers', None, *pro5)
    matcher.add('Computer and Information Research Scientists', None, *pro6)
    matcher.add('Computer Network Support Specialists', None, *pro7)
    matcher.add('Computer Programmers', None, *pro8)
    matcher.add('Computer Systems Analysts', None, *pro9)
    matcher.add('Computer Systems Engineers Architects', None, *pro10)
    matcher.add('Computer User Support Specialists', None, *pro11)
    matcher.add('Data Warehousing Specialists', None, *pro12)
    matcher.add('Database Administrators', None, *pro13)
    matcher.add('Database Architects', None, *pro14)
    matcher.add('Document Management Specialists', None, *pro15)
    matcher.add('Geographic Information Systems Technologists and Technicians', None, *pro16)
    matcher.add('Health Informatics Specialists', None, *pro17)
    matcher.add('Information Security Analysts', None, *pro18)
    matcher.add('Information Technology Project Managers', None, *pro19)
    matcher.add('Network and Computer Systems Administrators', None, *pro21)
    matcher.add('Operations Research Analysts', None, *pro22)
    matcher.add('Software Quality Assurance Analysts and Testers', None, *pro23)
    matcher.add('Statisticians', None, *pro24)
    matcher.add('Telecommunications Engineering Specialists', None, *pro25)
    matcher.add('Video Game Designers', None, *pro26)
    matcher.add('Web Administrators', None, *pro27)
    matcher.add('Web Developers', None, *pro28)

    doc = nlp(restext)
    
    d = []  
    matches = matcher(doc)
    for match_id, start, end in matches:
        rule_id = nlp.vocab.strings[match_id]
        span = doc[start : end]  # get the matched slice of the doc
        d.append((span.text))      
    keywords = set(d)
    return(keywords)


def skill_checker(userid):
    dat={}
    if resume.objects.filter(user=userid).exists():
        resume_file=resume.objects.get(user=userid).files
        dat = create_profile(resume_file)
    elif manual_input.objects.filter(user=userid).exists():
        txt=manual_input.objects.get(user=userid).technicals
        txt=txt[:-1]
        dat=set(txt.split(","))
    user_jobs=Final_Results.objects.get(user=userid).recommended_jobs
    user_jobs=eval(user_jobs)
    jobs=list(user_jobs.keys())
    lacking_skills_dict={}
    for i in jobs:
        technical_onet=Technical_skill.objects.get(job_profile=i).Technical_skills
        technical_onet=technical_onet.lower()
        onet_list=technical_onet.split(",")
        onet_list=set(onet_list)
        lacking_skill_in_job=[]
        for user_skill in dat:
            for onet in onet_list:
                if onet.find(user_skill) != -1:
                    lacking_skill_in_job.append(onet)
        lacking_skill_in_job=set(lacking_skill_in_job)
        lacking_skill_in_job=onet_list - lacking_skill_in_job
        filter_list=[]
        for skill in lacking_skill_in_job:
            if coursera_db.objects.filter(Lang=skill).exists():
                filter_list.append(skill)
        lacking_skills_dict[i]=filter_list
    if user_lacking_skills.objects.filter(user=userid).exists():
        user_lacking_skills.objects.filter(user=userid).delete()
    lacking=user_lacking_skills(
        user=userid,
        user_should_learn=lacking_skills_dict
    )
    lacking.save()
                        




    
