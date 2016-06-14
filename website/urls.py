from django.conf.urls import url
from website import  views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
	url(r'^$', views.index, name='index'),
]

urlpatterns += staticfiles_urlpatterns()
