from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from prometheus_client import generate_latest
from django.http import HttpResponse

def metrics_view(request):
    metrics_data = generate_latest()
    return HttpResponse(metrics_data, content_type="text/plain")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')), 
    path('metrics/', metrics_view, name='metrics'),
]


if settings.DEBUG: 
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)), 
    ] + urlpatterns


