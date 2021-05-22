from django.shortcuts import render
from django.http import HttpResponse
from .table import get_table, get_graph_data
import json

# Create your views here.
def home(request):
	if request.method == 'POST' and request.is_ajax():	
		return HttpResponse(json.dumps({'table': get_table(), 'graph': get_graph_data()}))
	return render(request, 'covid19-stat/main.html', {'title': 'Covid 19 Statistic', 'theme': 'light'})
	