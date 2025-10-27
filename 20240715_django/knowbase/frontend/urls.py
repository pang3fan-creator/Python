from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('index/<int:id>/',views.index),
    path('article/<int:id>/',views.article),
    path('register/',views.register),
    path('login/',views.login),
    path('logout/',views.logout),
    path('forget/',views.forget),
    path('comment/<int:id>/',views.comment),
    path('profile/',views.profile),
    path('verify/',views.verify),

]
