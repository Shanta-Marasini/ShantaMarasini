from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Project

# Create your views here.

class Project( ListView ):

    model = Project
    context_object_name = 'projects'
    template_name = 'github/github.html'