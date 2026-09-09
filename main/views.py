from django.shortcuts import render

from main.models import Experience


def show_main(request):
    context = {
        "name": "Meuthia",
        "npm": "2506637060",
        "study_program": "S1 Ilmu Komputer KKI",
        "bio": (
            "Hi, I'm Meuthia — a CS student who loves learning by building and excited to turn small ideas into things people can actually use."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Meuthia",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)