from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from .forms import UrlInputForm
from .core import A, C
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def home(request):
	if request.method == 'POST':
		url = request.POST.get('video_url')
		continuation = A(url)
		try: result = C(url, *continuation)
		except Exception as e: raise;result = None
		return HttpResponse(json.dumps(result))
	else:
		form = UrlInputForm()
		result = None
	return render(request, 'comment-viewer/main.html', {'form': form, 'result': result, 'title': 'Youtube Comments Scraper'})

@csrf_exempt
def load_comments(request):
	if request.POST:
		continuation = request.POST.getlist('continuation_token[]')
		print(continuation)
		url = request.POST['url']
		return HttpResponse(json.dumps(C(url, *continuation)))
	else:
		return HttpResponseBadRequest('Error 400', status=400)