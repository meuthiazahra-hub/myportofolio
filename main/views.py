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
def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    projects_json = serializers.serialize("json", projects)
    return HttpResponse(projects_json, content_type="application/json")

def show_projects(request):
    json_response = get_projects_json(request)

    projects = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    projects = [project.object for project in projects]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Meuthia",
        "project_list": projects,
        "title_query": title_query,
    }
    return render(request, "projects.html", context)

def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project berhasil dihapus!")
        return redirect("main:show_projects")

    return redirect("main:show_projects")