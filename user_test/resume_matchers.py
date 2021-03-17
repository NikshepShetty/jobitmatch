from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
from io import StringIO
import docx2txt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from .models import resume,manual_input,Final_Results,Job_description,Technical_skill,Related_job_profile,Skills,Knowledge,Education
from heapq import nlargest 
from courses.skill_mapper import skill_checker


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


def similarity(userid,filtered_list):
    resume_txt=""
    if resume.objects.filter(user=userid).exists():
        resume_file=resume.objects.get(user=userid).files
        resume_txt = pdf_to_string(resume_file)

    elif manual_input.objects.filter(user=userid).exists():
        resume_txt=manual_input.objects.get(user=userid).experience+", "+manual_input.objects.get(user=userid).description+", "+manual_input.objects.get(user=userid).education+", "+manual_input.objects.get(user=userid).technicals


    
    final_list={}

    for i in filtered_list:
        job_desc=""
        job_desc+=Job_description.objects.get(job_profile=i).description
        job_desc+=Technical_skill.objects.get(job_profile=i).Technical_skills
        job_desc+=Related_job_profile.objects.get(job_profile=i).Related_jobs
        job_desc+=Knowledge.objects.get(job_profile=i).Knowledge
        job_desc+=Skills.objects.get(job_profile=i).skills
        job_desc+=Education.objects.get(job_profile=i).education
        text = [resume_txt, job_desc]
        cv = CountVectorizer()
        count_matrix = cv.fit_transform(text) 
        matchPercentage = cosine_similarity(count_matrix)[0][1]*100
        matchPercentage = round(matchPercentage, 2) #The cosine similarity result in percentage
        final_list[i]=matchPercentage
    ThreeHighest = nlargest(3, final_list, key = final_list.get)
    job={}
    for val in ThreeHighest:
        job[val]= final_list[val]
    if Final_Results.objects.filter(user=userid).exists():
        Final_Results.objects.filter(user=userid).delete()
    jobs=Final_Results(
        user=userid,
        recommended_jobs=job
    )
    jobs.save()
    skill_checker(userid)
