from django.urls import path

from main.views import show_main, show_experience, show_projects, show_projects_page 

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path('projects/', show_projects, name='show_projects'),
    path('projects-page/', show_projects_page, name='show_projects_page'),
]