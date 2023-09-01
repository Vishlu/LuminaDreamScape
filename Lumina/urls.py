from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Chart1, name='C1-btn'),
    path('RegionLikelihood/', views.Chart2, name='C2-btn'),
    path('TopicRelavance/', views.Chart3, name='C3-btn'),
    path('YearLikelihood/', views.Chart4, name='C4-btn'),
    path('Data/', views.TableData, name='C5-btn'),
]
