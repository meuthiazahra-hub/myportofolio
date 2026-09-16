from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from main.forms import ProjectForm
from main.models import Experience,  Project


def show_main(request):
    context = {
        "name": "Meuthia",
        "npm": "2506637060",
        "study_program": "S1 Ilmu Komputer KKI",
        "bio": (
            "Hi, I'm Meuthia — a CS student who loves learning by building and excited to turn small ideas into things people can actually use."
            
        ),
        "job_title": "Computer Science Student"
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Meuthia",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def show_projects(request):
    projects = Project.objects.all()
    context = {
        'name': 'Meuthia',
        'projects': projects,
    }
    return render(request, 'projects_form.html', context)

def show_projects_page(request):
    projects = Project.objects.all()
    context = {
        'name': 'Meuthia',
        'projects': projects,
    }
    return render(request, 'projects_page.html', context)
def create_project(request):
    form = ProjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Proyek baru berhasil ditambahkan!")
        return redirect("main:show_projects")

    context = {
        "name": "Meuthia",
        "form": form,
    }
    return render(request, "projects_form.html", context)