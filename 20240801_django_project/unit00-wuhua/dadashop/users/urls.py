from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register),
    path('login', views.login),
    path('password/sms', views.password_sms),
    path('password/verification', views.password_verification),
    path('password/new', views.password_new),
    path('<slug:username>/password', views.change_password),
    path('activation', views.activation),
    path('sms/code', views.sms_code),
    path('<slug:username>/address', views.AddressView.as_view()),
    path('<slug:username>/address/<int:id>', views.AddressView.as_view()),
    path('<slug:username>/address/default',views.address_default),
    path('weibo/authorization',views.weibo_authorization),
    path('weibo/users',views.WeiBoUserView.as_view()),
    path('weibo/users/binduser',views.bind_user),
]
