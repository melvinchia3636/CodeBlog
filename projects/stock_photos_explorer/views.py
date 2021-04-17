from django.shortcuts import render, redirect
from django.template import RequestContext
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup as bs
import cloudscraper

def home(request):
	return render(request, 'stock_photos_explorer/main.html', {'title': 'Stock Photos Explorer'})

def pixabay_index(request):
	if not request.COOKIES.get('api'):
		return redirect('pixabay_ask_api')
	if request.method == 'GET':
		query = request.GET.get('q')
		if query: return render(request, 'stock_photos_explorer/pixabay-query.html', {'title': 'Search Result for {} - Pixabay API Explorer'.format(query).title()})
		image = bs(cloudscraper.create_scraper().get('https://pixabay.com').content, 'lxml').find('picture').find('source')['srcset']
		return render(request, 'stock_photos_explorer/pixabay-index.html', {'title': 'Pixabay API Explorer', 'image': image})

def pixabay_ask_api(request):
	if request.method == 'GET':
		if request.COOKIES.get('api'):
			return redirect('pixabay_index')
		return render(request, 'stock_photos_explorer/pixabay-ask-api.html', {'title': 'Pixabay API Explorer'})
	elif request.method == 'POST':
		return HttpResponse('Okay lol')
	