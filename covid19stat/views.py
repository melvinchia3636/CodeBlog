from django.shortcuts import render
from django.http import HttpResponse
from .table import get_table, get_graph_data

# Create your views here.
def home(response):
	return render(response, 'covid19-stat/main.html', {'table': get_table(), 'graph': get_graph_data()})