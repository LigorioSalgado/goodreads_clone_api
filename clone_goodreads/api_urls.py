from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
url(r'^authors/', include("modules.Authors.urls")),
url(r'^books/', include("modules.Books.urls")),
url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]