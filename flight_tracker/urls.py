from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.home, name='flight-tracker'),
    path('country/<str:country>', views.airportlist, name='country'),
    path('airport/<str:iata>', views.airport, name='airport'),
    path('next-page', views.get_next, name='next_page'),
    path('airport/<str:iata>/review', views.review, name='review')
]