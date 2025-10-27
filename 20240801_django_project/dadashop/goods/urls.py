from django.urls import path

from goods import views

urlpatterns = [
    path('index', views.j),
    path('catalogs/<int:id>', views.catalogs),
    path('detail/<int:id>', views.detail),
    path('sku', views.sku),
    path('1', views.mysql),
]
