from django.conf.urls import url, include
from django.contrib import admin

api_urls = []

urlpatterns = [
    url(r'^api/', include(api_urls)),
    url(r'^admin/', admin.site.urls),
]
