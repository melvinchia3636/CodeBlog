from django.shortcuts import render
from django.template import RequestContext

def home(request):
	return render(request, 'stock_photos_explorer/main.html', {'title': 'Stock Photos Explorer'})

def pixabay_index(request):
	return render(request, 'stock_photos_explorer/pixabay-index.html', {'title': 'Pixabay API Explorer'})