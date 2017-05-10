from django.conf.urls import url
from django.contrib import admin
from .views import ListBook,DetailBook

urlpatterns = [
    url(r'^$', ListBook.as_view(), name="list-books" ),
     url(r'^(?P<pk>[0-9]+)/$', DetailBook.as_view(), name="detail-books"),
]