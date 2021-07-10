from django.contrib.staticfiles.storage import staticfiles_storage
from django.http import HttpResponse
from django.shortcuts import render
from .models import *
import json

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