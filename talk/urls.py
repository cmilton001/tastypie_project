from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from talk import views

urlpatterns = [

    path('insert/', views.Insert.as_view(), name='insert'),
    path('get_talks/', views.GetTalks.as_view(), name='get_talks'),
]
