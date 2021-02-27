from django.urls import path

from . import views

app_name = 'google_auth'

urlpatterns = [
    path('oauth-callback', views.callback, name='callback'),
    path('exchange', views.exchange, name='exchange'),
    path('user_info', views.user_info, name='user_info'),
]
