from django.shortcuts import render
from .models import Project

# Create your views here.
def home(request):
    """ trae los objetos creados en el admin o en la base """
    projects = Project.objects.all()
    return render(request, 'home.html', {'projects' : projects})

