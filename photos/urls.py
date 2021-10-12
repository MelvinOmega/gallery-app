from django.conf.urls import url
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
# from django.conf.urls import include

app_name = 'photos'

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search_results, name='search'),
    path('location/(?P<location>\w+)/', views.image_location, name='location'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)