from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
    path('Home/', views.homepage),
    path('profile/', views.profile),
    path('settings/', views.settings),
    path('', views.welcomepage)
]
