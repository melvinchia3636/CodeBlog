from django.http import HttpResponse
from .models import *
import json
import datetime

class DateTimeEncoder(json.JSONEncoder):
    def default(self, z):
        if isinstance(z, datetime.datetime):
            return (str(z))
        else:
            return super().default(z)

def fetch(request):
    if not request.GET.get("cat"):
        return HttpResponse(json.dumps([[16+i, f"{e.category.short_name}-{e.proj_id}", e.name, e.category.name, e.color, e.image.url] for i, e in enumerate(Project.objects.all()[:(None if request.GET.get("item") == "all" else 5)])]), content_type='application/json')
    else:
        return HttpResponse(json.dumps([[16+i, f"{e.category.short_name}-{e.proj_id}", e.name, e.category.name, e.color, e.image.url] for i, e in enumerate(Project.objects.filter(category__short_name=request.GET.get("cat"))[:(None if request.GET.get("item") == "all" else 5)])]), content_type='application/json')