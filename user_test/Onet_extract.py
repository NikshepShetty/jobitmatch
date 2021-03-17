import xml.etree.ElementTree as ET
import webbrowser
from user_test.models import Holland_interests, Job_description, Related_job_profile, Technical_skill,Knowledge,Skills,Education


def xml_extract():
    MyTree=ET.parse('15-0000')
    myroot=MyTree.getroot()
    codel=['garbage']
    titlel=['garbage']
    for x in myroot.findall('occupation'):
        code=x.findtext('code')
        title=x.findtext('title')
        codel.append(code)
        titlel.append(title)

    for i in range(1,len(codel)):
        # interest_url= 'https://services.onetcenter.org/ws/online/occupations/'+codel[i]+'/summary/interests'
        # job_profiles_url = 'https://services.onetcenter.org/ws/online/occupations/'+codel[i]+'/'
        # tech_url='https://services.onetcenter.org/ws/online/occupations/'+codel[i]+'/summary/technology_skills'
        # task_url='https://services.onetcenter.org/ws/online/occupations/'+codel[i]+'/details/tasks'
        # skills_url='https://services.onetcenter.org/ws/online/occupations/'+codel[i]+'/summary/skills'
        # knowledge_url='https://services.onetcenter.org/ws/online/occupations/'+codel[i]+'/summary/knowledge'
        # education_url='https://services.onetcenter.org/ws/online/occupations/'+codel[i]+'/summary/education'

        # webbrowser.open_new_tab(job_profiles_url)
        # webbrowser.open_new_tab(interest_url)
        # webbrowser.open_new_tab(tech_url)
        # webbrowser.open_new_tab(tasks_url)
        # webbrowser.open_new_tab(knowledge_url)
        # webbrowser.open_new_tab(education_url)
        # webbrowser.open_new_tab(skills_url)
        
        interests_file = 'Interests/interests ' + '(' + str(i) + ')'
        downloads_file = 'Download/download ' + '(' + str(i) + ')'
        Tech_skills = 'Technology_skills/technology_skills ' + '(' + str(i) + ')'
        tasks = 'Tasks/tasks ' + '(' + str(i) + ')'
        knowledge_file='Knowledge/knowledge ' + '(' + str(i) + ')'
        skills_file='Skills/skills ' + '(' + str(i) + ')'
        education_file='Education/education ' + '(' + str(i) + ')'
        
        MyTree4 = ET.parse(tasks)                                    #Extract description
        myroot4 = MyTree4.getroot()
        descriptions = ''
        for x in myroot4.findall('task'):
            descriptions = descriptions + x.findtext('statement') + ' '
        if Job_description.objects.filter(job_profile=titlel[i]).exists():
            Job_description.objects.filter(job_profile=titlel[i]).delete()
        desc=Job_description(
            job_profile=titlel[i],
            description=descriptions
        )
        desc.save()
        # print('description:',description)

        MyTree1 = ET.parse(downloads_file)                           #Extract related jobs
        myroot1 = MyTree1.getroot()
        related_job = ''
        for x in myroot1.findall('sample_of_reported_job_titles'):
            for b in x.findall('title'):
                related_job = related_job + (b.text) + ','
        if Related_job_profile.objects.filter(job_profile=titlel[i]).exists():
            Related_job_profile.objects.filter(job_profile=titlel[i]).delete()
        reljob=Related_job_profile(
            job_profile=titlel[i],
            Related_jobs=related_job[:len(related_job) - 1]
        )
        reljob.save()
        
        MyTree2=ET.parse(interests_file)                             #Extract interests
        myroot2=MyTree2.getroot()
        interests=''
        for x in myroot2.findall('element'):
            interests=interests+x.findtext('name')+','
        if Holland_interests.objects.filter(job_profile=titlel[i]).exists():
            Holland_interests.objects.filter(job_profile=titlel[i]).delete()
        intr=Holland_interests(
            job_profile=titlel[i],
            Holland_interest=interests[:len(interests)-1]
        )
        intr.save()

        MyTree3=ET.parse(Tech_skills)                                #Extract Technology skills
        myroot3=MyTree3.getroot()
        skills=''
        for x in myroot3.findall('category'):
            for a in x.findall('example'):
                skills=skills+a.text+','
        if Technical_skill.objects.filter(job_profile=titlel[i]).exists():
            Technical_skill.objects.filter(job_profile=titlel[i]).delete()
        skill=Technical_skill(
            job_profile=titlel[i],
            Technical_skills=skills[:len(skills)-1]
        )
        skill.save()

        MyTree5=ET.parse(knowledge_file)                                #Extract Knowledge
        myroot5=MyTree5.getroot()
        know=''
        for x in myroot5.findall('element'):
            know = know + x.findtext('name') + ','
        if Knowledge.objects.filter(job_profile=titlel[i]).exists():
            Knowledge.objects.filter(job_profile=titlel[i]).delete()
        kn=Knowledge(
            job_profile=titlel[i],
            Knowledge=know[:len(know)-1]
        )
        kn.save()

        MyTree6=ET.parse(skills_file)                                #Extract Skills
        myroot6=MyTree6.getroot()
        skil=''
        for x in myroot6.findall('element'):
            skil = skil + x.findtext('name') + ','
        if Skills.objects.filter(job_profile=titlel[i]).exists():
            Skills.objects.filter(job_profile=titlel[i]).delete()
        sk=Skills(
            job_profile=titlel[i],
            skills=skil[:len(skil)-1]
        )
        sk.save()

        MyTree7=ET.parse(education_file)                                #Extract education
        myroot7=MyTree7.getroot()
        educat = ''
        for x in myroot7.findall('level_required'):
            for l in x.findall('category'):
                educat = educat + l.findtext('name') + ','
        if Education.objects.filter(job_profile=titlel[i]).exists():
            Education.objects.filter(job_profile=titlel[i]).delete()
        ed=Education(
            job_profile=titlel[i],
            education=educat[:len(educat)-1]
        )
        ed.save()

