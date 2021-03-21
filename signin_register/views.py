from django.shortcuts import render

def login(request):
	return render(request, 'login/index.html', {'title': 'Sign In'})

def join(request):
	return render(request, 'login/index.html', {'title': 'Sign Up'})