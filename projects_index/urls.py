from django.urls import path
from . import views

urlpatterns = [
    path('fetch/', views.fetch, name='projects-fetch')
]