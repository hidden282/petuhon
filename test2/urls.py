from django.contrib import admin
from django.urls import path

from test2.views import test1, page

urlpatterns = [
    path("", page),
    path("test1", test1),
]
