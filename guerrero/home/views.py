from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse

class Home(generic.TemplateView):
    template_name="home.html"
