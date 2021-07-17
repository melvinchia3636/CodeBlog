from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='projects-index'),
    path('get-details/<int:id>/', views.get_details, name='project-details')
]
