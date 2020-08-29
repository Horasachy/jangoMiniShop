from django.urls import path, include
from django.contrib.auth import views as AuthView
from . import views

urlpatterns = [
    path('login', views.login_view, name='login'),
    path('register', views.register_view, name='register'),
    path('logout/', AuthView.LogoutView.as_view(), name='logout'),
]

