from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('personalInfo/', views.personalInfo, name='personal-info'),
  path('resumePage/', views.resumePage, name='resume-page'),
]
