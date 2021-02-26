from django.shortcuts import render

def login(request):
	return render(request, 'login/index.html')

def join(request):
	return render(request, 'login/index.html')