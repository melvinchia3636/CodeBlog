from django.shortcuts import render
from django.apps import apps

def home(request):
	models = apps.get_model('ideas', 'Post')
	return render(request, 'home/homepage.html', {'articles': models.objects.order_by('-id')[:5]})