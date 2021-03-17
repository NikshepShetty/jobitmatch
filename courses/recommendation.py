from bs4 import BeautifulSoup
import requests
from courses.models import coursera_db
import pandas as pd
import re

def keylist():
    cname=["Programs"]
    reader = pd.read_csv('courses/course_csv/ProgramDatabase1.csv', names=cname)
    keywordslist=reader.Programs.to_list()
    return keywordslist

def course_link(key):
    url = "https://www.coursera.org/search?query=" + key + "&page=&index=prod_all_products_term_optimization"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    li=[]
    a=soup.find_all(class_='tab-contents')
    b=(a[0].find_all('script')[0])
    b=str(b)
    b=b.strip()
    z=b[35:len(b)-9]
    z=z.strip()
    v=z[69:len(z)-1]
    v=eval(v)
    for i in range(3):
        li.append(v[i]['url'])
    return li

def Scraper(tag,clas,key):
    l=[]
    url = "https://www.coursera.org/search?query="+key+"&page=&index=prod_all_products_term_optimization"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    for j in range(3):
        x = soup.find_all(tag,clas)[j].get_text()
        l.append(x)
    return l

def course_rec_db():
    regex=re.compile(r'^[a-zA-Z0-9\s!-~]+$')
    Course_name, Course_type, Company_l, Rating_l, Difficulty_l, links_l = [],[],[],[],[],[]
    keywords=keylist()
    coursera_db.objects.all().delete()
    for key in keywords:
        try:
            Course_name=Scraper('h2','color-primary-text card-title headline-1-text',key)
            Course_type=Scraper('div','_jen3vs _1d8rgfy3',key)
            Company_l=Scraper('span','partner-name m-b-1s',key)
            Rating_l=Scraper('span','ratings-text',key)
            Difficulty_l=Scraper('span','difficulty',key)
            links_l=course_link(key)
            for i in range(len(Course_name)):
                name_course=str(Course_name[i])
                name_course.replace(" ","")
                if regex.search(name_course)==None:
                    continue
                else:
                    coursera=coursera_db(
                        Lang=key,
                        Name=Course_name[i],
                        Type=Course_type[i],
                        Company=Company_l[i],
                        Rating=Rating_l[i],
                        Difficulty=Difficulty_l[i],
                        Link=links_l[i]
                    )
                    coursera.save()
        except:
            continue