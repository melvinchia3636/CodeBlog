from django.urls import path
from . import views

urlpatterns = [
    path('fetch/', views.fetch, name='projects-fetch'),
    path('fetch-count/', views.fetch_count, name='projects-fetch-count')
]