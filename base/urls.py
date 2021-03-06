from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/<us>/', views.profile, name='profile'),
    path('upload/', views.upload, name='upload'),
    path('post/<pk>/', views.post, name='post'),
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('logout/', views.logoutUser, name='logout'),
    path('searchResults/', views.searchResults, name='searchResults'),
    path('accountSettings/', views.accountSettings, name='accountSettings'),

    
]