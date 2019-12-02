from django.urls import path
from django.conf.urls import url, include
from . import views

app_name='sightings'

urlpatterns=[
    path('',views.index, name="index"),
    path('add/',views.add, name="add"),
    
]
