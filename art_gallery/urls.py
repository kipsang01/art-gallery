from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$',views.home,name='gallery_home'),
   # url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_news,name = 'pastNews'), 
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^category/(\d)$', views.get_category, name='get_category'),
#     url(r'^category/(\d)$', views.test, name='test')
 ]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

