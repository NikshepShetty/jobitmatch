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


def create_profile(file):
    restext = pdf_to_string(file) 
    restext = str(restext)
    restext = restext.replace("\\n", "")
    restext = restext.replace(",", "")
    restext = restext.lower()
    #below is the csv where we have all the keywords, you can customize your own
    keyword_dict = pd.read_csv('courses/course_csv/Programs.csv')
    keys = [nlp(text) for text in keyword_dict['Programs'].dropna(axis = 0)]

    matcher = PhraseMatcher(nlp.vocab)
    matcher.add('Programs', None, *keys)

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
                        




    
