from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('join-us/', views.join_us, name='join-us'),
    path('login-user/', views.login_user),
    path('logout-user/', views.logout_user),
    
    path('reset-password-request/', views.reset_password, name='reset-password-request/',),
    path('password-reset-email-sent/', views.reset_email_sent),
]
