from django.shortcuts import render

def home(request):
	return render(request, 'book-catalogue/index.html', {'title': 'Book Catalogue'})