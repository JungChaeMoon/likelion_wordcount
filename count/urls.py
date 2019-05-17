from django.contrib import admin
from django.urls import path
from . import views
from count.models import Star


app_name = 'count'

urlpatterns=[
    path('count/', views.view, name='index'),
    path('count/about', views.about, name='about'),
    path('count/detail', views.detail, name='detail'),
    path('count/see/', views.see, name='see'),
    path('count/vote/', views.vote, name='vote'),
    path('count/result/', views.results, name='result'),
]