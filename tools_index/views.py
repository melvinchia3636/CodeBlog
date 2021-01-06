from django.shortcuts import render

def home(request):
	return render(request, 'browse-tools/main.html')