from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='parcel_tracker_index')
]
