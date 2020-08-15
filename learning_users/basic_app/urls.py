""" Urls for basic_app """

from django.urls import path
from basic_app import views

# TEMPLATE URLS
app_name = 'basic_app'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('hoes', views.hoes, name='charlie'),
    path('user_login/', views.user_login, name='user_login'),
]
