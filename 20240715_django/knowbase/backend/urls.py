from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('login/', views.login),
    path('check/', views.check),
    path('logout/',views.logout),

    ##################################################
    path('author/', views.author),
    path('author/create/', views.create_author),
    path('author/post/', views.post_author),
    path('author/get/<int:id>/', views.get_author),
    path('author/put/<int:id>/', views.put_author),
    path('author/delete/<int:id>/', views.delete_author),
    ##################################################
    path('category/', views.category),
    path('category/create/', views.create_category),
    path('category/post/', views.post_category),
    path('category/get/<int:id>/', views.get_category),
    path('category/put/<int:id>/', views.put_category),
    path('category/delete/<int:id>/', views.delete_category),
    ##################################################
    path('article/', views.article),
    path('article/create/', views.create_article),
    path('article/post/', views.post_article),
    path('article/get/<int:id>/', views.get_article),
    path('article/put/<int:id>/', views.put_article),
    path('article/delete/<int:id>/', views.delete_article),
    path('article/recycle/',views.recycle_article),
    path('article/restore/<int:id>/',views.restore_article),
    path('article/remove/<int:id>/',views.remove_article),
]
