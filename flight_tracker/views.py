from django.shortcuts import render
from django.http import HttpResponse
from .core import get_countries, get_airports, get_airport_data
import re

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