from django.urls import path

from . import views

urlpatterns = [
    path('basic/', views.basic),
    path('parameters/', views.parameters),
    path('headers/', views.headers),
    path('body/', views.body),
    path('register/', views.register),
]
