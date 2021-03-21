from django.shortcuts import render

def home(response):
	return render(response, 'parcel-tracker/main.html', {'title': 'Universal Parcel Tracker'})