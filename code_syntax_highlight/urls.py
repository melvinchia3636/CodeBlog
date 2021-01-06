from django.urls import path
from . import views

app_name = 'code-syntax-highlight'

urlpatterns = [
    path('', views.home, name='code-syntax-highlight'),
    path('get-preview/<str:theme>', views.get_preview, name='get-preview'),
    path('/get-formatted-code', views.get_formatted_code, name='get-formatted-code')
]
