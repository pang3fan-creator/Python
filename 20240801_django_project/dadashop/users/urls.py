from django.urls import path, include
from . import views

urlpatterns = [
    path('register', views.register),
    path('login', views.login),
    path('password/sms', views.sms),
    path('password/verification', views.verification),
    path('password/new', views.new),
    path('<slug:username>/password', views.password),
    path('activation', views.activation),
    path('sms/code', views.sms_code),
    path('<slug:username>/address/<int:id>', views.AddressView.as_view()),
    path('<slug:username>/address', views.AddressView.as_view()),
    path('<slug:username>/address/default', views.default),

    # "GET /v1/users/weibo/authorization HTTP/1.1" 404 4221
    path('weibo/authorization', views.weibo),
    path('weibo/users', views.WeiBoUsers.as_view()),
    path('weibo/users/binduser', views.bind_user),
]
