from django.shortcuts import render, get_object_or_404
from .models import Project, Tag

# Create your views here.

def home(request):
    project = Project.objects.all()
    tags = Tag.objects.all()

    return render(request, "home.html", {"projects" : project, "tags" : tags})

def contact(request):
    return render(request, "contact.html")

def project(request, id):
    project = get_object_or_404(Project, pk = id)

    return render(request, "project.html", {"project" : project})