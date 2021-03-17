from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_ref_view, name='course_refresh'),
]
