from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='comment-viewer'),
    path('load-comments/', views.load_comments, name='load-comments')
]
