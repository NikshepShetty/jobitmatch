from django.contrib import admin
from courses.models import coursera_db,user_lacking_skills

admin.site.register(coursera_db)
admin.site.register(user_lacking_skills)
