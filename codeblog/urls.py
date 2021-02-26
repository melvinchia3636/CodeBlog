from django.contrib import admin
from django.urls import path, include
from . import settings
from django.conf.urls import url
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ideas/', include('ideas.urls')),
    path('', include('home.urls')),
    path('home/', include('home.urls')),
    path('youtube-comment-scraper/', include('comment_viewer.urls')),
    path('projects/', include('projects_index.urls')),
    path('covid19-stat/', include('covid19stat.urls')),
    path('code-syntax-highlight/', include('code_syntax_highlight.urls')),
    path('flight-tracker/', include('flight_tracker.urls')),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    path('account/', include('signin_register.urls')) 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)