from django.urls import path

from carts import views

urlpatterns = [
    path('<slug:username>', views.CartsView.as_view()),
]
