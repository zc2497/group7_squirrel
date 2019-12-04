from django.urls import path
from django.conf.urls import url, include
from . import views

app_name='sightings'

urlpatterns=[
    path('',views.index, name="index"),
    path('add/',views.add, name="add"),
    path('<unique_squirrel_id>/', views.details, name="details"),
    path('<unique_squirrel_id>/update/', views.update, name="update"),
    path('<unique_squirrel_id>/delete/', views.delete, name="delete"),
]
