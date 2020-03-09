from django.contrib import admin
from django.urls import include, path
from home.views import Home
from django.contrib.auth import views as auth_views

urlpatterns= [
    path('',Home.as_view(),name='home'),
]
