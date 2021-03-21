from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def home(request):
	posts = reversed(Post.objects.all())
	return render(request, 'ideas/main.html', {'posts': posts, 'title': 'Ideas'})