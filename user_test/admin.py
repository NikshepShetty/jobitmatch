from django.contrib import admin
from .models import resume,manual_input,holland,holland_score, technical_list,Holland_interests, Job_description,Technical_skill,Related_job_profile, User_Filtered_Job,Final_Results, Knowledge, Skills, Education

admin.site.register(resume)
admin.site.register(manual_input)
admin.site.register(holland)
admin.site.register(holland_score)
admin.site.register(technical_list)
admin.site.register(Holland_interests)
admin.site.register(Job_description)
admin.site.register(Technical_skill)
admin.site.register(Related_job_profile)
admin.site.register(User_Filtered_Job)
admin.site.register(Final_Results)
admin.site.register(Skills)
admin.site.register(Knowledge)
admin.site.register(Education)