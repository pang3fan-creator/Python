from django.urls import path

from orders import views

urlpatterns = [
    path('<slug:username>/advance', views.advance),
    path('result/', views.result),
    path('<slug:username>', views.OrdersView.as_view()),
]
