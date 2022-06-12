from rest_framework.serializers import ModelSerializer
from base.models import Post, User



class PostSerializer(ModelSerializer):
  class Meta:
    model = Post
    fields = '__all__'

   
class UserSerializer(ModelSerializer):
  class Meta:
    model = User
    fields = ['id', 'last_login', 'username', 'first_name', 'last_name', 'is_active', 'date_joined', 'email', 'bio', 'image', 'contact']
  