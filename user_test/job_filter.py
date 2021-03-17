from .models import holland_score,User_Filtered_Job,Holland_interests
from .resume_matchers import similarity
def holland_filter(userid):
    realistic_score=holland_score.objects.get(user=userid).realistic
    investigative_score=holland_score.objects.get(user=userid).investigative
    enterprising_score=holland_score.objects.get(user=userid).enterprising
    artistic_score=holland_score.objects.get(user=userid).artistic
    social_score=holland_score.objects.get(user=userid).social
    conventional_score=holland_score.objects.get(user=userid).conventional

    m_value=0
    m_list=[]
    m_list.append(realistic_score)
    m_list.append(investigative_score)
    m_list.append(enterprising_score)
    m_list.append(artistic_score)
    m_list.append(social_score)
    m_list.append(conventional_score)

    m_value=max(m_list)
    filtered_list=[]
    interest_user=''
    if m_value==realistic_score:
        interest_user='Realistic'
    elif m_value==investigative_score:
        interest_user='Investigative'
    elif m_value==enterprising_score:
        interest_user='Enterprising'
    elif m_value==artistic_score:
        interest_user='Artistic'
    elif m_value==social_score:
        interest_user='Social'
    else:
        interest_user='Conventional'
    
    intr_sep=''
    objects=Holland_interests.objects.all()
    for x in objects:
        intr_sep=x.Holland_interest
        if interest_user in intr_sep.split(","):
            filtered_list.append(x.job_profile)
    jobs=""
    jobs=",".join(filtered_list)
    if User_Filtered_Job.objects.filter(user=userid).exists():
        User_Filtered_Job.objects.filter(user=userid).delete()
    user_job_list=User_Filtered_Job(
        user=userid,
        filtered_list=jobs
    )
    user_job_list.save()
    similarity(userid, filtered_list)