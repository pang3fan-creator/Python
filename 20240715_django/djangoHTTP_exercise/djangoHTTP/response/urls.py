from django.urls import path

from . import views

urlpatterns = [
    path('responseHTML/', views.responseHTML),
    path('responseText/', views.responseText),
    path('responseCSS/', views.responseCSS),
    path('responseJS/', views.responseJS),
    path('responseJSON/', views.responseJSON),
    path('responseJSON1/', views.responseJSON1),
    path('redirectToBaidu/', views.redirectToBaidu),
    path('redirectToSina/', views.redirectToSina),
    path('headers/', views.headers),
    path('badRequest/', views.badRequest),
    path('notFound/', views.notFound),
    path('serverError/', views.serverError),
]
