from django.shortcuts import render
from django.views.defaults import page_not_found

# Create your views here.
def http_404_handler(request, exception):
	return render(request, "base/404_page.html", {'title': 'Oops! Error 404'}) 