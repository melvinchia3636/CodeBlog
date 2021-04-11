from django.shortcuts import render, redirect
from django.template import RequestContext
from django.http import HttpResponse

def home(request):
	return render(request, 'stock_photos_explorer/main.html', {'title': 'Stock Photos Explorer'})

def pixabay_index(request):
	if not request.COOKIES.get('api'):
		return redirect('pixabay_ask_api')
	return render(request, 'stock_photos_explorer/pixabay-index.html', {'title': 'Pixabay API Explorer'})

def pixabay_ask_api(request):
	if request.method == 'GET':
		if request.COOKIES.get('api'):
			return redirect('pixabay_index')
		return render(request, 'stock_photos_explorer/pixabay-ask-api.html', {'title': 'Pixabay API Explorer'})
	elif request.method == 'POST':
		return HttpResponse('Okay lol')
	