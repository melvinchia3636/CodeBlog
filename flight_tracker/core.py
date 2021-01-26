import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from bs4.element import NavigableString
import os
import json
import time

ua = UserAgent()
headers = {'User-Agent': ua.random}

def get_countries():
	sorted_country = {}
	country = [i.text.strip() for i in BeautifulSoup(requests.get('https://www.flightradar24.com/data/airports', headers=headers).content, 'html.parser').findAll('td') if i.text.strip() and len(i.text.strip()) > 1]; country = [country[i:i+2] for i in range(0, len(country), 2)]
	country = [i+['flight-tracker/flag-icon/{}.svg'.format(i[0].lower())] for i in country]
	for i in country:
		if i[0][0] not in sorted_country:
			sorted_country[i[0][0]] = [i]
		else: 
			sorted_country[i[0][0]] += [i]
	return sorted_country

def get_airports(country):
	sorted_airport_list = {}
	airport_list = [i[0].replace(')', '').split('(') for i in sum([i for i in [[[k.text.strip() for k in j.contents if str(k).strip() and type(k) != NavigableString] for j in i.findAll('td') if j.text.strip()] for i in BeautifulSoup(requests.get('https://www.flightradar24.com/data/airports/{}'.format(country), headers=headers).content, 'html.parser').find('tbody').findAll('tr')] if i], []) if i]
	for i in range(len(airport_list)): airport_list[i][1] = airport_list[i][1].split('/')
	count = len(airport_list)
	for i in airport_list:
		if i[0][0] not in sorted_airport_list:
			sorted_airport_list[i[0][0]] = [i]
		else: 
			sorted_airport_list[i[0][0]] += [i]
	return sorted_airport_list, count

def get_airport_data(iata):
	headers = {'User-Agent': ua.chrome}
	raw = requests.get('https://api.flightradar24.com/common/v1/airport.json?code='+iata, headers=headers).json()['result']['response']['airport']['pluginData']
	schedule_data = raw['schedule'] 
	arrival_data = [
    	[
        	time.strftime('%I:%M %p', time.localtime(i['time']['scheduled']['arrival'])),
			i["identification"]['number']['default'],
			{
				'name': i['airport']['origin']['position']['region']['city'],
				'iata': i['airport']['origin']['code']['iata'] 
			},
			i['airline']['short'] if i['airline'] else None,
			i['aircraft']['model']['code'] if i['aircraft'] else None,
			{
				'text': i['status']['text'],
				'status': i['status']['generic']['status']['color']
			}
		]
    	for i in [i['flight'] for i in schedule_data['arrivals']['data']]
	]
	departure_data = [
    	[
        	time.strftime('%I:%M %p', time.localtime(i['time']['scheduled']['departure'])),
			i["identification"]['number']['default'],
			{
				'name': i['airport']['destination']['position']['region']['city'],
				'iata': i['airport']['destination']['code']['iata'] 
			},
			i['airline']['short'] if i['airline'] else None,
			i['aircraft']['model']['code'] if i['aircraft'] else None,
			{
				'text': i['status']['text'],
				'status': i['status']['generic']['status']['color']
			}
		]
    	for i in [i['flight'] for i in schedule_data['departures']['data']]
	]
	result = {
		'name': raw['details']['name'],
		'code': {
			'icao': raw['details']['code']['icao'],
			'iata': raw['details']['code']['iata']
		},
		'position': {
			'longitude': raw['details']['position']['longitude'],
			'latitude': raw['details']['position']['latitude']
		},
		'country': {
			'name': raw['details']['position']['country']['name'],
			'code': raw['details']['position']['country']['code']
		},
		'timezone': {
			'abbr': raw['details']['timezone']['abbr'],
			'region': raw['details']['timezone']['name']
		},
		'temperature': {
			'celsius': raw['weather']['temp']['celsius'] if raw['weather'] else 'N/A',
			'condition': raw['weather']['sky']['condition']['text'] if raw['weather'] else 'N/A'
		},
		'wind': {
			'direction': raw['weather']['wind']['direction']['degree'] if raw['weather'] and raw['weather']['wind']['direction']['degree'] else 'N/A',
			'speed': raw['weather']['wind']['speed']['kmh'] if raw['weather'] and raw['weather']['wind']['speed']['kmh'] else 'N/A'
		},
		'images': [
			'https://cdn.jetphotos.com/full/{}/{}'.format(*i['src'].split('/')[-2:]) for i in raw['details']['airportImages']['large']
		] if raw['details']['airportImages'] else [],
		'arrivals': arrival_data,
		'departures': departure_data,
		'arrivals_page_limit': schedule_data['arrivals']['page'],
		'departures_page_limit': schedule_data['departures']['page']
	}
	return result
    
def next_page(iata, page, AorD):
	headers = {'User-Agent': ua.chrome}
	orgiOrDest = {'arrivals': 'origin', 'departures': 'destination'}
	raw = requests.get('https://api.flightradar24.com/common/v1/airport.json?page={}&code={}'.format(page, iata), headers=headers).json()['result']['response']['airport']['pluginData']
	schedule_data = raw['schedule'] 
	data = [
    	[
        	time.strftime('%I:%M %p', time.localtime(i['time']['scheduled'][AorD[:-1]])),
			i["identification"]['number']['default'],
			{
				'name': i['airport'][orgiOrDest[AorD]]['position']['region']['city'],
				'iata': i['airport'][orgiOrDest[AorD]]['code']['iata']
			},
			i['airline']['short'] if i['airline'] else None,
			i['aircraft']['model']['code'] if i['aircraft'] else None,
			{
				'text': i['status']['text'],
				'status': i['status']['generic']['status']['color']
			}
		]
    	for i in [i['flight'] for i in schedule_data[AorD]['data']]
	]
	return data