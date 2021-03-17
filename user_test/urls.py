from django.urls import path
from . import views


urlpatterns = [
    path('', views.test_start_view, name='Test Start'),
    path('skills/',views.manual_input_view, name='Skills'),
    path('interests/',views.interest_view, name='Interests'),
    path('result/',views.result_view, name='result'),
    path('onet_xml/', views.onet_ref_view, name='onet_refresh'),
]
