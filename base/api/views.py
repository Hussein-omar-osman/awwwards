from django.db import router
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from base.models import Post, User
# from django.contrib.auth.models import User
from .serializers import UserSerializer, PostSerializer


@api_view(['GET'])
def get_links(request):
   endpoints = {
    'all':'/api/',
    'all_todos':'/api/todos'
   }
   return Response(endpoints)
  
@api_view(['GET'])
def get_posts(request):
   posts = Post.objects.all()
   serializer = PostSerializer(posts, many=True)
   return Response(serializer.data)
  
   
@api_view(['GET'])
def single_post(request, pk):
   try:
     post = Post.objects.get(id=pk)
   except:
      return Response({'error':'not found'}, status=status.HTTP_404_NOT_FOUND)
   if request.method == 'GET':
     serializer = PostSerializer(post)
     return Response(serializer.data)
  
  
@api_view(['GET'])
def single_user(request, pk):
   try:
     user = User.objects.get(id=pk)
   except:
      return Response({'error':'not found'}, status=status.HTTP_404_NOT_FOUND)
   if request.method == 'GET':
     serializer = UserSerializer(user)
     return Response(serializer.data)
  
  
@api_view(['GET'])
def get_users(request):
   users = User.objects.all()
   serializer = UserSerializer(users, many=True)
   return Response(serializer.data)
   
   