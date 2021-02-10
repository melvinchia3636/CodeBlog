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
		try: result = C(url, A(url))
		except Exception as e: raise;result = None
		return HttpResponse(json.dumps(result))
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