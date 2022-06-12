from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_links),
    path('posts/', views.get_posts),
    path('users/', views.get_users),
    path('post/<pk>', views.single_post),
    path('user/<pk>', views.single_user),
    
]