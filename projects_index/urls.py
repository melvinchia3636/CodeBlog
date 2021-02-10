from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='projects-index'),
    path('api/projects-list.json', views.projectsListAPI, name='project-index-api')
]
