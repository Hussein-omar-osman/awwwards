from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField
import uuid


# Create your models here.
class User(AbstractUser):
   email = models.EmailField(unique=True)
   bio = models.TextField(null=True)
   image = CloudinaryField('image', null=True, blank=True, default='image/upload/v1654285390/hz7a08c74kynhnx24lwd.png')
   contact = models.CharField(max_length=100 ,blank=True, null=True)
   USERNAME_FIELD = 'email'
   REQUIRED_FIELDS = ['username']
   
   
class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=500)
    url = models.CharField(max_length=500)
    image = CloudinaryField('image')
    feedback = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    comments = models.IntegerField(default=0)
    

    class Meta:
      ordering = ['-created']
    def __str__(self):
        return self.title
     
     
class Ratings(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   post = models.ForeignKey(Post, on_delete=models.CASCADE)
   stars = models.IntegerField()
   body = models.TextField()
   created = models.DateTimeField(auto_now_add=True)  
   
   class Meta:
      ordering = ['-created']
      
   def __str__(self):
         return self.body[0:50]