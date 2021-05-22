from django.contrib.staticfiles.storage import staticfiles_storage
from django.http import HttpResponse
from django.shortcuts import render
import json

def home(request):
	return render(request, 'projects-index/main.html', {'data': projectsListAPI(None), 'title': 'Projects', 'theme': 'light'})

def projectsListAPI(request):
	if not request: return json.load(open(staticfiles_storage.path('projects-index/projects-list.json'),'r'))
	data_amount = request.GET.get('amount')
	data = json.load(open(staticfiles_storage.path('projects-index/projects-list.json'),'r'))
	if data_amount: data['items'] = data['items'][0:int(data_amount)]
	return HttpResponse(json.dumps(data))