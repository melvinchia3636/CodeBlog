from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from .forms import UrlInputForm
from .core import A, C
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def home(request):
	if request.method == 'POST':
		form = UrlInputForm(request.POST)
		try: result = C(form.data['video_url'], A(form.data['video_url']))
		except: result = None
	else:
		form = UrlInputForm()
		result = None
	return render(request, 'comment-viewer/main.html', {'form': form, 'result': result})

@csrf_exempt
def load_comments(request):
	if request.POST:
		continuation = request.POST['continuation_token']
		url = request.POST['url']
		return HttpResponse(str(C(url, continuation)))
	else:
		return HttpResponseBadRequest('Error 400', status=400)