from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$',views.home,name='gallery_home'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^category/(\d)$', views.get_category, name='get_category'),
    url(r'^location/(\d)$', views.get_by_locations, name='get_by_location'),
    url(r'^image/(\d+)$', views.image_view, name="image_view")
 ]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

