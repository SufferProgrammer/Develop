
from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin

urlpatterns = [
    url(r'', include("website.urls")),
    url(r'^admin/', include(admin.site.urls)),
]
