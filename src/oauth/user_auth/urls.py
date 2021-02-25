from django.urls import path

from . import views

app_name = 'user_auth'

urlpatterns = [
    path('', views.LoginView.as_view(), name='login'),
    path('login', views.LoginView.as_view(), name='login'),
    path('signup', views.SignupView.as_view(), name='signup'),
    path('logout', views.logout, name='logout'),
]
