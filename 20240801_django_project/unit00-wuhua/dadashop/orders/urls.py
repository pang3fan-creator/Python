from django.urls import path
from . import views

urlpatterns = [
    path('<slug:username>/advance', views.advance),
    path('<slug:username>',views.OrdersView.as_view()),
    path('result/',views.result),
    path('query/',views.query),
]
