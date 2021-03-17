from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='Home'),
    path('about/', views.about_view, name='About'),
    path('profiles/', views.job_profile_view, name='Job Profile'),

]