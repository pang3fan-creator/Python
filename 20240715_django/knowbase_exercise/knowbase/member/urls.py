from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('lists/', views.lists),

    # 为基于函数的视图 -- FBV
    # path('manage/',views.manage),
    # path('delete/<int:id>/',views.delete),
    # path('get/<int:id>/',views.get),
    # path('put/<int:id>/',views.put),


    # 为基于类的视图 -- CBV
    path('admin/<int:id>/',views.MemberView.as_view()),
    path('admin/',views.MemberView.as_view()),

]
