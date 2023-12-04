from django.contrib import admin
from django.urls import path

from search.views import *


urlpatterns = [
    path('',home),
    path('search',search,name="search"),
    path("update/<int:id>",update,name="update_item"),
    path("delete/<int:id>",delete_item,name="delete_item"),
    path("update/<int:id>/",update,name="update_item")
]
