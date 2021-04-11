from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='stock_photos_explorer_index'),
    path('pixabay/', views.pixabay_index, name='pixabay_index'),
    path('pixabay/api-key', views.pixabay_ask_api, name='pixabay_ask_api')
]
