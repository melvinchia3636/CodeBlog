from django import http
from django.shortcuts import render
from django.http import HttpResponse
from .core import *
import re, json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(response):
	return render(response, 'flight-tracker/main.html', {'countries': get_countries()})
	
def airportlist(response, country=None):
	country_search = re.sub(r',|\(|\)|\'|-', '', country).replace(' ', '-').lower()
	airport_list, count = get_airports(country_search)
	return render(response, 'flight-tracker/airport-list.html', {'airport_list': airport_list, 'airport_count': count, 'country': country})

def airport(response, iata=None):
	result = get_airport_data(iata.lower())
	return render(response, 'flight-tracker/airport.html', result)

@csrf_exempt
def get_next(response):
    data = next_page(response.POST['iata'], response.POST['page'], response.POST['AorD'])
    return HttpResponse(json.dumps(data))

@csrf_exempt
def review(response, iata):
	data = get_review(iata, response.POST['page'] if 'page' in response.POST else 1)
	return HttpResponse(json.dumps(data))