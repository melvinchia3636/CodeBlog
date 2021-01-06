import requests
from bs4 import BeautifulSoup
import json

def get_table():
	soup = BeautifulSoup(requests.get('https://www.worldometers.info/coronavirus/').content, 'lxml')
	counter = [i.find('span').text.strip() for i in soup.findAll('div', {'id':'maincounter-wrap'})]
	print(counter)
	title = [i.text.strip() for i in soup.find('div', {'id': 'nav-today'}).findAll('th')][1:]
	table = [[j if j else None for j in i][1:] for i in [[j.text.strip() for j in i.findAll('td')] for i in soup.find('div', {'id': 'nav-today'}).findAll('tr')[1:]]][7:-8]
	table = [[i]+table[i] for i in range(len(table))]
	return counter, table

def get_snippet(string, target, delimiter, skip=0):
	start = string.find(target)+len(target)+skip
	end = string.find(delimiter, start)
	return string[start:end]

def get_graph_data():
	soup = BeautifulSoup(requests.get('https://www.worldometers.info/coronavirus/worldwide-graphs/').content, 'lxml')
	raw = str(soup.findAll('script')).replace('\n', '')
	cases = [int(i) if i!='null' else 0 for i in get_snippet(get_snippet(get_snippet(raw, '\'Daily Cases', ';'), '7-day moving average', ';'), 'data: ', ']', skip=1).split(',')]
	recovered = [int(i) if i!='null' else 0 for i in get_snippet(get_snippet(raw, '\'New Recoveries', ';'), 'data: ', ']', skip=1).split(',')]
	death = [int(i) if i!='null' else 0 for i in get_snippet(get_snippet(get_snippet(raw, "name: 'Daily Deaths'", ';'), '7-day moving average', ';'), 'data: ', ']', skip=1).split(',')]
	
	return cases, recovered, death