from django.test import TestCase
from base.models import User, Post, Ratings


class TestModel(TestCase):
   def test_create_user(self):
    user = User.objects.create_user(username='banana', email='banana@gmail.com', password1='password', password2='password')
    user.save()
    
    self.assertEqual(str(user), 'banana')
    
   def test_create_post(self):
    user = User.objects.create_user(username='banana', email='banana@gmail.com', password1='password', password2='password')
    user.save()
    post = Post.objects.create(user=user, image='image/upload/v1654464303/dhagnnfxtfd9ldneefvv.jpg', 
                               caption='test image', )
    post.save()
    
    self.assertEqual(str(post), 'banana')
    
   def test_create_ratings(self):
    user = User.objects.create_user(username='banana', email='banana@gmail.com', password1='password', password2='password')
    user.save()
    post = Post.objects.create(user=user, image='image/upload/v1654464303/dhagnnfxtfd9ldneefvv.jpg', 
                               caption='test image', )
    post.save()
    
    ratings = Ratings.objects.create(user=user, post=post, body='just commented')
    ratings.save()
    self.assertEqual(str(ratings), 'just commented')