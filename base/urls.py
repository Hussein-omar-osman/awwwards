from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('upload/', views.upload, name='upload'),
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),

    
]