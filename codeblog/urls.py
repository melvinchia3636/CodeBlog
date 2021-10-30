from django.contrib import admin
from django.urls import path, include
from . import settings
from django.conf.urls import url
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404, handler500
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', admin.site.urls),
    path('projects/', include('projects_index.urls')),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('base/img/favicon.ico'))),
    
    path('youtube-comment-scraper/', include('comment_viewer.urls')),
    path('flight-tracker/', include('flight_tracker.urls')),
    path('covid19-stat/', include('covid19stat.urls')),
    path('code-syntax-highlight/', include('code_syntax_highlight.urls')),
    path('parcel-tracker/', include('parcel_tracker.urls')),
    path('stock-photos/', include('stock_photos_explorer.urls')),
    path('book-catalogue/', include('book_catalogue.urls')),
]

handler404 = 'base.views.http_404_handler'
#handler500 = 'base.views.http_404_handler'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)