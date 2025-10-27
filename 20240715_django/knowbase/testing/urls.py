from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('detail/<int:id>',views.detail),
    path('field/',views.field),
    path('filter/',views.filter),
    path('order/',views.order),
    path('aggregate/',views.aggregate),
    path('onetoone/',views.onetoone),
    path('onetomany/', views.onetomany),
    path('manytomany/', views.manytomany),
    path('related/', views.related),
]
