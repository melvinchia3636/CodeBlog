from django.contrib.staticfiles.storage import staticfiles_storage
from django.http import HttpResponse
from django.shortcuts import render
from .models import *
import json
import requests
from requests.auth import HTTPDigestAuth
from bs4 import BeautifulSoup

def home(request):
	cat = request.GET.get("cat")
	try: cat = json.loads(cat)
	except: cat = None
	categories = [i.id for i in (Category.objects.filter(id__in=cat).all() if cat else Category.objects.all())]

	lang = request.GET.get("lang")
	try: lang = json.loads(lang)
	except: lang = None
	languages = [i.id for i in (Language.objects.filter(id__in=lang).all() if lang else Language.objects.all())]

	result = Project.objects.filter(category__id__in=categories, language__id__in=languages).all().order_by('-star')
	return render(request, 'projects-index/main.html', {
		'data': result, 
		'categories': Category.objects.all(), 
		'selectedCat': cat, 
		'languageUsed': Language.objects.all(),
		'selectedLang': lang, 
		'title': 'Projects'})

def get_details(request, id):
	project = Project.objects.get(id=id)
	if project:
		url_suffix = project.repo.replace('https://github.com/', '')
		loc = BeautifulSoup(requests.get('https://img.shields.io/tokei/lines/github/'+url_suffix).content, 'lxml').select_one('text:last-child').text
		size = BeautifulSoup(requests.get('https://img.shields.io/github/repo-size/'+url_suffix).content, 'lxml').select_one('text:last-child').text
		return HttpResponse(json.dumps({
			"name": project.name,
			"desc": project.desc,
			"created_at": project.created_at.strftime('%a, %d %b %Y %I:%M %p').replace('AM', 'a.m.').replace('PM', 'p.m.'),
			"loc": loc,
			"cat": project.category.name,
			"license": project.license,
			"size": size,
		}), content_type='application/json')
	return HttpResponse(json.dumps({}))